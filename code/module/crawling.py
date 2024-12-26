import requests
from bs4 import BeautifulSoup as bs
import re


def get_ids_with_state(page_num: int, url: str) -> list:
    """
    청년 정책의 ID 수집.
    Parameters:
        page_num (int): 추출하려는 총 페이지 수
        url (str): 추출 대상의 페이지 링크를 조합할 베이스 링크
    Returns:
        policy_id_list (list): 상시, 진행중인 정책의 ID를 list로 모아 반환합니다.
    """
    policy_id_list = []
    for i in range(1, page_num + 1):
        response = requests.get(f"{url}{i}")
        soup = bs(response.text, "lxml")

        badges = soup.select("div.badge")
        titles = soup.select("a.tit")
        organ = soup.select("div.organ-name")

        for j in range(len(titles)):
            badge = badges[j].find("span", attrs={"label"}).text
            if badge in ["진행중", "상시"]:
                policy_id = titles[j].attrs["id"].replace("dtlLink_", "")
                organ_name = re.sub(r"<.*?>", "", str(organ[j].select_one("p")))
                organ_name = "세종" if organ_name == "세종 세종" else organ_name
                if policy_id not in policy_id_list:
                    policy_id_list.append([policy_id, organ_name])

    return policy_id_list


def formated(string: str) -> str:
    """
    HTML 태그, 이스케이프 문자, 과도한 공백 제거.
    """
    tag_format = r"<.*?>"
    string = string.replace("\n", "").replace("\t", "")
    string = re.sub(tag_format, "", str(string))
    string = string.replace("  ", "")
    return string


def crawling(
    policy_id_list: list, url: str, params: dict, cont_attrs: bool = True
) -> list:
    """
    정책 상세 정보를 수집.
    """
    total_policy = []
    format = {"br": r"<br/>", "a": r"<a href"}

    for id, organ in policy_id_list:
        policy = {}
        try:
            response = requests.get(f"{url}{id}")
        except:
            response = requests.get(f"{url.replace('https', 'http')}{id}")

        soup = bs(response.text, "html.parser")

        # 정책 이름 추출
        title = soup.find(params["title"][0], params["title"][1]).text
        policy["정책 이름"] = title

        if cont_attrs:
            policy["기관"] = organ
            subtitle = soup.find("p", "doc_desc").text
            subtitle = subtitle.replace("\r", " ")
            subtitle = subtitle.strip()
            policy["요약"] = subtitle
            list_tit = soup.find_all(
                name=params["list_tit"][0], attrs=params["list_tit"][1]
            )
            list_cont = soup.find_all(
                name=params["list_cont"][0], attrs=params["list_cont"][1]
            )
        else:
            list_tit = soup.find_all(name=params["list_tit"][0])
            list_cont = soup.find_all(name=params["list_cont"][0])

        # 항목 내용 처리
        for i in range(len(list_tit)):
            # list_cont[i].contents = ["\n", "ㅁㅁㅁ", "\n"] 또는 ["\n\t\t\t\tㅁㅁㅁㅁ\n\t\t\t\t", "<br/>", "ㅁㅁㅁ"]과 같이 나옴
            if len(list_cont[i].contents) > 1:
                contents = []
                for j in range(len(list_cont[i].contents)):
                    content = list_cont[i].contents[j]
                    # <br/> 제거
                    if re.match(format["br"], str(content)) != None:
                        content = None
                    # url만 있는 경우 추출
                    elif re.match(format["a"], str(content)) != None:
                        content = content.attrs["href"]
                    # 그 외 공백 제거, '\n', '\t', 제거 안된 html 태그 제거
                    else:
                        content = content.text
                        content = content.strip()
                        content = formated(content)
                    # 처리 작업이 끝난 후 의미있는 요소만 contents(list)에 추가
                    if content not in [None, "\n", "", ","]:
                        # \r이 있을 경우 이를 구분자로 분할한 뒤 삽입
                        if "\r" in content:
                            content = content.split("\r")
                            for con in content:
                                contents.append(con)
                        else:
                            contents.append(content)
                if len(contents) == 1:
                    contents = "".join(contents)
            else:
                contents = list_cont[i].contents
                contents = "".join(contents)
                contents = formated(contents)

            # 동일한 요소가 contents(list)에 들어있을 경우
            if (
                isinstance(contents, list)
                and len(contents) == 2
                and contents[0] == contents[1]
            ):
                contents = set(contents)
                contents = "".join(contents)
                contents = formated(contents)
            # 정책의 항목 이름, 내용 연결
            policy[list_tit[i].text] = contents
        total_policy.append(policy)
    return total_policy

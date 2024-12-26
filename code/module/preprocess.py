import re

############## 사용되지 않는 항목, 값 삭제 #################
# 삭제 항목 정의
remove_keys = [
    "요약",
    "정책 번호",
    "신청 사이트",
    "사업관련 참고 사이트 1",
    "사업관련 참고 사이트 2",
    "첨부파일",
]

remove_values = [
    "제한없음",
    "",
    "-",
    "상관없음",
    "□제한없음",
    "□ 제한없음",
    "- 제한없음",
    "-제한없음",
]


# 삭제 함수 정의
def remove_keys_from_data(data, keys):
    if isinstance(data, list):
        return [remove_keys_from_data(item, keys) for item in data]
    elif isinstance(data, dict):
        return {
            key: remove_keys_from_data(value, keys)
            for key, value in data.items()
            if key not in keys
        }
    else:
        return data


def remove_values_from_data(data):
    if isinstance(data, list):
        return [
            remove_values_from_data(item) for item in data if item not in remove_values
        ]
    elif isinstance(data, dict):
        return {
            key: remove_values_from_data(value)
            for key, value in data.items()
            if value not in remove_values
        }
    else:
        return data


######### 불용어 ###########
# 불용어
stopwords = [
    "수행",
    "경우",
    "해당",
    "통하여",
    "대한",
    "관련",
    "등",
    "및",
    "또는",
    "중인",
    "통해",
    "따라",
    "서비스",
    "제공",
    "프로그램",
    "참여",
    "따른",
    "관한",
    "이용",
    "등을",
    "두고",
]


# 제거 함수
def remove_text(text):
    if isinstance(text, str):
        # URL 제거
        text = re.sub(r"\bhttps?://[^\s]*\.kr\b", "", text)

        # 특수기호 제거 (숫자, 한글, 영어 유지)
        text = re.sub(r"[^가-힣a-zA-Z0-9\s.~%]", " ", text)

        # 불용어 제거
        for stopword in stopwords:
            text = text.replace(stopword, "")
        return text

    return text


# 데이터 처리
def process_json(data):
    if isinstance(data, dict):
        return {key: process_json(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [process_json(item) for item in data]
    elif isinstance(data, str):
        return remove_text(data)
    else:
        return data


######### 토큰화 ##############
# 키-값을 문자열로 병합
def key_value_to_string(key, value):
    """
    키와 값을 병합하여 문자열로 반환
    """
    merged_value = merge_values(value)
    return f"{key}:{merged_value}"


# 리스트, 딕셔너리, 문자열 병합
def merge_values(item):
    """
    리스트, 딕셔너리, 문자열을 하나의 문자열로 병합
    """
    if isinstance(item, list):
        return " ".join(merge_values(sub_item) for sub_item in item)
    elif isinstance(item, dict):
        return " ".join(f"{key}:{merge_values(value)}" for key, value in item.items())
    elif isinstance(item, str):
        return remove_text(item)
    else:
        return str(item)


# 정책 이름을 키로 사용하고 나머지 키-값을 리스트로 변환
def tokenize_by_policy_name(data):
    """
    정책 이름을 키로 사용하고, 나머지 키-값을 리스트로 변환합니다.
    """
    result = {}
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "정책 이름" in item:
                policy_name = item["정책 이름"]

                # 나머지 키-값을 리스트로 변환
                tokenized_content = [
                    key_value_to_string(key, value)
                    for key, value in item.items()
                    if key != "정책 이름"
                ]

                result[policy_name] = tokenized_content
    return result

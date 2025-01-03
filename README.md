# <br>🧐**내게 필요한 청년정책 알려줘! 챗봇**🤖
> **SK Networks AI CAMP 6기 - 1Team** <br/> **개발기간: 2024.12.24 ~ 2024.12.26**
---

# **개발 팀** <br>
## <br> **팀명** <br>
![team_name](https://github.com/user-attachments/assets/c623e101-7db5-4e9e-8d26-b04ec270185f)

## <br> **팀 소개** <br>
| 고성주 | 김지영 | 이세화 | 정유진 | 정지원 |
|:----------:|:----------:|:----------:|:----------:|:----------:|
| ![1_sj](https://github.com/user-attachments/assets/9fb495e0-732f-4eb3-9dc0-541eccbcd2e4)| ![2_jy](https://github.com/user-attachments/assets/f3940834-2f8e-4b5d-9988-d85c0f4c6cab)| ![3_sh](https://github.com/user-attachments/assets/8b62f945-e894-49e0-abd4-35f4e5d4010b)| ![4_yj](https://github.com/user-attachments/assets/16dd5434-fd43-42f6-aaa9-1b6b2a90a812)| ![5_jw](https://github.com/user-attachments/assets/4aaa4891-38ea-4679-be53-6d3741c33255)|
| 데이터 수집,성능 평가 | RAG 시스템 | 데이터 전처리,RAG 시스템 | 데이터 수집 | 성능 평가,발표 |
<br>

---

# **프로젝트 개요** <br>
## <br> **소개** <br>
> &nbsp;정부에서 진행 중인 청년 정책을 소개해 주는 RAG기반 챗봇 시스템입니다. 대화를 통해 사용자의 조건에 적합한 청년 정책들을 추천해 줍니다.

## <br> **필요성** <br>
> - 정부는 청년들의 경제적·사회적 자립을 돕기 위해 다양한 분야에 막대한 예산을 투입하여 여러 청년 정책을 시행하고 있습니다. 그러나 많은 청년들이 이런 기회들을 놓치고 있습니다.
> - 청년 정책은 매우 방대하여 자신에게 맞는 정책을 찾기가 쉽지 않습니다. 정보가 산발적으로 흩어져 있어 존재하는지도 모르고 지나치는 정책들도 있으며, 본인이 지원 대상에 해당하는지 일일이 확인해야 하고 어떤 정책이 더 큰 혜택을 제공하는지 비교하는 것도 많은 시간과 노력이 필요합니다. 이러한 복잡성은 청년들이 정책을 적극적으로 활용하지 못하게 만드는 주요 원인 중 하나입니다.
> - 이러한 상황에서 질문과 답변을 통해 맞춤형 청년 정책을 추천하는 RAG 기반 챗봇은 큰 도움이 됩니다. 이 챗봇은 사용자에게 적합한 정책들을 빠르고 정확하게 소개합니다. 이를 통해 청년들은 복잡한 정보 탐색 과정 없이 손쉽게 지원 가능한 정책을 확인하고, 더 많은 혜택을 누릴 수 있을 것입니다.
<br>

---

# **기술** <br>
## <br> **01. 데이터 수집**
### **데이터 크롤링**
<br>

**온통청년** ([https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do]()) 크롤링 진행<br>

    {
        "사업명": "청년월세 특별지원 사업(2차)",
        "요약": "19세~34세 청년 대상 월 최대 20만원까지, 12개월 간 월세 지원",
        "정책 번호": "R2024030420286",
        "정책 분야": "주거분야",
        "지원 내용": "실제 납부하는 임대료 범위 내에서 월 최대 20만원씩 최장 12개월에 걸쳐 분할 지급",
        "사업 운영 기간": "-",
        "사업 신청 기간": "2024년 02월26일 ~ 2025년 02월25일",
        "지원 규모(명)": "-",
        "비고": "2024.02.26.~2025.02.25.",
        "연령": "만 19세 ~ 34세",
        "거주지 및 소득": "□ (소득·재산요건) 청년 본인가구와 부모 등을 포함하는 원가구의 소득 및 재산을 고려하며, 세부 기준은 첨부파일 참고",
        "학력": "-",
        "전공": "-",
        "취업 상태": "-",
        "특화 분야": "-",
        "추가 단서 사항": "-",
        "참여 제한 대상": "주택 소유자(분양권, 입주권 포함), 2촌 이내 주택 임차자, 보증금 5천만원 초과 주택 거주자, 「공공주택특별법」에 따른 공공임대주택 거주자, 1실에 다수가 거주하는 형태의 전차인, 지자체 시행 기존 월세지원 수혜자",
        "신청 절차": "모의계산 서비스를 통해 지원 대상 해당 여부 확인 후, 신청 서류를 구비하여 복지로(누리집 또는 어플리케이션) 혹은 거주지의 기초자치단체로 신청",
        "심사 및 발표": "-",
        "신청 사이트": "복지로 홈페이지",
        "제출 서류": "월세지원 신청서, 소득·재산 신고서, 임대차계약서 및 최근 3개월간 월세이체 증빙서류, 통장 사본, 가족관계증명서 등",
        "기타 유익 정보": "-",
        "주관 기관": "국토교통부 주택토지실 주거복지지원과",
        "운영 기관": "-",
        "사업관련 참고 사이트 1": "https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95089642",
        "사업관련 참고 사이트 2": "",
        "첨부파일": "240412(조간) 보증금 월세 관계없이 청년월세 특별지원 신청하세요(청년주거정책과).pdf"
    },


## <br> **02. 데이터 전처리**
### **항목 삭제**
- key 값 삭제 -> ["요약", "정책 번호", "신청 사이트", "사업관련 참고 사이트 1", "사업관련 참고 사이트 2", "첨부파일"]
- 의미 없는 value값 삭제 -> ["제한없음", "", "-", "상관없음", "□제한없음","□ 제한없음","- 제한없음","-제한없음"]
### **텍스트 전처리**
- 불용어 제거 -> [
    "수행", "경우", "해당", "통하여", "대한", "관련", "연", "있는", "자", "기준",
    "시", "가능", "신청", "등", "및", "확인", "포함", "또는", "중인",
    "후", "심사", "통해", "따라", "서비스", "제공", "프로그램", "참여", "따른",
    "단", "추가", "중", "수", "맞춤형", "대한", "해당", "관한", "이용", "그",
    "개별", "등을", "두고"
- url 삭제 -> 정규표현식이 'http://'(http,https),'.kr'인 경우 삭제
- 특수기호 제거 -> re.sub(r'[^가-힣a-zA-Z0-9\s.]',' ', text)
### **토큰화**
- 문자열 단어 단위로 토큰화
- 청년 정책 챗봇은 정확한 정보 전달을 최우선으로 여김 -> chunk size를 지정해 토큰화하지 않고 key-value값 병합된 문자열을 하나의 토큰으로 나눔

> **key- value값 병합**
> - key 값:'정책 이름', '기관', '요약', '정책 분야'인 경우는 유지
> - 나머지 모든 key,value값 문자열로 반환 -> 병합 후 key 값:"내용"의 value값에 저장

<br>

### **성능 평가 이후 추가 설정 사항**
- 질문을 명확하게 이해하고 관련 문서를 분류하는 능력이 부족하다고 판단.
- 추가 설정

    ① "기관" 값을 "지역"으로 변경 : "기관": "인천 계양구" -> "지역": "인천 계양구" <br> 
    ② key값 띄어쓰기 삭제 <br>
    ③ <정책 분야>에서 "분야" 삭제 <br>

  
## <br> **03. RAG 시스템 개발**
### **디렉토리 설정**
1) 경로 설정:  text-embedding-ada-002
   고품질 임베딩을 생성하기 위해 해당 임베딩 모델을 선택함

2) JSON 데이터 불러오기
   - 개별 정책 text를 통합하여 metadata와 함께 JSON 문서를 생성
  
### **Retriever 설정**

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 10,
            "lambda_mult": 0.2,
        },
    )
        
### **DB 기반 검색 도구, Web 기반 검색 도구 생성**
- 데이터에 빠르게 접근하고, 최신 외부 정보를 검색할 수 있도록 tool 생성

        # db 검색 tool
        @tool
        def search_policy(query: str) -> list[Document]:
            """
            Vector Store에 저장된 청년 지원 정책과 해당 정책의 정보를 검색한다.
            이 도구는 청년 지원 정책 관련 질문에 대해 실행한다.
            """
            result = retriever.invoke(query)
            return result if result else [Document(page_content="검색 결과가 없습니다.")]
        
        
        # web 검색 tool
        @tool
        def search_web(query: str) -> list[Document]:
            """
            Web에서 청년 지원 정책과 해당 정책의 정보를 검색한다.
            이 도구는 청년 지원 정책 관련 질문에 대해 실행한다.
            """
            try:
                tavily_search = TavilySearchResults(max_results=2)
                result = tavily_search.invoke(query)
                if result:
                    return [
                        Document(
                            page_content=item.get("content", ""),
                            metadata={"title": item.get("title", "")},
                        )
                        for item in result
                    ]
                else:
                    return [Document(page_content="검색 결과가 없습니다.")]
            except Exception as e:
                return [Document(page_content=f"오류 발생: {str(e)}")]
  

### **Prompt 설정**
- 주요 설정 사항

        """
        3. 답변에 불필요한 정보는 제공하지 마세요.
        7. 질문을 완전히 이해하지 못할 경우, 구체적인 질문을 다시 받을 수 있도록 사용자에게 유도 질문을 하세요.
        """


### 질문-응답 프로세스
- **사용자 질문 입력** > **검색 결과 통합** > **LLM 메세지 구성** > **최종 응답 생성 > log 저장**

 
## <br> **04. 성능 평가**
### **질문-답변 생성**
- 평가 데이터로 사용할 context 100개를 랜덤으로 추출한 뒤, 각 3개씩의 질문-답변 쌍을 생성하여 **총 300개의 질문-답변 쌍**을 생성
<br>

**prompt 작성** <br>

          {
            """
            당신은 RAG 평가를 위해 질문과 정답 쌍을 생성하는 인공지능 비서입니다.
            해당 RAG는 사용자에게 각 정책에 대한 질의응답을 위해 만들어졌으니 이를 참고하여 평가 질문과 정답 쌍을 생성하세요.
            주어진 [Context]를 활용해서 최대한 다양한 질문-정답 쌍을 만들어 주세요.
            다음 [Context] 에 문서가 주어지면 해당 문서를 기반으로 {num_questions}개 질문-정답 쌍을 생성하세요.
    
            질문과 정답을 생성한 후 아래의 출력 형식 GUIDE 에 맞게 생성합니다.
            질문은 반드시 [Context] 문서에 있는 정보를 바탕으로 생성해야 합니다. [Context]에 없는 내용을 가지고 질문-정답을 절대 만들면 안됩니다.
            질문은 간결하게 작성합니다.
    
            질문을 만들 때 반드시 각 [Context] 문서의 "정책 이름"을 질문에 포함해야합니다.
            예시는 "경남 저소득 증장애인 집정리 범사업을 주관하는 기관은 어디인가요?" 라는 형식의 질문 생성입니다.
    
            하나의 질문에는 한 가지의 내용만 작성합니다.
            질문을 만들 때 "제공된 문맥에서", "문서에 설명된 대로", "주어진 문서에 따라" 또는 이와 유사한 말을 하지 마세요.
            정답은 반드시 [Context]에 있는 정보를 바탕으로 작성합니다. 없는 내용을 추가하지 않습니다.
            질문과 정답을 만들고 그 내용이 [Context] 에 있는 항목인지 다시 한번 확인합니다.
    
            어떤 형식으로 만들었든 생성된 질문-답변 쌍은 반드시 dictionary 형태로 정의하고 list로 묶어서 반환해야 합니다.
            어떤 형식으로 만들었든 질문-답변 쌍은 반드시 {num_questions}개를 만들어야 합니다.

            """
            }
### **RAG Chain 구성**
- Vector Store와 web에서 검색한 context들과 RAG 시스템의 응답이 출력되도록 chain을 구성

### **평가**

> - **LLMContextRecall**: 컨텍스트를 기반으로 정보를 재현한 능력을 측정
> - **LLMContextPrecisionWithReference**: 문서의 정확하고 관련된 정보를 기반으로 답변을 생성했는지 평가
> - **Faithfulness**: 문서의 내용에 얼마나 충실하게 답변했는지 평가
> - **AnswerRelevancy**: 질문과 답변 간의 의미적 관련성을 측정

<br>

### **평가 결과**
- **문맥 회수율**(0.6406)과 참조 기반 **문맥 정밀도**(0.6265)가 균형을 이루며, **답변 충실도**(0.7462)는 상대적으로 높고, **답변 적합성**(0.5982)은 개선의 여지가 있는 것으로 나타남
  
| LLMContextRecall | LLMContextPrecisionWithReference | Faithfulness | AnswerRelevancy |
| :--------------: | :--------------: | :--------------: | :--------------: |
| 0.6406 | 0.6265 | 0.7462 | 0.5982 |

---

# **Review** <br>

> 고성주: 한게 너무 없네요... 팀원분들 고생 많으셨습니다~~!
> 
> 김지영: 좋은 성능의 시스템을 개발하는 것이 생각보다 어렵네요... 설계하는 단계를 좀 더 명확히 익히고 작동 원리를 이해해야겠다는 생각을 했습니다! 다들 고생하셨어요 ❤️
> 
> 이세화: RAG 기반 챗봇을 체계적으로 습득할 수 있었습니다. 아쉬운 부분은 다음 프로젝트때 반영하도록 하겠습니다!! 다들 고생 많으셨어요☺️
> 
> 정유진: 크롤링 어디까지 끌어오는거에요? 끝이 왜 없지!
> 
> 정지원: 모델 성능 향상시키는데 꽤나 힘들었네요ㅠㅠ 다들 고생하셨습니다! 다음 프로젝트도 화이팅...!!



from fastapi import APIRouter
import random
from fastapi.responses import JSONResponse


router = APIRouter()

#질문
response_data = {
  "quiz": [
    {
      "question": "미국 경제성장률은 둔화하고 물가상승률은 고공행진하면서 ‘이것’에 대한 우려가 다시 높아졌다. 이것에 적절한 단어는?",
      "options": ["디플레이션", "스태그플레이션", "빅스텝", "베이비스텝"],
      "answer": "스태그플레이션"
    },
    {
      "question": "주가 하락을 예상하고 주식을 보유하지 않은 상태에서 빌려서 매도 주문을 내는 투자 기법은?",
      "options": ["따따상", "손절매", "사이드카", "공매도"],
      "answer": "공매도"
    },
    {
      "question": "다음 중 현재 글로벌 금융시장에서 기축통화로 가장 널리 인정받고 있는 화폐는 무엇일까??",
      "options": ["위안", "달러", "유로", "엔"],
      "answer": "달러"
    },
    {
      "question": "미국의 ‘니어쇼어링’으로부터 경제가 큰 수혜를 받는 나라로 꼽힌다. 미국과 국경이 맞닿아 있고 화폐는 페소화를 쓰는 이 국가는?",
      "options": ["베트남", "멕시코", "쿠바", "브라질"],
      "answer": "멕시코"
    },
    {
      "question": "물가가 상승 기조를 유지하고는 있지만 상승폭이 차츰 줄어드는 현상은?",
      "options": ["디플레이션", "하이퍼인플레이션", "디스인플레이션", "스태그플레이션"],
      "answer": "디스인플레이션"
    },
    {
      "question": "‘경제성장률’은 이것이 얼마나 증가했거나 감소했는지를 가리킨다. 이것은 무엇일까?",
      "options": ["1인당 GNI", "실질 GDP", "경상수지", "외환보유액"],
      "answer": "실질 GDP"
    },
    {
      "question": "새마을호보다 두 배 빠른 고속철도인 ‘이것’이 이달 개통 20주년을 맞았다. 누적 승객 10억 명을 넘은 이것은?",
      "options": ["GTX", "KTX", "LCC", "OTT"],
      "answer": "KTX"
    },
    {
      "question": "국가가 과도한 빚 부담을 이겨내지 못하고 상환능력을 잃을 때 일어날 수 있는 상황은?",
      "options": ["캐즘", "어닝쇼크", "디폴트", "유동성랠리"],
      "answer": "디폴트"
    },
    {
      "question": "신용등급이 낮은 투기등급 채권에 집중 투자해 고수익·고위험을 추구하는 펀드는?",
      "options": ["액티브펀드", "매칭펀드", "비전펀드", "하이일드펀드"],
      "answer": "하이일드펀드"
    },
    {
      "question": "증시에서 ‘대형 우량주’를 뜻하는 말이다. 안정적 이익을 내고 재무구조가 건전한 기업의 주식인 이것은?",
      "options": ["스톡옵션", "블루칩", "자사주", "관리종목"],
      "answer": "블루칩"
    },
    {
      "question": "한 가지 자산에 몰아서 투자하지 않고 여러 자산에 ‘분산투자’하는 것의 가장 주된 목적으로 볼 수 있는 것은?",
      "options": ["복리 효과", "절세 효과", "위험 추구", "위험 회피"],
      "answer": "위협 회피"
    }
  ]
}
    
@router.get("/")
def get_data():    
    random_quiz = random.choice(response_data["quiz"])
    return JSONResponse(content=random_quiz,media_type="application/json; charset=utf-8")

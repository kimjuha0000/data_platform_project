# main.py 상단 수정
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from datetime import datetime
import random
from faker import Faker

app = FastAPI()
fake = Faker() # 가짜 데이터를 만들기 위한 인스턴스

class UserAction(BaseModel):
    user_id: str
    action: Literal['view', 'click', 'purchase']
    product_id: str
    timestamp: datetime

@app.get("/")
def read_root():
    """
    서버의 루트 경로로 접속했을 때 간단한 환영 메시지를 반환합니다.
    """
    return {"message": "데이터 플랫폼 API 서버에 오신 것을 환영합니다!"}


# main.py 하단에 추가
@app.post("/log")
def log_user_action() -> UserAction:
    """
    가상의 사용자 행동 로그를 생성하여 반환합니다.
    """
    action_log = UserAction(
        user_id=fake.uuid4(),
        action=random.choice(['view', 'click', 'purchase']),
        product_id=f"prod-{random.randint(1, 100)}",
        timestamp=datetime.now()
    )
    return action_log
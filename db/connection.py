# 데이터베이스 사용 방법

# 1. connection 맺기 (DB ======= Python)
#   - IP      : 컴퓨터 주소
#   - Port    : 27017
#   - ID & PW : 계정 정보
# 2. 명령 보내기      (Python ------> DB)
# 3. 결과 받기        (DB ------> Python)
# 4. connection 끊기 (Python XXXXXXX DB)

from pymongo import MongoClient

# MongoDB Connection
def conn():
    # Python-MongoDB 연결
    client = MongoClient("mongodb+srv://cnu:cnu1234@movieorange.j3uospk.mongodb.net/")
    db = client["review"]  # DB 선택

    collection = db.get_collection("movie")
    return collection

# MongoDB 구조
#   - MongoDB(DBMS) : 데이터베이스 관리 시스템
#     ㄴ DB(NAVER) : 프로젝트 단위
#        ㄴ Collection(회원)
#        ㄴ Collection(카페)
#        ㄴ Collection(쇼핑)
#        ㄴ Collection(메일)
#     ㄴ DB(KAKAO)
#     ㄴ DB(BLOG)

# MongoDB 데이터 주고받기
#   - MongoDB는 BSON Type으로 데이터를 주고받음
#   - BSON(Binary JSON) = JSON과 거의 동일
#   - 그냥 JSON은 Type으로 사용하면 됨(문제 없음)
#   - Python에서 JSON은 Dict Type 사용!(Python Dict = JSON)
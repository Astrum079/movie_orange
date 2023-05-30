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
    client = MongoClient("mongodb+srv://cnu:cnu1234@movieorange.j3uospk.mongodb.net/")
    db = client["movie"]

    collection = db.get_collection("movie")
    return collection

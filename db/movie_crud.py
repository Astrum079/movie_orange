# CRUD
#  - CREATE : 생성
#  - READ   : 조회
#  - UPDATE : 수정
#  - DELETE : 삭제

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

from db.connection import conn

# 리뷰 저장(MongoDB)
def add_review(data):
    collection = conn()  #Conn(DB : review, Collection : movie) 정보
    collection.insert_one(data)  # 1건 저장(CREATE)

#리뷰 조회(MongoDB)
def get_reviews():
    review_list = []  #MongoDB에서 가져온 Data 저장

    collection = conn()  #Connection 맺기
    # find({조건},{컬럼 선택}) : 데이터 조회
    # 조건 예 : 평점 8점 이상 조회
    # 컬럼 선택 예 : review, score 조회
    #    *컬럼 (title, review, score, writer, regdate
    #    *_id(고유 식별값) 기본으로 조회 설정
    for one in collection.find({},{"_id":0, "title":1, "score":1, "review":1}):
        review_list.append(
            [
                one["title"],
                one["review"],
                one["score"]
            ]
        )
    return review_list
#국룰 : 마지막 줄에 빈 줄 추가해주기

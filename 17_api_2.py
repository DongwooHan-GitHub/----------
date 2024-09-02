
import requests

# 기상청 API 요청 URL
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

# 서비스키를 저장할 변수
serviceKey = "WJKo4RHlXcza+DgAA0I294iDTMwbvak5Y2wdNilzAaD5B4FpEfgHF3gsB7z9ea+S+N9Hvi27MNI+XnpWU6vzVQ=="

# API 요청 파라미터 설정
parameter = {
    'serviceKey': serviceKey,   # 서비스 키
    'pageNo': '1',              # 페이지 번호
    'numOfRows': '1000',        # 한 페이지에 조회할 데이터 수
    'dataType': 'JSON',         # 응답 데이터 형식 (JSON)
    'base_date': '20210628',    # 기준 날짜 (YYYYMMDD)
    'base_time': '1900',        # 기준 시간 (HHMM)
    'nx': '55',                 # 격자 X 좌표
    'ny': '127'                 # 격자 Y 좌표
}

# GET 요청 보내기
response = requests.get(url, params=parameter)

data = response.json()

from  pprint import pprint

# 응답 데이터의 키 response 에 대한 인덱싱
response_key = data["response"]

body_key = response_key["body"]


# 키 items 에 대한 인덱싱
items_key = body_key["items"]

# 키 item에 대한 인덱싱
items_key = items_key["item"]
pprint(body_key)


# 날씨 정보 목록이 저장된 "item" 데이터 추출
item_list = data["response"]["body"]["items"]["item"]

pprint(item_list)

for item in item_list:
    """
    pprint(item)
    print(type(item))
    """
    


    # 날씨 중 키 category 정보만 추출
    # 키 category 인덱싱
    category = item["category"]
    print(category)
"""
# 위 데이터 추출 코드까지의 과정

# 응답 데이터의 키 response 에 대한 인덱싱
response_key = data["response"]

# 키 body 에 대한 인덱싱
body_key = response_key["body"]

# 키 items 에 대한 인덱싱
items_key = body_key["items"]

# 키 item 에 대한 인덱싱
item_key = items_key["item"]

pprint(item_key)
"""

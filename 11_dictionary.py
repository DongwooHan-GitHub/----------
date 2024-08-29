# 11_dictionary
# 08.26일 월요일
# 딕셔너리(dict) / 사전형 자료형

# 딕셔너리 특징
# 1. 하나의 원소에 두 개의 데이터가 필요하다.
# 키(key) - 값(value) : 키 벨류, 키 값, 식별자 값
# 2. 순서가 없다.
# 3. 중복된 키(key)는 저장이 불가능하다.

# 딕셔너리 원소 생성
# 키와 밸류의 구분(매핑):(콜론)
# 각각 다른 키와 밸류(원소)의 구분은,(쉼표)

# 딕셔너리 생성
# 원소(키는 "키", 밸류는 "밸류"}를 생성
# 키가 "age", 밸류가 20인 원소를 추가 생성
dict_1 = {"키":"밸류",
           "key":"value",
           "age":20, 
          0:"한동우"} # 키의 숫자 0은 위치를 의미 X


# 키(key)를 이용한 인덱싱(접근)
# 키(key)가 "age" 인 밸류(value) 인덱싱(접근) 코드
age = dict_1["age"]
print(age)

# 개인 정보를 저장한 딕셔너리를 생성하고 변수에 할당하는 코드
# 이름 / 사는 구 / 키

dict_2 = {
    "name":"한동우",
    "from":"영등포구",
    "height" : 181

}
# 이름 사는구 키에 대해서 인덱싱 후 출력하는 코드
print(dict_2["name"])
print(dict_2["from"])
print(dict_2["height"])

# 원소의 추가 수정 삭제
dict_3 = {}
# 딕셔너리 원소의 추가 : 새로운 키(key) 에 대해 인덱싱 후 값(value) 저장
dict_3["name"] = "한동우"
print(dict_3)

# 딕셔너리 원소 수정 : 키(key)에 대해 인덱싱 . 후새로운 값(value) 재할당
dict_3["name"] = "홍길동"
print(dict_3)


dict_4 = {}
# 비어있는 딕셔너리에 key "사는곳" 에 대한 value "장한평역" 원소를 생성하는 코드 작성
dict_4["from"] = "장한평역"
print(dict_4)
# key "사는곳" 에 대해 value 수정하는 코드
dict_4["from"] = "양평역"

dict_5 = {}
# 두 개의 원소를 생성
# key는 "정수" value는 [1,2,3]
# key는 "실수" value는 (1.0, 2.0, 3.0)
dict_5 = {"정수":[1,2,3]}
print(dict_5)
dict_5 = {"실수":(1.0, 2.0, 3.0)}

print(dict_5)

# 딕셔너리에 대한 맴버쉽 연산자(in / not in)
# 특정 값이 원소에 포함되는지 검사하는 연산자
# 리스트 -> 원소의 데이터 1개
# 딕셔너리 -> 원소의 데이터 2개(key - value)

dict_6 = {
    "일":1,
    "이":2
}

result_1 = "일" in dict_6
result_2 = 1 in dict_6
print(f"result1 = {result_1}")
print(f"result2 = {result_2}")
# 딕셔너리에 대한 맴버쉽 연산자 검사는 키(key) 모음에 대해서 검사한다.

reuslt_3 = "삼" in dict_6
print(reuslt_3)

# 딕셔너리 값(value) 모음에 대해 검사를 하고 싶을 때?
# 딕셔너리.values() : 딕셔너리의 값(value) 모음을 생성하는 도구
result_4 = 1 in dict_6.values()
print(result_4)


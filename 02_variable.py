# 02_variable.py
# 학습날짜 : 8월 20일 화요일
# 파이썬 프리코스 2회차
# 학습 내용 : 변수

# 변수란?
# 데이터를 저장하는 상자 / 공간

# 변수 생성과 데이터(값) 저장
# 변수명 = 데이터
# = (할당 / 저장 연산자) : 변수명에 데이터를 할당 저장한다.

a = "a" # 문자열 "a" 를 변수 a 에 할당(저장)
number = 1 # 정수 1을 변수 number  에 할당
# 실수 1.0을 변수 number2에 할당
print(a)

string = "hello World"
print(string)

# 유지보수
print("hello python")
print("hello python")
print("hello python")
print("hello python")
print("hello python")


string = "hello python"
print(string)
print(string)
print(string)
print(string)
print(string)


# 문제, 문자열 정수가 저장된 리스트를 반복해서
# 각 원소를 정수형(int)로 변환해서 출력(type())
list3 = ["1", "2", "3"]
list4 = [] # 정수로 변환한 데이터를 자료형 정수형(int) 변환 후 변수에 할당


for string in list3:
    number = int(string)
    print(number, type(number))
    list4.append(number)
    print(list4)
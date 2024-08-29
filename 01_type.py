# 8월 19일 1회차 내용
# 배운 내용
# Python 설치, VScode  설치
# VScode 사용법, Python 사용법
# 주석 작성 방법

# print("hello world")

"""
큰 따옴표 (") 3개를 위 아래로 작성하면 여러 줄 주석이 된다.
"""

# 파이썬 자료형
# 숫자형 자료형
# 양의 정수, 음의 정수, 0


print(10)
print(-10)
print(0)
print(type(10))
print(type(-10))
print(type(0))

# 실수형 (float) 자료형
# 소수점이 있는 숫자
print(10.1)
print(-10.1)
print(0.0)
print(10.0)
print(type(10.1))
print(type(-10.1))
print(type(0.0))
print(type(10.0))


# 문자열 자료형
# (문자) 들의 나(열)
# 첫 번째 생성 방법 : 큰 따옴표 ""
print("Hello World")

# 두 번째 생성 방법 : 작은 따옴표 ''
print('Hello World')

print(10)
print("10")

print(type(10))
print(type("10"))

# 불린형
# 참(True) or 거짓(False) 2개의 값만 가지는 자료향

# 형 변환
# 자료형을 변환시키는 기능
# 예시) 정수형 -> 문자열 / 문자열 -> 정수형 / 실수형 -> 정수형
# type() 기능의 결과물 : int / float / str / bool
# 정수형(int) 변환
# int() : 다른 자료형을 정수형으로 변환하는 기능
print(int("10"))
print(type(int("10")))

# 실수형 데이터 -> 정수형 데이터로 변환
print(int(1.5))
print(type(int(1.5)))

print(bool(0)) # 정수형의 거짓 표현
print(bool(0.0)) # 실수형의  거짓 표현
print(bool("")) # 문자열의 거짓 표현

print(bool("0.0")) # 참(True) 으로 표현
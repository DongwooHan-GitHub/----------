# 04_operator.py

number1 = 10
number2 = 20

plus = number1 + number2 # 10과 20을 더한 데이터를 plus 할당
print(plus)

minus = number1 - number2
print(minus)

multiple = number1 * number2
print(multiple)

division = number1 / number2
print(division)

# 추가 산술 연산
# 목 계산, 나머지 계산, 제곰 계산
# // , %(shift + 5), **


quotient = number1 // number2
remain = number2 % number1 
square = number1 ** 2

print(quotient)
print(remain)
print(square)

number1 = number1 + number2

# 축약 연산자 표현
number1 += number2

# 비교연산자
# 두 데이터를 비교 (크다, 작다, 다르다, 초과, 미만, 이상, 이하)한다.
# 비교의 결과는 boolean형 (참/ 거짓)이다.

# 같다 == 
# 다르다 !=
# 초과, 미만 < > 
# 이상, 이하 >= ,<=

number3 = 3
number4 = 4
# 같다
print(number3 == number4)

#다르다
print(number3 != number4)

#초과
print(number3 > number4)

# 미만
print(number3 < number4)

# 이상
print(number3 >= number4)

# 이하
print(number3 <= number4)

print(1 == "1")

print(1 == 1.0)
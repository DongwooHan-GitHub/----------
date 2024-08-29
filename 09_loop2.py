# 09_loop_2
# 08.23일 금요일
# while 반복문

# while 반복문
# 조건식이 들어가는 반복문
# 조건식이 결과가 참(True) 이면 반복하는 반복문

# while 반복문 사용법
"""
while 조건식:
    1.코드블럭
    반복해서 실행할 코드 블럭
"""

# 1부터 10까지 출력하는 반복문
number = 1
print(number)

number =+ 1
print(number) # 2

number =+ 1 # 3
print(number)

# number 가 11이 아니면 위 코드가 반복해서 실행

number = 1
while number != 11:
    print(number)
    number = number + 1

# while 반복문 주의할 점
# 1. 조건식의 조건 변수
# 2. 조건 변수에 대한 적절한 변화식이 필요
#  - 적절한 변화식 : 조건식을 언젠가는 만족하지 않게 만드는 코드(식)

# 문제. number2에 2를 곱한 값을 반복해서 출력
# 값이 1000 보다 작은 값들만 출력
number2 = 2 
while number2 <= 1000:
    print(number2)
    number2 = number2 * 2


for _ in range(3):
    print("hello")
    # break : 반복문의 반복을 종료하는 키워드
    break


number = 1
while number < 10:
    print(number)
    number = number + 1
    break

print(number)


# 리스트 내부 원소를 하나씩 출력하는 코드
# 이 때 10보다 크면 반복문을 종료한다

numbers3 = [0,4,2,11,3,2,1,5]

for number in numbers3:
    print(numbers3)
    if number > 10:
        break


# 문제. number3 에 대해 더하기 10을 한 값을 반복 출력
# number3 = number3 + 10
# 이 때 , number3이 100을 초과하면 반복문을 종료하는 코드 작성
number3 = 10
while True:
    print(number3)
    number3 = number3 + 10
    if number3 > 100:
        break


# continue 키워드
# 1. continue 아래 코드를 실행하지 않는다.
# 2. break 와 다른 점이라면 다음 반복으로 넘어가게 한다.

numbers4 = [1,2,3,11,4,5]
# 리스트 원소 중 10 이하의 값만 출력

for number in numbers4:
    if number > 10:
        print("continue 를 실행 합니다. 아래 코드들은 실행이 되지 않습니다.")
        continue
    print(number)


numbers = [1,2,3,4,5,6,7,11,20,33,45,50.70]

for num in numbers:
    if num == 33:
        print('found: 33!')
        break
    else:
        print("not Found Sorry", num)    

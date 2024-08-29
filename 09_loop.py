# 레인지(range)의 for 반복문
# 리스트와 사용법은 동일
# 1 부터 10 까지의 연속된 정수 목록을 출력
for number in range(1, 11,1):
    print(number, end=" ") # 1 2 3 4 5 6 7 8 9 10

print("\n")
# 문제2 2 부터 20까지 연속된 정수 목록을 출력, 짝수만 출력
for number in range(2 ,21, 2):
    print(number, end= " ")   # 출력 2 4 6 8 10 12 14 16 18 20 

# N(특정 수) 만큼 반복하고 싶은 코드가 있을 때
# range 활용
print()
# 5번 반복하는 코드
for number in range(5):
    print("안녕하세요")

# 반복문 내부 변수 생략하는 방법
for _ in range(5):
    print("안녕하세요2")

# 리스트 인덱스 활용
# 1. 리스트의 범위
# [1,2,3,4]
# 위치 : 0,1,2,3 -> 0 부터 3까지의 연속된 정수 목록
# len() : 리스트의 길이 (원소의 개수) 구해주는 도구(기능)
# 리스트의 끝 위치 (index) -> 리스트의 길이 -1
number_list = [1,2,3,4,5,6,7]
end = len(number_list) 

# 연속된 위치 목록을 반복해서 출력
for index in range(0,end):
    # print(index)
    # 인덱스를 활용해 원소에 접근 후 출력
    print(number_list[index])

# 문제. 위치(index)가 3 이상인 원소만 출력
# 출력 : 
number_list2 = [0,4,1,7,2,1,9,10]
end = len(number_list2)


# 두 가지 방법
# 첫번째 range 시작 정수 3
for index2 in range(3, end):
    print(number_list2[index])

# 두 번째 조건문 활용
end = len(number_list2)
for index3 in range(0, end):
    print(index3)
    # 조건문, 조건식이 위치 (idx) >=3
    if index3 >= 3:
        print(number_list2[index])

sum1 = 0
for v in range(1, 1000):
    sum1+= v
    print(sum1)
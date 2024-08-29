# 14_2d_loop
# 08.28일 수요일
# 학습 내용 : 중첩 반복문

# y 는 0~9까지 증가하고
# x 는 0~9까지 증가한다.

for y in range(0,10):
    for x in range(0,10):
        # y 와 x 를 동시에 출력, 값의 변화를 관찰
        print(f"y = {y}, x = {x}")

"""
y = 0, x = 0
y = 0, x = 1
y = 0, x = 2
y = 0, x = 3
y = 0, x = 4
y = 0, x = 5
y = 0, x = 6
y = 0, x = 7
y = 0, x = 8
y = 0, x = 9
y = 1, x = 0
y = 1, x = 1
y = 1, x = 2
y = 1, x = 3
y = 1, x = 4
y = 1, x = 5
"""        

# 이차원 리스트 : 리스트를 저장한 리스트
# 일차원 리스트 : 선의 모양
list_1 = [
 [0,1,2], # index = 0
 [3,4,5], # index = 1
 [6,7,8], # index = 2
 [9,10,11] # index = 3
]

list_1_length = len(list_1)
for index in range(list_1_length):
    print(index, list_1[index])
    
    in_list = list_1[index]
    in_list_length = len(list_1[index])
    for in_index in range(in_list_length):
        print(in_index)

"""
0 [0, 1, 2]
1 [3, 4, 5]
2 [6, 7, 8]
3 [9, 10, 11]
"""

# 이차원리스트에 대한 2중 반복문
# 리시트들을 감싸는 바깥 리스트에 대한 반복문 1개
# 바깥 리스트 내부에 있는 각 리스트들에 대한 반복문 1개

list_2 = [[0], [1,2], [3,4,5]]

list_2_len = len(list_2)
for y in range(len(list_2)):
    in_list = list_2[y]

    in_list_len = len(in_list)
    for x in range(len(in_list)):
        number = in_list[x]
        print(number)


list_3 = [[1,2,3],[4,5,6],[7,8,9]]
total = 0

for i in list_3:
    for j in i:
        total += j

print(total)

# 딕셔너리에 대한 반복문
# 리스트에 대한 반복문 -> 내부 원소에 대한 반복
# 딕셔너리에 대한 반복문 -> 내부 원소에 대한 반복
# 딕셔너리는 원소에 대한 key - value 2개의 데이터가 있다.

dict_1 = {
    "일":1,
    "이":2,
    "삼":3
}
# 딕셔너리의 반복문은 키(key)를 기준으로 반복한다.
for key in dict_1:
    # key 가 있기 때문에 value에 대한 인덱싱
    value = dict_1[key]
    print(key, value)

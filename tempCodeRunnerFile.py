class Book:
    # 생성자 매서드 작성
    def __init__(self,name, page_length):
        # Book 객체에 대한 속성(정보) 정의
        self.name = name # 책 이름
        self.page_length = page_length # 책의 페이지 수
        self.page_number = 0 # 현재 페이지 번호

        # 책을 1 페이지 넘기는 기능(매서드) 작성
    def turn(self):
        # 현재 페이지 번호가 책의 페이지 수와 같은지 검사하는 조건문
        if self.page_number != self.page_length:
            # 다르면 더 넘길 수 있다.
           self.page_number = self.page_number + 1

        print(f"현재 페이지 번호는 {self.page_number}.")

    def back(self):
        if self.page_number != 0:
            self.page_number = self.page_number -1
        print(f"현재 페이지 번호는 {self.page_number}.")



# Book 객체 생성하고, book_1 에 할당
# 이름은 파이썬 기본 도서, 페이지 수는 10 인 Book 객체 생성
book_1 = Book("파이썬 기본 도서", 10)
book_1.turn()
book_1.back()

# 책을 넘기는 (앞 / 뒤) 무한히 넘길 수 있을까?
# 챙의 페이지 수 초과해서 페이지 번호가 증가할 수 있을까?
# 페이지 번호가 0보다 작아질 수 있을까?

for _ in range(100):
    book_1.turn()

for _ in range(100):
    book_1.turn()    
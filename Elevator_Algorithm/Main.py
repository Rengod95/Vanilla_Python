import time

class list_to_col:
    def __init__(self):
        self.colist = [] #전체 엘리베이터 구조
        self.current_floor = None # 엘리베이터 현재 층
        self.total_floor = None # 총 층수
        self.user_floor = None # 사용자 층
        self.directed_floor = None # 사용자가 원하는 목적지 층
        self.moving_count = 0 # 움직이고 있는 지 아닌지 유무를 검사
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_floor < len(self.colist):
            CF = self.colist[self.current_floor]
            self.current_floor += 1
            return CF
        else:
            StopIteration

#엘리베이터 전체 상태 표시
    def display_all(self):
        print(f'현재 구조 : {self.colist}, \n 현재 층: {self.current_floor} \n, 총 층수 : {self.total_floor}\n 사용자 층 : {self.user_floor}\n, 목적지 층 : {self.directed_floor}\n,')

#유저가 있는 층 수 설정: get
    def set_user_floor(self, user_floor):
            if user_floor > 0 and user_floor <= 21: #층수 범위 1<n<21
                self.user_floor = user_floor-1
                print(f' 유저 층 : {self.user_floor+1}')

#엘리베이터 총 층수 설정: get 사용
    def set_total_floor(self, total_floor):
        if total_floor > 1 and total_floor < 21: #층수 범위 1<n<21
            self.total_floor = total_floor
            print(f' 총 층수 : {self.total_floor}')

#current floor 설정 함수
    def set_current_floor(self, current_floor):
        if current_floor <= int(len(self.colist)) and current_floor >= 1:
            self.current_floor = current_floor - 1 #입력값의 순서는 1부터 시작
            self.colist[self.current_floor] = '*'
            # * 중복 안되게


#엘리베이터 구조 설정 함수:
    def set_colist(self):
        if self.total_floor != None:
            for i in range(int(self.total_floor)):
                self.colist.append([])



#엘리베이터의 현재 층 표시

    def print_current_floor(self):
        print(self.colist)
        print(F'현재 층: {self.current_floor+1}')

#사용자와 엘리베이터의 층 수가 다를 때 사용자가 있는 곳으로 엘리베이터를 호출

    def call_elevator(self):
        self.difference = self.user_floor - 1 - self.current_floor
        if self.difference > 0:
            self.up(self.difference) #양수 일 때
        elif self.difference < 0:
            self.down(self.difference)


    def down(self, difference):
        if self.moving_count == 0:
            pass
        elif self.moving_count != 0:
            pass

    def up(self, difference):
        for i in range(difference):
            self.colist[self.current_floor] = []
            self.set_current_floor(self.current_floor+2)
            self.print_current_floor()
            time.sleep(1)



    def open(self):
        print('-문이 열립니다.-')
        for i in range(3):
            print('-대기 중-')
            time.sleep(1)

    def close(self):
        print('-문이 닫힙니다.-')
        for i in range(3):
            print('-닫는 중-')
            time.sleep(1)
        print('closed')



test_elevator = list_to_col() #변수에 elevator 클래스 객체 바인딩

while True:
    print('엘리베이터를 호출 하시겠습니까 yes/no 를 입력해주세요 :')
    call_true = str(input())
    if call_true == 'yes': #호출 시
        total_floor = int(input('엘리베이터의 총 수를 설정해주세요.(단 2층이상 20층이하) :'))
        test_elevator.set_total_floor(total_floor) #총 층수 설정
        test_elevator.set_colist() #리스트로 엘리베이터 구성 설정
        test_elevator.set_current_floor(1) #초기 엘리베이터 층은 1층으로 설정
        test_elevator.print_current_floor()

        test_elevator.open()
        test_elevator.close()
        test_elevator.up(5)



#호출 요청 -> cf, uf 확인 -> call_elevator
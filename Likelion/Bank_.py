class Node:
    def __init__(self,key,name,money):
        self.key = key
        self.name = name
        self.money = money

class Account:
    def __init__(self):
        self.accountList = []
        self.menuSelector()

    def status(self):
        print("=====Bank Menu=====\n1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 계좌이체\n6. 프로그램 종료\n==================")

    def create(self):
        newKey = int(input("계좌번호:"))
        if type(newKey) == type(1) and len(str(newKey))==13:
            newName = str(input('이름:'))
            newMoney = int(input("예금:"))
            if newMoney < 0:
                print('잘못 된 입력입니다.')
                return 0
            else:
                self.accountList.append(Node(newKey, newName, newMoney))

    def deposit(self):
        targetKey = int(input('입금하실 계좌 번호를 입력 해 주세요:'))
        if type(targetKey) == type(1) and len(str(targetKey))==13: #자료형태가 정수형이고 총 13자리 이면 검사 진행 (형식에 부합)
            for i in range(len(self.accountList)): #모든 accountlist의 원소에 대해 메모리 참조 떄문에 인덱스 i를 추출
                if self.accountList[i].key == targetKey: #입력 값이랑 기존 값이 같은 게 있다면
                    print(f'계좌이름: {self.accountList[i].name}\n 계좌잔고: {self.accountList[i].money}')
                    depos = int(input('입금하실 금액을 입력 해 주세요:'))
                    if depos < 0:
                        print('잘못 된 값 입니다.')
                        return 0
                    else:
                        self.accountList[i].money += depos
                        print(f"##계좌잔고 : {self.accountList[i].money}##")
                        print("## 입금이 완료되었습니다 ##")
                        return 0
                elif (i == len(self.accountList)-1):  ##i가 끝에 도달했다면
                    print('##잘못 된 게좌번호를 입력하셨습니다.##')  # 형식에 부합하지만 일치 값 없음

    def withDraw(self):
        targetKey = int(input('출금하실 계좌 번호를 입력 해 주세요:'))
        if type(targetKey) == type(1) and len(str(targetKey)) == 13:  # 자료형태가 정수형이고 총 13자리 이면 검사 진행 (형식에 부합)
            for i in range(len(self.accountList)):  # 모든 accountlist의 원소에 대해 메모리 참조 떄문에 인덱스 i를 추출
                if self.accountList[i].key == targetKey:  # 입력 값이랑 기존 값이 같은 게 있다면
                    print(f'계좌이름: {self.accountList[i].name}\n 계좌잔고: {self.accountList[i].money}')
                    depos = int(input('출금하실 금액을 입력 해 주세요:'))
                    if depos < 0:
                        print('잘못 된 값 입니다.')
                        return 0
                    else:
                        self.accountList[i].money -= depos
                        print(f"##계좌잔고 : {self.accountList[i].money}##")
                        print("##출금이 완료되었습니다##")
                        return 0
                elif (i == len(self.accountList) - 1):  ##i가 끝에 도달했다면
                    print('##잘못 된 게좌번호를 입력하셨습니다.##')  # 형식에 부합하지만 일치 값 없음

    def sendMoney(self):
        transfering = int(input('출금할 계좌번호 :'))
        transfered = int(input('이체할 계좌번호:'))
        ingIndex = None
        edIndex = None
        if len(str(transfered)) == 13 and len(str(transfering)) == 13:
            for node in range(len(self.accountList)):
                if transfering == self.accountList[node].key:
                    ingIndex = node
                if transfered == self.accountList[node].key:
                    edIndex = node
            if ingIndex == None or edIndex == None:
                print("출금 또는 이체의 계좌번호 값이 잘못 되었습니다.")
                return 0
            elif ingIndex == edIndex :
                print('출금 계좌와 이체 계좌는 동일할 수 없습니다.')
                return 0
            else:
                targetMoney = int(input('이체하실 금액을 입력 해 주세요:'))
                self.accountList[ingIndex] -= targetMoney
                self.accountList[edIndex] += targetMoney





    def checkAll(self):
        print("=====전체 조회=====")
        for node in self.accountList:
            print(f"계좌번호: {node.key} / 이름: {node.name} / 잔액 : {node.money} ")
        print("==============")

    def menuSelector(self):
        while True:
            self.status()
            getNum = int(input('입력: '))
            if getNum < 1 or getNum > 6:
                print('잘못된 입력 값 입니다.')
            elif getNum == 1:
                self.create()
            elif getNum == 2:
                self.deposit()
            elif getNum == 3:
                self.withDraw()
            elif getNum == 4:
                self.checkAll()
            elif getNum == 5:
                self.sendMoney()
            elif getNum == 6:
                exit(0)

test = Account()










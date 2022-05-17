import random
file_path = "/users/in/documents/git-in/food_list.txt"

with open(file_path) as food:
    lines = food.readlines()

food_list = [line.rstrip('\n') for line in lines]
recall_count = '0'
while True:

    if recall_count == '0':
        print('점심 고르는 프로그램 : 실행시키려면 1을 입력, 종료는 2를 입력하세요 :')
    else:
        print('실행은 1, 종료는 2를 입력하세요:')
    command_line_input = str(input())


    if command_line_input == '2':
        exit(0)
    elif command_line_input == '1':
        print(random.choice(food_list))
        print('원하시는 음식이 아닐 경우 3을 입력하시고, 종료를 원하시면 2를 입력하세요 :')
        recall_command = str(input())
        if recall_command == '3':
            recall_count = '1'
        elif recall_command == '2':
            exit(0)

    else:
        print('잘못된 입력입니다.')



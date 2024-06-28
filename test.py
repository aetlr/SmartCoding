import random 

random_number = random.randint(1, 100)

cnt = 0
while (True):
    try:
        cnt += 1
        user_ans = int(input("숫자를 입력하세요"))
        print(user_ans)
        if user_ans == random_number:
            print(f'정답입니다 {cnt}번 만에 맞췄습니다')
            break
        
        elif (user_ans > random_number):
            print('down')
        else:
            print('up')
    except:
        print('숫자를 입력하세요')
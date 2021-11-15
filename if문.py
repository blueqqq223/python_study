# name = 'Alice'
# if name == 'Alice':
#     print('반가워요, Alice.')
# print('종료')


# a, b = 10, 10
# if a > b:
#     print("조건이 참이면 실행")
#     print("실행 코드는 띄어쓰기로 구분")

# elif a == b:
#     print("a b가 같다")
# else:
#     print("if의 조건이 거짓일 때 실행")

#     print("종료")


# number = int(input("숫자를 입력: \n"))

# if (number % 2 == 0):
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")


height = int(input("키를 cm로 입력해 주세요: \n"))
if (height > 120):
    print("청룡열차를 탈 수 있습니다.")
    age = int(input("나이를 입력해 주세요: \n"))

    if age < 12:
        print("요금은 5000원 입니다.")
    elif age <= 18:
        print("요금은 7000원 입니다.")
    else:
        print("요금은 12000원 입니다.")
else:
    print("죄송하지만 탈 수 없습니다.")

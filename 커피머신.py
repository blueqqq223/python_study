# coffee = 10  # 커피 수량 10개

# while True:  # 무한 반복
#     print(f"남은 커피의 양은 {coffee}개 입니다.")
#     money = int(input("커피 한잔에 300원 입니다. 돈을 넣어 주세요 : "))
#     # 입금한 돈이 300원일때 더 클때, 작을 경우 처리 if elif else
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print(f"거스름돈 {money-300}를 주고 커피를 줍니다.")
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

# for n in [1, 2, 3]:
#     print(n)


# for s in ['땅다람쥐', '바다코끼리', '스컹크', '아나콘다', '코알라', '하이에나', '바다소']:
#     print(s)

# for c in '홍길동님':
#     print(c)

# for n in range(3):
#     print(n)

# total = 0
# for x in range(1, 101):
#     total += x

#     print("1에서 100까지 더한 값", total)

# for i in range(1, 10):
#     print(f'2 X {i} = {2*i}')

for i in range(2, 10):
    print()
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}', end="")

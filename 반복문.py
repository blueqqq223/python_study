# while True:
#     print("무한반복")

# count = 0
# while count < 3:
#     print('횟수: ', count)
#     count += 1


# name = ''
# while name != '펭수':
#     name = input('펭수를 입력해 주세요 : ')

# print("thank you")

hit = 0
while hit < 10:
    hit += 1
    if hit % 2 == 0:
        continue
    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 5:
        break

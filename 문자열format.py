# 1. f - string
name = '홍길동'
age = 20
print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

# 2. 문자열.format()
welcome = '환영합니다'
base = '{} 번 손님 {}'


name = '김펭수'
color = '핑크'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color}입니다.')

string1 = "abcdefg"
print(string1[2])
print(string1[1:5])
# 슬라이싱 [시작 : 끝], [ : : 증감]
print(string1[::-1])


string1[0] = 'k'

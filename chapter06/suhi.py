year = input('あなたの生まれた年を４桁で教えてください >> ')
month = input('あなたの生まれた月を教えてください >> ')
day = input('あなたの生まれた日付を教えてください >> ')

number = 0
for i in year:
    number += int(i)
for i in month:
    number += int(i)
for i in day:
    number += int(i)

while number >= 10:
    tmp = str(number)
    number = 0 #一旦クリアする
    for i in tmp:
        number += int(i)

print(f'あなたの運命数は{number}です')

#number = int(year[0]) + int(year[1]) + int(year[2]) + int(year[3])
#↑これと同じ
'''
number = int(year[0]) + int(year[1]) + int(year[2]) + int(year[3])
このintがないと、表示が2005の場合、"2005"となるためエラーになってしまう
'''
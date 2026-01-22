#1つめ
one = int(input('1つめの整数を入力してください >> '))
#2つめ
two = int(input('2つめの整数を入力してください >> '))
#和
print('和：', one + two)
#差
print('差：', one - two)
#積
print('積：', one * two)
#商
if two > 0:
    print('商：', one // two)
else:
    pass
#剰余
if two > 0:
    print('剰余：', one % two)
else:
    pass
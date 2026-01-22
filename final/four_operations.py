#数字以外だと繰り返すように
#chapter5/cardg.pyを参考に
while True:
#1つめ
    try:
        one = int(input('1つめの整数を入力してください >> '))
        break
    except ValueError:
        print('数字を入力してくださいね\n')
#１つ目が数字で２つ目が数字以外の場合に２つ目の質問を繰り返す
while True:
        #2つめ
    try:
        two = int(input('2つめの整数を入力してください >> '))
        break
    except ValueError:
        print('数字を入力してくださいね\n')
# 和
print('和：', one + two)
# 差
print('差：', one - two)
# 積
print('積：', one * two)
# 商
if two > 0:
    print('商：', one // two)
    print('剰余：', one % two)
else:
    pass
#pass文は何もしないとサイトに書かれてたので使用しました！
#終わり
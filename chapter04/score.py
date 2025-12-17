#名前
name = ['相沢いわし', '伊藤うずら', '上野えのき']

#格納するリスト
score = [0, 0, 0]


for i in range(3):
    score[i] = int(input(f'{name[i]}さんの点数を入力してください >> '))
    #print(f'{name[i]}さん: {score[i]}点')
    #print(f'{name[i]}さんの点数を入力してください。 >> ', end='')
    #score[i] += int(input())

#成績の表示
for i in range(3):
    print(f'{name[i]}さん: {score[i]}点')

#こんな書き方もあるよ
'''

number = 0
for i in name:
    score[number] = int(input(f'{i}さんの点数を入力してください >> '))
    number += 1
'''
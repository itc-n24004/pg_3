import random
'''
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(cards) #シャッフル前
random.shuffle(cards)
print(cards) #シャッフル後
'''

suit = ['スペード', 'ハート', 'ダイヤ', 'クラブ']

cards = []
for i in range(1, 53):
    cards.append(i)
print(cards)
random.shuffle(cards)
print(cards)

pick = int(input('何枚目のカードを引きますか？(1-52) >> '))
#引いたカードはcards[pick-1]になります

# スートを特定する
s = cards[pick - 1] // 13
print(s)
#ナンバーを特定する
number = cards[pick - 1] % 13
if number == 0:
    s -= 1
    number = 13

print(f'あなたが引いたのは{suit[s]}の{number}です')


"""
while True:
    try:
        pick = int(input('何枚目のカードを引きますか(1-52) >> '))
        if 1 <= pick <= 52:
            print(f'あなたが引いたのは{card[pick - 1]}です')
            break
        else:
            print('1-52の数字を入力してくだいね\n')
    except ValueError:
        print('数字を入力してくださいね\n')

"""
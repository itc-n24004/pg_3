import random

mark = ['♠', '♥', '♦', '♣']
number = ['A', '2', '3', '4', '5',
          '6', '7', '8', '9', '10',
          'J', 'Q', 'K']

card = []

for i in mark:
    for j in number:
        card.append(i + j)
print(card)
random.shuffle(card)
print(card)

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
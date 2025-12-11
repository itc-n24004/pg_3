# 数当てゲーム

import random
print('1から10までの数を当てましょう')
score = 5
game = 1
while True:
    print(f'数当てゲーム{game}回目')
    secret_number = random.randint(1, 10)
#10回聞く
    for guesses_taken in range(1, 11):

        guess = int(input('数を入力してください(0は終了) -> '))
        if guess == 0:
            break
        if guess < secret_number:
            print('あなたの推定値は小さいです。')
            score -= 1
        elif guess > secret_number:
            print('あなたの推定値は大きいです。')
            score -= 1
        else:
            print('正解！')
            score += 10
            game += 1 # 次のゲームに進む
            break #　当たり！
    if guess == 0:
        break
# 結果発表
    print(f'正解は{secret_number}でした。')
print(f'得点は{score}でした。')
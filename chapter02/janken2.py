import random

te = ['グー','チョキ','パー']
'''
te[0] -> グーになる
te[1] -> チョキになる
te[2] -> パーになる
'''
#勝ち負けあいこのカウント
wins = 0 #人間のスコア
loses = 0 #コンピュータのスコア
ties = 0

print('全部で10回勝負です。勝つのはどちらになるか…')

game_end = False

#ゲーム開始
for turn in range(1,11):#ゲームのループは10回
    print(f':::第{turn}回:::')
    if turn != 1:
        print(f'現在{wins}勝,{loses}敗,あいこ{ties}回です')
    print()

    while True: #入力のループ
        try:
            player_move = int(input('グー：0、チョキ：1、パー：2、ゲーム終了：3 -> '))
            if player_move == 3:
                print()
                print('ゲームを途中終了しますわ,勝ち分がマイナス1になりますわ')
                game_end = True
                wins -= 1
                break #ゲーム終了なので入力のループから抜ける
            if player_move >= 0 and player_move <= 2:
                break #勝ち負けの判定に行く
        except ValueError:
            print('0から3までの数字を入力してくださいな')
    if game_end:
        break


    #入力のループここまで
    # コンピュータは人間の手をあえて見ないようにして出す手を後出ししている
    computer_move = random.randint(0,2)
    print()
    print(f'コンピュータ：{te[computer_move]} あなた：{te[player_move]}')
    print()

    # 勝敗の判定
    judge=(player_move - computer_move + 3) % 3
    if judge == 0: #あいこ
        print('-----あいこです-----')
        ties += 1
    elif judge == 1: #負け
        print('-----あなたの負けです-----')
        loses += 1
    else: #勝ち
        print('-----あなたの勝ちです-----')
        wins += 1
    print()
'''
    if computer_move == player_move:
        print('あいこです')
        ties += 1
    else: # 勝ちか負けのパターン
        if computer_move == 0: # コンピュータがグーの場合
            print('コンピュータ：グー ', end='')
            if player_move == 1: # 人間はチョキ
                print('あなた：チョキ …あなたの負けです')
                loses += 1
            else: # 人間はパー
                print('あなた：パー …あなたの勝ちです')
                wins += 1
        elif computer_move == 1:# コンピュータがチョキの場合
            print('コンピュータ：チョキ ', end='')
            if player_move == 0: # 人間はグー
                print('あなた：グー …あなたの勝ちです')
                wins += 1
            else: #人間はパー
                print('あなた：パー …あなたの負けです')
                loses += 1
        else: # コンピュータがパーの場合
            print('コンピュータ：パー ', end='')
            if player_move == 0: # 人間はグー
                print('あなた：グー …あなたの負けです')
                loses += 1
            else: # 人間はチョキ
                print('あなた：チョキ …あなたの勝ちです')
                wins += 1
'''
#ゲームのループはここまで

#結果発表
print()
print('結果は -> ', end='')
print(f'{wins}勝{loses}敗{ties}分')
if wins > loses:
    print('おめでとうございます。あなたの勝利です!')
elif wins < loses:
    print('あなたの負けです。また挑戦してくださいな!')
else:
    print('同点ですね、いい勝負でした!')
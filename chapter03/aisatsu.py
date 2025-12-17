#あいさつする関数
def aisatsu(namae, jikantai):
    if jikantai == 1:
        print(f'{namae}さん、おはようございます')
    elif jikantai == 2:
        print(f'{namae}さん、こんにちは')
    elif jikantai == 3:
        print(f'{namae}さん、こんばんは')
    else:
        print(f'{namae}さん、おやすみなさい')
#↓↑は別のプログラムとしてみていい

#プログラム実行はここから
name = input('名前を入力してくだい >> ')
print('朝：1 昼：２ 晩：3 寝る前：４ ')
jikan = int(input('時間帯を入力してくだい >> '))
aisatsu(name, jikan)

'''
namae -> name
jikantai -> jikan
○番目が一緒のところが反映される
namaeは1番目のnameに、jikantaiは2番目のjikan
'''
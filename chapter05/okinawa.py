#辞書を設定する

okinawa = {'県花':'デイゴ', '県鳥':'ノグチゲラ',
           '県魚':'タカサゴ', '県のお菓子':'ミセスマーコの田芋パイ'}

#キーの一覧を表示
print(okinawa.keys())

#調べたいものを入力
search = input('調べたいものはなんですか？ >> ')

#キーに対するバリューを表示する
if search in okinawa.keys():
    print(okinawa[search])
else:
    print('そのデータはありません')
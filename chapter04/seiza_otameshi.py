seiza = ['山羊座', '水瓶座', '魚座', '牡羊座',
         '牡牛座', '双子座', '蟹座', '獅子座',
         '乙女座', '天秤座', '蠍座', '射手座']

#キーワード
keyword = ['"I keep..."(私は守る)',
               '"I solve..."(私は解明する)',
               '"I believe..."(私は信じる)',
               '"I exist..."(私は存在する)',
               '"I have..."(私は所有する)',
               '"I choose..."(私は選択する)',
           '"I sense..."（私は感じる)',
           '"I will..."(私は～する)',
           '"I analyze ..."（私は分析する)',
           '"I balance ..."（私はバランスをとる)',
           '"I want ..."(私は要求する)',
           '"I experience ..."(私は体験する)']


month = int(input('生まれた月はいつですか？ >> '))
day = int(input('生まれた日はいつですか？？ >> '))

#星座特定
#seiza = month #その月の星座として仮決定

changeday = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]

index = (month - 1 + (day >= changeday[month - 1])) % 12

print(f'あなたの星座は{seiza[index]}です')
print(f'キーワードは{keyword[index]}です')
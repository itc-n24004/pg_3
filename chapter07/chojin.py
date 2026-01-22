import re

text = input('あなたが知っている超人は？ >> ')

#ハイフン区切りの電話番号の場合
chojin_regex = re.compile(r'.*マン|.*[mM][aA][nN]')
mo = chojin_regex.search(text)
if mo.group() != None:
    print(f'超人{mo.group()}参上！')
else:
    print('そんなのいません')
import re

text = '明日098-862-5437に電話してください。オフィスは(098)-855-5437です'

#ハイフン区切りの電話番号の場合
phone_number_regex = re.compile(r'(\d{3}-\d{3}-\d{4})')
mo = phone_number_regex.search(text)
print(f'電話番号が見つかりました：{mo.group()}')


#市外局番号がカッコになっている場合
phone_number_regex = re.compile(r'(\(\d{3})\)-\d{3}-\d{4}')
mo = phone_number_regex.search(text)
print(f'電話番号が見つかりました：{mo.group()}')

#　※正規表現でマッチしたパターンが複数ある場合は最初のものだけ取得される

#mo = phone_number_regex.findall('明日098-862-5437に電話してください。オフィスは098-855-5437です')
#for n in mo:
#    print(f'電話番号が見つかりました：{'-'.join(n)}')

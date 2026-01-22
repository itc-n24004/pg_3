def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

message = '明日098-862-5437に電話してください。オフィスは098-855-5437です'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk) == True:
        print(f'電話番号が見つかりました：{chunk}')
print('完了。')
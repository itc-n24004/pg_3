name = input('名前を入力してください！ >> ')

while True:
    print('朝…1、昼…２、晩…３、寝る前…４')
    time = int(input('時間帯を入力してくだい >> '))

    if time == 1:
        print(f'{name}さん、おはようございます')
        break
    elif time == 2:
        print(f'{name}さん、こんにちは')
        break
    elif time == 3:
        print(f'{name}さん、こんばんは')
        break
    elif time == 4:
        print(f'{name}さん、おやすみなさい')
        break
    else:
        print(f'{name}さん、指定された数字を入力してください！\n')
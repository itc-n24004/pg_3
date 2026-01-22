import webbrowser
address = input("調べたい住所を入力してください>>")
webbrowser.open("https://www.google.com/maps/place/" + address)

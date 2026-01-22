for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print()
#print()があることによって、横一列が1*9が終わったあとの2の段みたいに分かれるようになる
#pythonのprint文は何も指定しなかったら、改行コードが松尾に追加されるみたい
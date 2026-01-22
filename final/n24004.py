#書き込みモードでオープン(中身は上書きされる)
write_file = open('n24004.txt', 'w')
write_file.write("出席番号：n24004\n")
write_file.close()

print('----------')
print('保存完了しました！')

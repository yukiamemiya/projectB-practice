f = open('pyramid.jpg','rb')
lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ
 
for line in lines2:
    print(line)
print(len(lines2))
# 簡単な足し算
# 入力例が　「1 1」　のようになるため
# input()を2回書くといったやり方は不可。
# そのためsplitメソッドを使う.
# splitは引数を指定しないと、空白文字を区切り文字とする

x, y = input().split()
print(int(x) + int(y))
# ch5_4.py
print("奇偶性")
num = input("input any number:")
rem = int(num) % 2
if (rem == 0):
    print("%d 是偶数" % int(num))
else:
    print("%d 是奇数" % int(num))
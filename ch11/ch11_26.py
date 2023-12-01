# ch11_26.py
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n + factorial(n-1))

value = 5
print("%s %s" % (value,factorial(value)))
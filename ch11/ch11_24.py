# ch11_24.py
def make_icecream(icecream_type, *toppings):
    print("this " + icecream_type + " icecream is made of:")
    for topping in toppings:
        print("--- " + topping)

make_icecream("1","a")
make_icecream("2","b","c","d")
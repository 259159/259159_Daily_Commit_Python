pizza = int(input("Enter the how many pizza slice you need "))

if pizza % 2 == 0:
    pizza_new = pizza * 120
else:
    pizza_new = pizza * 123
print("The Total cost of your pizza is %d\n" % pizza_new)

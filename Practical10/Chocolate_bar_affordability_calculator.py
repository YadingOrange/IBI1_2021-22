def number(total_money,price):
    number=int(total_money/price)
    return number

allmoney=float(input("total money:"))
chocolate_price=float(input("unit price:"))
chocolate_number=int(number(allmoney,chocolate_price))
change=(allmoney-chocolate_number*chocolate_price)
print("the number of chocolate is",chocolate_number)
print("the change is",change)

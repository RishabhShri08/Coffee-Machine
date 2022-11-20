from logo import logo

print(logo)

menu = """

Coffee Menu = Lette : $10,  Cappicino : $30,  Espresso : $50

"""

print(menu)

milk = [20]
coffee = [500]
sugar = [5]


def check():
    for i in milk:
        if i == 0:
            return True


def lette():
    for i in milk:
        for j in coffee:
            for k in sugar:


                pay = int(input(" pay $10 for Lattee coffee                : "))

                if pay == 10:
                    print(" Thanks for payment, Enjoy your Coffee ")
                    l_milk = i - 0.3
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.2
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.2
                    sugar.remove(k)
                    sugar.append(l_sugar)
                elif pay < 10:
                    print("Not sufficient payment")
                elif pay > 10:
                    refund = pay - 10
                    print(" Enjoy your coffee and please, collect your extra money : ", refund)
                    l_milk = i - 0.3
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.2
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.2
                    sugar.remove(k)
                    sugar.append(l_sugar)

            print(
                f" Remaining Ingrediants Status :  Milk  :  {milk}Litre  | Coffee  :  {coffee}gram  |  Sugar  :  {sugar}kg")


def cappicino():
    for i in milk:
        for j in coffee:
            for k in sugar:
                pay = int(input(" pay $30 for Cpicciono  coffee  : "))
                if pay == 30:
                    print(" Thanks for payment, Enjoy your Coffee ")

                    l_milk = i - 0.6
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.4
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.4
                    sugar.remove(k)
                    sugar.append(l_sugar)


                elif pay < 30:
                    print(" Payment Not Sufficient ")
                elif pay > 35:
                    refund = pay - 30
                    print(" Enjoy your coffee and please, collect your extra money : ", refund)
                    l_milk = i - 0.6
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.4
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.4
                    sugar.remove(k)
                    sugar.append(l_sugar)

                print(
                    f" Remaining Ingrediants Status : Milk  :  {milk}Litre  | Coffee  :  {coffee}gram  | Sugar  :  {sugar}kg")


def espresso():
    for i in milk:
        for j in coffee:
            for k in sugar:


                pay = int(input(" pay $50 for Espresso  coffee  : "))

                if pay == 50:
                    print(" Thanks for payment, Enjoy your Coffee ")
                    l_milk = i - 0.9
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.8
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.6
                    sugar.remove(k)
                    sugar.append(l_sugar)
                elif pay < 50:
                    print("Not sufficient payment")
                elif pay > 50:
                    refund = pay - 50
                    print(" Enjoy your coffee and please, collect your extra money : ", refund)
                    l_milk = i - 0.9
                    milk.remove(i)
                    milk.append(l_milk)

                    c_coffee = j - 0.8
                    coffee.remove(j)
                    coffee.append(c_coffee)

                    l_sugar = k - 0.6
                    sugar.remove(k)
                    sugar.append(l_sugar)

                print(f"Remaining Ingrediants Status :  Milk  :  {milk}Litre  | Coffee  :  {coffee}gram  |  Sugar  :  {sugar}kg")


flag = True
while flag:
    want = input(" Want Coffee ( yes for y and No for n) : ").lower()
    if want == "y":
        sign = check();
        if sign == True:
            print("No Ingrediants To make Coffee. Please refill it")
            break
        else:
            print(" Which Coffee You Want ")
            ask = input(" L for Latte, C for cappicino, E for Espresso :  ").lower()
            if ask == "l":
                lette();
            elif ask == "c":
                cappicino();
            elif ask == "e":
                espresso();
    elif want == "n":
        print(" Hope, You like my Service ")
        flag = False
    else:
        print(" Please enter valid input ")

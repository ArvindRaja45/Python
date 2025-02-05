#Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1
#Example Interaction
#Welcome to Python Pizza Deliveries!
#What size pizza do you want? S, M or L: L
#Do you want pepperoni on your pizza? Y or N: Y
#Do you want extra cheese? Y or N: N
#Your final bill is: $28.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
a = 15
b = 20
c = 25
if size == "S":
    if pepperoni == "Y":
        d = a+2
        if extra_cheese == "Y":
            e = d+1
            print(f"Your final bill is {e}")
        else:
            print(f"Your final bill is {d}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
           d = a+1
           print(f"Your final bill is {d}")
    else:
        print(f"Your final bill is {a}")
elif size == "M":
    if pepperoni == "Y":
        f = b+3
        if extra_cheese == "Y":
            g = f+1
            print(f"Your final bill is {g}")
        else:
            print(f"Your final bill is {f}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
           f = b+1
           print(f"Your final bill is {f}")
    else:
        print(f"Your final bill is {b}")
else:
    if pepperoni == "Y":
        h = c+3
        if extra_cheese == "Y":
            i = h+1
            print(f"Your final bill is {i}")
        else:
            print(f"Your final bill is {h}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
           h = c+1
           print(f"Your final bill is {h}")
    else:
        print(f"Your final bill is {c}")

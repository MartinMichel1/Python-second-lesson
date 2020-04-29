print("Hello random person. This program converts kilometers(km) to miles (mi).")
number_km = float(input("Write the number of kilometers you want to convert: "))
number_mi = number_km * 0.621

print(str(number_km) + "km is " + str(number_mi) + " miles")

positive = input("Would you like to convert again? (y/n)")

if positive == "y":

    while positive == "y":

        km_again = float(input("Write the number of kilometers you want to convert again: "))
        mi_again = km_again * 0.621
        print(str(km_again) + "km is " + str(mi_again) + " miles")
        positive = input("Would you like to convert again? (y/n)")
    else:
        print("OK, good bye")
else:
    print("OK, good bye")

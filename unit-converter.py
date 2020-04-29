print("Hello random person. This program converts kilometers(km) to miles (mi).")
while True:
    number_km = float(input("Write the number of kilometers you want to convert: "))
    number_mi = number_km * 0.621
    print(str(number_km) + "km is " + str(number_mi) + " miles")
    answer = input("Would you like to convert again? (y/n)")

    if answer == "y":
        continue
    else:
        print("Thank you and good bye.")
        break

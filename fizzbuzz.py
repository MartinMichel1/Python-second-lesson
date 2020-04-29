cNumber = int(input("Select a number betwen 1 and 100: "))
for i in range (1, cNumber + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)

import time
time.sleep(5)

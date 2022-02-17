
num = float(input("Put in weird decimal"))

if num % 1 == 0:
    print("{:.0f}".format(num))
else:
    print("{:.1f}".format(num))

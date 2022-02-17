
all_calculations = []

for item in range(0, 5):
    get_item = input("enter an item")
    all_calculations.append(get_item)

print()
print("*** The full list ***")
print(all_calculations)

print("*** Recent three ***")
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])

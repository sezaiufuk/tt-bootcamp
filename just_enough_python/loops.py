lst = [0, 1, 2, 3, 4, 5]

lst_hetero = [None, True, False, "Erwin", 3.14, 9]

lst_auto = list(range(6))

for element in lst:
    print(element)

for i, element in enumerate(lst_hetero):
    print(f"{i + 1}. element is {element}")


for i, (e1, e2) in enumerate(zip(lst, lst_hetero)):
    print(f"{i + 1}. {e1} and {e2}")

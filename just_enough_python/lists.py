lst = [1, 2, 3, 4, 5]

print("List initialized")
print(lst)

print(type(lst))

# Add a new element to the end
print("Append an element")
lst.append(6)

print(lst)

print("Append two more strings")
lst.append("Husnu")
lst.append("Sensoy")

print(lst)

print("Prepend an element")
lst.insert(0, -1)

print(lst)

print("Take a slice")
print(lst[2:4])


print("Pop the second one")
value = lst.pop(2)

print(lst)

lst.reverse()
lst.reverse()

reversed_lst = reversed(lst)

print(reversed_lst)

lst.pop(-1)
lst.pop(-1)
lst.reverse()


sorted_lst = sorted(lst)
# lst.sort()

print(lst)
print(sorted_lst)

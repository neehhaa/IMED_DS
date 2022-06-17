# To print even numbers and odd numbers from 1 to 10.

even_list = []
odd_list = []
for i in range(0, 11):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)

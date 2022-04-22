# To find prime numbers in a given user list using python.

num = int(input("Enter number of elements in the list : "))
num_list = []
prime_list = []
for i in range(0, num):
    elements = int(input("Enter elements : "))
    num_list.append(elements)
print("User-defined List : ", num_list)

for elements in num_list:
    for x in range(2, elements):
        if elements % x == 0:
            break
    else:
        prime_list.append(elements)
print("Prime List : ", prime_list)

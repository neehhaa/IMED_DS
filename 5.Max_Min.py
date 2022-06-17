# To find minimum and maximum numbers in a user given list.

num = int(input("Enter number of elements : "))
num_list = []
for i in range(0, num):
    elements = int(input("Enter elements : "))
    num_list.append(elements)
print("User-defined list : ", num_list)
print("Maximum Number in the list is : ", max(num_list))
print("Minimum Number in the list is : ", min(num_list))

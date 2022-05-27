"""
Pattern Printing
*
* *
* * *
* * * *
"""

num_rows = int(input("Enter the number of rows : "))

for row in range(1,num_rows+1):
    for column in range(row,0,-1):
        print("*",end=" ")
    print()


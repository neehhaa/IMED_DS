"""WAP to Print any 5 patterns.

(i)

* * * *
* * * 
* * 
*

"""

rows = int(input("Enter the number of rows : "))
for row in range(1, rows+1):
    for column in range(1, rows+1):
        rows = column-1
        print("*", end=' ')
    print()

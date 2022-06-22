"""

Write a program to Print any 5 patterns.

(ii) Equilateral Triangle

    *
   * *
  * * *
 * * * *
* * * * *

"""

rows = 5#int(input("Enter the number of rows : "))
rows = rows*2
for i in range(1, rows+1):
    if i % 2 == 1:
        for j in range(1, i+1, 2):

            print("*", end=" ")
    print()

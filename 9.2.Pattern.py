"""

Write a program to Print any 5 patterns.

(ii) Equilateral Triangle

    *
   * *
  * * *
 * * * *
* * * * *

"""

rows = 5  # int(input("Enter the number of rows : "))
rows = rows * 2
for row in range(1, rows + 1):
    for column in range(1, rows + 1):

        print("+", end=" ")
    print("")

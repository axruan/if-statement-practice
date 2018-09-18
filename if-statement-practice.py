# Alex Ruan
# 17 September 2018
# On my honor, I have neither given nor recieved unauthorized aid
# Sources:
# Ethan Chapman for helping with the y list that matched value to grade

import sys

x = float(sys.argv[1])
grade = ["F", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
value = [0, 1.5, 2, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85, 5]

if x >= 5 or x <= 0:
    print("Invalid input!")

y = [i for i in value if i <= x]

z = len(y) - 1

a = grade[z]

print(a)

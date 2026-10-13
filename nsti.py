# rectangle pattern

for i in range (1,5):
    for j in range (1,7):
        print ("*", end=" ")
    print()

# Increasing triangle

for i in range (1,8):
    for j in range (i):
        print("+",end=" ")
    print()

# Number Square

for num in range (1,5):
    for k in range (1,5):
        print(k,end=" ")
    print()

# multiplication tables

for num in range (2,11):
    print("Table of" ,num)
    for t in range(1,11):
        multiply = num*t
        print(num, "*",t,"=", multiply)

# Classroom seating

for c in range(1,6):
    for r in range(1,9):
        print("Seats",end=" ")
    print()

# prime number

for i in range(2,51):
    count=0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=" ")

# Pattern challenge

for i in range(1,6):
    print(" " * (5 - i), end=" ")
    print("* " * i)
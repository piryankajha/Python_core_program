# Python_Loops.py
"""
Topic: Loops in Python
Author: Piryanka Jha
"""

# ----------------------------
# What are Loops?
# ---------------------------
# Loops are used to execute a block of code repeatedly.
# Python supports two main types of loops:
# 1. for loop
# 2. while loop

# --------------------------
# for Loop
# ---------------------------
# Used to iterate over a sequence (like list, string, range, etc.)

print("Using for loop with range:")
for i in range(10):
    print("Value:", i)

print("\nUsing for loop with list:")
fruits = ["apple", "Orange", "Berry","Guava"]
for fruit in fruits:
    print(fruit)

# ---------------------------
# while Loop
# ---------------------------
# Executes as long as the condition is true

print("\nUsing while loop:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

'''___________________FOR_loop__________|🆚|_____________WHILE_loop______________________'''

#   ● Work with sequence or range.             ● work with condition
#   ● loop control is built-in like-           ● You must manually update condition
#     range(start,end,step)  
#   ● when you know how many times to repeat.  ● when you don't know how many times to repeat.

#   ● When you looping overime (fixed range).  ●  loop until a condition become false.


# ---------------------------
# break Statement
# ---------------------------
# Used to exit the loop prematurely

print("\nUsing break in a loop:")
for i in range(20):
    if i == 8:
        break
    print("Break Example:", i)

# ---------------------------
# continue Statement
# ---------------------------
# Skips the current iteration and moves to the next

print("\nUsing continue in a loop:")
for i in range(20):
    if i == 6:
        continue
    print("Continue Example:", i)

# ---------------------------
# Nested Loops
# ---------------------------
# Loops within loops

print("\nNested loop output:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

# ---------------------------
# else with Loops
# ---------------------------
# The else block executes after the loop ends normally (no break)

print("\nUsing else with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")




#__________________________________________________________________________________________________________________________
#-------------------------------------LOOP_QUESTIONS-----------------------------------------------------------------------


'''print 1 to 20 Sequence counting by for and while loop'''

for i in range(1,21):
    print(i)          
#------------------
x=1
while x<21:
    print(x)
    x+=1

'''Print "INDIA " 5 times by for and while loop '''
x=1
while x<=5:
    print("INDIA")
    x+=1
#----------------------
for i in range(1,6):
    print("INDIA")

'''print 20 to 30 Sequence counting by for and while loop'''
for i in range(20,31):
    print(i)

#--------
x=20
while x<=30:
    print(x)
    x+=1

'''backword counting 20 to 1 by while and for loop'''
x=20
while x>=1:
    print(x,end="|")
    x-=1

#-----------
for i in range(20,0,-1):
    print(i)

# print all even number 1 to 20 by for and while.
x=1
while x<=20:
    if x%2==0:
        print(x) 
    x+=1
#--------------------
for i in range(1,21):
    if i%2==0:
        print("Even no : ",i)

# print all Odd number 1 to 20 by for and while.
x=1
while x<=20:
    if x%2!=0:
        print(x) 
    x+=1
#-----------
for i in range(1,21):
    if i%2!=0:
        print("Odd no : ",i)

#to print all number which is divisible by 3 and 2

for i in range (10,41):
    if i%3==0 and i%2==0:
        print(i)



#count all even number from 10 to 25

c=0
for i in range (10,26):
    if i%2==0:
        c+=1
print(c)














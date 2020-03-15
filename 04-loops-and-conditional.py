'''
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/python_while_loops.asp




Test what you learnt
--------------------

1) write an example of if statement

2) write an example of if statement on one line

3) write an example of if else on one line


4) What would below print out?

a = 33
b = 200

if b > a:
	pass

5) What would below print out without a pass?

a = 33
b = 200

if b > a:

6) given following list below write a for loop that would print all values in the list

fruits = ["apple", "banana", "cherry"] 

7) where would you add a break statement to exit the loop when x is banana

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":

8) what values would below print out?

for x in range(2, 6):
  print(x)


9) below returns the values 1, 2, 4, 5, 6 why is 3 missing?

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
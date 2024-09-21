#COS2005 Python Programming
#Luke Snell
#Clara Riley
#09/20/24
#Program 2

#Prompt for age
age= int(input('Enter age:'))
#If person is greater than or equal to 1, display "infant."
if age <= 1:
    print('infant')
#If person is greater than 1 but less than 13, display "child."
elif age > 1 and age < 13:
    print('child')
#If person is greater than 12 but less than 20, display "teenager."
elif age > 13 and age < 20:
    print('teenager')
#If person is greater than 20 but less than 125, display "adult."
elif age >= 20 and age < 125:
    print('adult')
#If other, display "You are Dead."
else:
    print('You are dead.')

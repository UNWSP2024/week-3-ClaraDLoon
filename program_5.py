#COS2005 Python Programming
#Luke Snell
#Clara Riley
#09/20/24
#Program 5

print('Would you like a Hot dog or a Chilie dog?')
answer = (input('Enter choice:'))
if answer == ('Hot dog'):
    amount1 = 3.50
elif answer == ('Chili dog'):
    amount1 = 4.50
else:
    print('We do not sell that here.')
    amount1 = 0

print('Would you like cheese?')
answer2 = (input('Enter choice:'))
if answer2 == ('Yes'):
    amount2 = 0.50
elif answer2 == ('No'):
    amount2 = 0
else:
    print('Wrong answer.')
    amount2 = 0


print('Would you like peppers?')
answer3 = (input('Enter choice:'))
if answer3 == ('Yes'):
    amount3 = 0.75
elif answer3 == ('No'):
    amount3 = 0
else:
    print('Wrong answer.')
    amount3 = 0

print('Would you like grilled onions?')
answer4 = (input('Enter choice:'))
if answer4 == ('Yes'):
    amount4 = 1.00
elif answer4 == ('No'):
    amount4 = 0
else:
    print('Wrong answer.')
    amount4 = 0

sub_total = (amount1 + amount2 + amount3 + amount4)
sales_tax = (sub_total * 0.07)
total = (sub_total + sales_tax)

print('Subtotal: $', sub_total)
print('Salestax: $', sales_tax)
print('Total: $', total)

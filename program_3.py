#COS2005 Python Programming
#Luke Snell
#Clara Riley
#09/20/24
#Program 3

weight = float(input("Enter wight:"))
if weight <= 2:
    print("Your total is $",weight*1.50, "for your package.")
elif weight > 2 and weight <= 6:
    print("Your total is $",weight*3.00, "for your package.")
elif weight > 7 and weight <= 10:
    print("Your total is $",weight*4.00, "for your package.")
elif weight > 10:
    print("Your total is $",weight*4.75, "for your package.")

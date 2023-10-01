#Write a program that converts 400oK 
# to Celsius and displays the formatted result.

degreeK = 400

funcKtoC = degreeK - 273

print(f"{degreeK:d} Kelvin equals to {funcKtoC} Celcius")


"""
Write a program that finds the sum of the 
first and last digit of some 4-digit number.
"""
a = input("give me a 4-digit number:" )
print(a)

b,c = a[0],a[-1]

summ = int(b) + int(c)
print(f"sum of the first and last digit of the number {summ:d}")


"""Write a program to calculate the number of hours 
and minutes needed for a car to travel 500 kilometers 
at the velocity 110 km/h."""

km = 500
velocity = 110
cal_hour = 500/110
print(f"cal hour : {cal_hour:.2}" )
print("minutes=",  cal_hour*60)
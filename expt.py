number = int(input ("Enter a number: "))
thousandth_digit = number//1000
non_zero_thousand = thousandth_digit % 10 != 0
#tell user whether thousandth digit number is non zero 
print("Is the thousandth place digit a non zero? ", non_zero_thousand)

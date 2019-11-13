pay = float(input("Hourly pay rate - "))
worked = int(input("Hours worked - "))

taxformula = (pay * worked) * 0.22
tax = (pay * worked)
a = str(tax - taxformula)

print("Your pay after taxes is", "$" + a)

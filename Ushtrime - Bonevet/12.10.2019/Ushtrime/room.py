width = int(input("Width - "))
length = int(input("Length - "))
price = float(input("Price - "))

sfeet = float(width * length)
fomula = str(float(sfeet * price))

print("Your room is", sfeet, "square feet.")
print("The total cost of carpeting your room will be", "$" + fomula)
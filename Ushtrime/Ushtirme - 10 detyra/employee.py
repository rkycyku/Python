monthb = input("Month born - ")
yearb = int(input("Year born - "))
months = input("Month start - ")
years = int(input("Start year - "))

med = str(years + 1)
ret = str(years + 5)
pension = str(yearb + 65)

print("You are eligible for medical insurance in", months, "of", med)
print("You will be in retirement plan in", months, "of", ret)
print("You can start collecting your pension in", monthb, "of", pension)
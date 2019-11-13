bpfp = int(input("Base Pice for Pizza - "))
coupon = int(input("Coupon - "))
stax = int(input("Sales Tax - "))



if coupon == 0:
    a = (bpfp * 0)
    b = (bpfp - a)
    c = (stax * 0.01)
    d = (b * c)
    e = (b + d)
    f = str(e)
    print("The total is", "$" + f,".")
    print("Enjoy your pizza!") 
elif coupon == 5:
    a = (bpfp * 0.5)
    c = (stax * 0.01)
    d = (b * c)
    e = (b + d)
    f = str(e)
    print("The total is", "$" + f,".")
    print("Enjoy your pizza!") 
elif coupon == 10:
    a = (bpfp * 0.1)
    b = (bpfp - a)
    c = (stax * 0.01)
    d = (b * c)
    e = (b + d)
    f = str(e)
    print("The total is", "$" + f + ".")
    print("Enjoy your pizza!") 
elif coupon == 15:
    a = (bpfp * 0.15)
    b = (bpfp - a)
    c = (stax * 0.01)
    d = (b * c)
    e = (b + d)
    f = str(e)
    print("The total is", "$" + f,".")
    print("Enjoy your pizza!") 

    
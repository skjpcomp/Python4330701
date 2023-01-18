P=float(input("Enter principal amount:"))
R=float(input("Enter rate of interest:"))
T=float(input("Enter time period:"))
simple=(P*R*T)/100
Compound=P*(1+R/100)**T-1
print("Simple Interest:{}".format(simple))
print("Compound Interest:{}".format(Compound))
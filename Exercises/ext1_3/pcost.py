

with open("../../Data/portfolio.dat","r") as f:
    sum=0
    for line in f:
        details=line.split()
        qty=float(details[1])
        price=float(details[2])
        sum+=qty*price

print(sum)

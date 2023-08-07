

def portfolio_cost(filename):
        #try:
    
            with open(filename,"r") as f:
                sum=0
                for line in f:
                    details=line.split()
                    qty=0
                    try:
                        qty=float(details[1])
                    except ValueError:
                        print(f"Incorrect qty in line: {line}")

                    price=0
                    try:
                        price=float(details[2])
                    except ValueError:
                         print(f"Incorrect price in line: {line}")
                    sum+=qty*price

            print(sum)
        #except:
        #     print("Error")
    
if __name__ == '__main__':
    portfolio_cost('../../Data/portfolio3.dat')
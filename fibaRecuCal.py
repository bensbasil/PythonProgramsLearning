fseries=[0,1]
def fib():
    num=int(input("Enter the number of terms:"))
    if num<=0:
        print("Please enter a positive integer")
    elif num==1 or num==2:
        print(fseries[0:num])
    elif num>2:
        for i in range(2,num):
            nextterm=fseries[i-1]+fseries[i-2]
            fseries.append(nextterm)
        print(fseries)
if __name__=="__main__":
    fib()
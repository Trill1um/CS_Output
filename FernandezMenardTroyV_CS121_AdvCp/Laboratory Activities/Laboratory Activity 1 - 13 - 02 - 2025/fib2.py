num=int(input("Enter the number of terms: "))

test=[0, 1]
if num==0:
    print()
elif num==1:
    print(test[num-1])
elif num==2:
    print(test)
elif num>len(test):
    while not len(test)==num:
        test.append(test[-1]+test[-2])
    print(f"Fibonacci Series: ",end="")
    for i in test:
        print(i,end=" ")
else:
    print("Enter valid number!!!")

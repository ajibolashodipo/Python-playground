num= int(input("enter a number: "))
l=[num]
def collatz(num):
    # lb.append(num)
    last= l[-1]
    while last is not 1:

        if last %2 ==0:
            new= last//2
            l.append(new)
        else:
            new= last*3 +1
            l.append
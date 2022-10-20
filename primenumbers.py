v= int(input("enter the value of the number:"))

def primenumberss(x):

    for v in range(2, x-1):
        if x % v == 0:
          print(False)
    else: x == 0
    print(True)


print(primenumberss(1))
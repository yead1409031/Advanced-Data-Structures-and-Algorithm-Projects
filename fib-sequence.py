from hashMap import HashMap

temp = HashMap()

def fib(n,temp):
    if n in temp:
        return temp[n]
    
    if n==0 or n==1:
        return n
    
    result= fib(n-1, temp) + fib(n-2, temp)
    temp[n]=result
    return result

def fib_sequence(n):
    for i in range(n):
        yield fib(i,temp)

if __name__=='__main__':
    n=int(input("Enter the number: ", ))
    for j in fib_sequence(n):
        print(j)
def main():
    print("The nth item is: ", fib(6, temp))

main()


    

    

    





from hashMap import HashMap

f = HashMap()

def fib(n):
    # if already calculated for n, then retrieve result from HashMap and return it
    if n in f:
        return f[n]

    # if calculating for 0, then record result to HahsMap and return result
    if n == 0 or n == 1:
        f[n] = n
        return n

    # if calculating for != 0, 1, value that is alredy in HashMap, then
    elif n > 1:
        value = fib(n-1) + fib(n-2)
        f[n] = value
        return value
    # calculate value according to Fib formula, record the result to HashMap
    # and return the result

def main():
    print(fib(100))

main()
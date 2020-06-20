def fun_or(x,y):
    # print(bin(x), bin(y), bin(x | y), sep="\n") 
    # print(x|y, sep="\n") 
    return bin(x | y)

def fun_and(x,y):
    # print(bin(x), bin(y), bin(x & y), sep="\n") 
    return bin(x & y)

def fun_xor(x,y):
    # print(bin(x), bin(y), bin(x ^ y), sep="\n") 
    return bin(x ^ y)

def fun_not(x):
    return bin(~x)

def fun_shiftr(x,n):
    print(x,'---',bin(x),'---',x>>n,'---',bin(x>>n))
    return bin(x>>n)
fun_shiftr(234,2)

def fun_shiftl(x,n):
    print(x,'---',bin(x),'---',x>>n,'---',bin(x<<n))
    return bin(x<<n)
fun_shiftl(58,2)

def fun_rotr(x,n):
    rt= x>>n
    rt1= x<<len(bin(x))-n
    res= rt|rt1
    return bin(res)

def fun_rotl(x,n):
    rt= x<<n
    rt1= x>>len(bin(x))-n
    res= rt|rt1
    return bin(res)



def sig0(x):
    return 


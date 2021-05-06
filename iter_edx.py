def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


iterPower(3, 4)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 0
    if exp <= 0:
        return 1

    return base * recurPower(base, exp - 1)


def gcdIter(a, b):
    if a > b:
        t = a
        a = b
        b = t

    t = a
    while t > 1:
        if b % t == 0 and a % t == 0:
            return t

        t = t - 1


gcdIter(82, 64)

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(0))

def isPalindrome(s):
    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstwxyz'
                    ans = ans+c
        return ans

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0] ==s[-1] and isPal(s[1:-1])
        return isPal(toChars(s))
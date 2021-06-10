import timeit as tm
import math as m

def factor_a(x):
    n = x
    #print("n = {}".format(n))
    factored = True
    while factored:
        if n == 2 or n == 3:
            factored = False
            break
            
        if n % 2 == 0:
            n = n // 2
            print(2)
            factored = True
            continue
            
        if n % 3 == 0:
            n = n // 3
            print(3)
            factored = True
            continue
            
        if n < 8:
            factored = False
            break
        
        lim = m.floor(m.sqrt(n)) + 10
            
        for i in range(6, lim, 6):
            #print("{} mod {} = {}".format(n, (i-1), n % (i-1)))
            #print("{} mod {} = {}".format(n, (i+1), n % (i+1)))
            if n % (i - 1) == 0 and n != (i - 1):
                #print("OK! i-1")
                n = n // (i - 1)
                print(i - 1)
                factored = True
                break
            elif n % (i + 1) == 0 and n != (i + 1):
                #print("OK! i+1")
                n = n // (i + 1)
                print(i + 1)
                factored = True
                break
            else:
                #print("ok")
                factored = False
                
            #print(i)
        #print("N: {}".format(n))
        #print("Factored?: {}".format(factored))
        #print("Next")
                
    print(n)
    #print("---")
    
def factor_b(x):
    prime = True
    lim = m.floor(m.sqrt(x))+10
    for i in range(2, lim):
        if x%i == 0:
            print(i)
            x = x // i
            prime = False
            break
    if not prime:
        factor_b(x)
    else:
        print(x)
        
def test():
    #tests = [722427373245979, 17275381274295433, 790857608753147]
    tests = [6469693230, 31996938545466404601, 790857608753147, 2090862748777986991]
    funcs = [
        ("Fast factorization", "factor_a"),
        ("Slow factorization","factor_b")
    ]
    iter = 1
    for t in tests:
        print("---")
        print("Test: {}".format(t))
        print("Iterations: {}\n".format(iter))
        for f in funcs:
            print(f[0])
            #print(eval("{}({})".format(f[1], t)))
            tim = tm.timeit(
                "{}({})".format(f[1], t),
                "from __main__ import {}".format(f[1]),
                number = iter
            )
            print("{} time: {:.6f}\n".format(f[1], tim))


test()
          
"""
factor(624) # 2^4 * 3 * 13
factor(72) # 2^3 * 3^2
factor(720) # 2^4 * 3^2 * 5
factor(627) # 3 * 11 * 19
factor(210) # 2 * 3 * 5 * 7
factor(1729) # 7 * 13 * 19
factor(160239) # 3 * 31 * 1723
factor(30)
factor(49)
factor(16) # 2^3
factor(2090862748777986991) # 1137182693 * 1838633987
factor(722427373245979) # 15099943 * 47843053
factor(17275381274295433) # 134922397 * 128039389
factor(790857608753147) # 13 * 61561 * 988210079
factor(6469693230) # 29 * 23 * 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
factor(31996938545466404601) # 7  * 13 * 41 * 103 * 3 * 24181 * 20849 * 55051
"""
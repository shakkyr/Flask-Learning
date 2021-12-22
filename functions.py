def printStr(str):
    print(str)
    return


printStr('shadi')

# =========================


def sumNums(a, b):
    print(a+b)


sumNums(5, 10)

# =========================


def prinMe(arg, *vartuple):  # the *vartuple is like a container
    print('output')
    print(vartuple)
    print(arg)
    for var in vartuple:
        print(var)


# the first arg will go into arg above and all the other arguments will go iside vartuple
prinMe(10, 20, 30, 40, 50, 60, 70)


# ========== anonimus function ===========
def summ(x, y):
    print("------- summ ---------")
    print(x+y)


summ(10, 20)


def summ1(x, y): return x+y


print(summ1(32, 40))


# ============= local global ===============
f = 0
print(f)


def testt():
    f = 5  # this f is defined localy in the function only
    print(f)


testt()
print(f)
# ==========================================
f = 0
print(f)


def testt():
    global f  # this f is defined globaly
    f = 5
    print(f)


testt()
print(f)


# ============sliccing============
print('==========slice======')
x = 'shadi rada'
print(x[0])  # s
print(x[4])  # i
print(x[8])  # d
print(x[5])  # space
print(x[0:4])  # shad
print(x[0:])  # shadi rada
print(x * 2)  # shadi radashadi rada
print(x + x)  # shadi radashadi rada


# ============ dot format============
print('==========dot format======')

print('my name is {} and my age is {}'.format('shadi', 34))


# ============ lists ==================='
print('==========Lists======')

list1 = ['shadi', 1987, 2 ,'aws']

list1.insert(4,'rada')
print(list1)

list1.append('family') # adds to the end of the list
print(list1)
print(list1.count('family'))  # counts the element repeting
print(list1.pop())  # delets the last element
list1.reverse() # reverse the order

# ============ dictionary ==================='
print('==========dictionary======')

s = {1:'shadi', 2:'mays', 3:'aws'}
print(s[1])

s[5] = 'maysshadi'
print(len(s))
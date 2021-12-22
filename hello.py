msg = "hellow shadi"
print(msg)

print(list(range(0,10,2)))

# ===========================
for i in "shadi":
    if i =="i":
        break
    print('current letter:' , i)


    # =========================
var = 10
while var > 0:
    print('sss',var)
    var -= 1

print('number             square')
print('-------------------------')
for i in range(1,11):
    square = i **2
    print(i ,'\t\t    ' , square)



## \n new line
## \t tab = 4 spaces


# =================================
# start = input('enter a start number :') # input takes a str class
start = int(input('enter a start number :'))#int transfers the str to int
end = int(input('enter the end number :'))

print('number             square')
print('-------------------------')
for i in range(start, (end+1)): #will thro error it should take just int
    square = i **2
    print(i ,'\t\t    ' , square)





# ================================
rows = int(input('how many rows :'))
cols = int(input('how many cols :'))

for r in range(rows):
    for c in range(cols):
        print('*' , end='') # the end tells the print to not jump into new line
    print()                 # the empty print tells to jump to empty new line



# ========================
size = 8

for r in range(8):
    for c in range(r+122):
        print('*', end='')

    print()
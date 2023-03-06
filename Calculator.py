n = int(input("Enter number of element to insert:"))

l = []
for i in range(n):
    e = int(input("insert the element:"))
    l.append(e)
print(l)    

def add(l):
    s = 0
    for i in range (len(l)):
        s = s + l[i]
    return s    

def max_(l):
    m = [l[0]]
    for i in range(len(l)):
        if l[i] > m[0]:
            m = l[i]
    return m        

def min_(l):
    m = [l[0]]
    for i in range(len(l)):
        if l[i] < m[0]:
           m = l[i]
    return m  

def len_(l):
    c = 0
    for i in range(len(l)):
        if l != 0:
            c = c +1
    return c        

def avg(l):
    s = add(l)
    l = len_(l)
    avg = s / l
    
    return avg
    
print("1.add, 2. Max, 3. Min, 4. Length, 5. Average")
option = int(input("Enter the valid choices:"))

if option == 1:
    a = add(l)
    print(a)
    
if option == 2:
    m = max_(l)
    print(m)

if option == 3:
    mi= min_(l)
    print(mi)

if option == 4:
    l = len_(l)
    print(l)
    
if option == 5:
   av= avg(l)
   print(av)
   
else:
    print("Enter the valid option")






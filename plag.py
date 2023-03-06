f1 = open('C:/Users/ADMIN/OneDrive/Desktop/navikenz/text1.txt', 'w+')
f1.write(" Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.")
f1.seek(0)
file1_contents = f1.read()
print(file1_contents)
f1.close()

f2 = open('C:/Users/ADMIN/OneDrive/Desktop/navikenz/text2.txt', 'w+')
#2.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.")
f2.write('''Python programming language is one of dynamic and object-oriented programming languages 
         used for the development of diverse kinds of software developed by the Python Software foundation. 
        Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.''')
f2.seek(0)
file2_contents = f2.read()
print(file2_contents)
f2.close()


def count(str):
    counts = dict()
    words = str.lower().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

d1 = count(file1_contents)
d2 = count(file2_contents)

total = 0
for i,j in d1.items():
    for x,y in d2.items():
        if i == x:
            total = total + min(j,y)
print(total) 

d1_t = 0
for i,j in d1.items():
    d1_t = d1_t + j

d2_t = 0
for i,j in d2.items():
    d2_t = d2_t + j

plag = total / max(d1_t,d2_t)

print(plag * 100) 





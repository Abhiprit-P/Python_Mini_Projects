x=input("Enter first name:")
y=input("Enter second name:")

x=list(x) 
y=list(y)
for i in x[:]:
    if i in y:
        x.remove(i) 
        y.remove(i)
        
count=len(x)+len(y)
print(count)

result = ["friends", "love", "affection", "marriage", "enemy", "siblings"] 

while len(result) > 1 : 
	s = (count % len(result) - 1) 
	if (s>=0) :
		right = result[s + 1 : ]
		left = result[ : s] 
		result = right + left
	else : 
		result = result[ : len(result) - 1] 
print(result)
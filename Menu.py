menu = {"tea": 10, "coffee": 20,"cold drink": 40,"sandwich": 50,"pie": 60}
print(menu)
d = {}

name=input("Enter the order name: ") 
quantity=int(input("Number of Quantity: ") )
d[name]=quantity 

print(d)   

def order(d):
        name=input("Enter the order name: ") 
        quantity=int(input("Number of Quantity: ") )
        d[name]=quantity

     
def remove(d):
    r = input("Enter item to remove")
    if r in d:
        d.pop(r)
    print(d)   
        
    
def modify(d):
    m = input("Modify Quanty of items:")
    n = int(input("New quantity"))
    if m in d:
        d[m]=d.get(m) + n
    print(d)    


def bill():
    total = []
    for i in d.keys():
        if i in menu.keys():
             s = d[i] * menu[i]
             total.append(s)
             
    print("Total bill:" , sum(total))         


for i in menu:
    ask = int(input("1.add, 2. remove, 3.modify the quantity, 4. confirm/bill"))
    
    if ask == 1:
        order(d)
    if ask ==2:
        remove(d)   
    if ask ==3:
        modify(d) 

    print(d)   
        
    p = input("Done y or n:")
    if p == "y":
        bill()
        break 









        

    

      

# Online Python - IDE, Editor, Compiler, Interpreter
X = str(input("enter any sentence : "))
vow="A,E,I,O,U,a,e,i,o,u"
countC=0
countV=0
countW=1
for char in X:
    if char in vow:
        countV+=1
    elif char in " ":
        countW+=1
    else:
        countC+=1
print("number of vowels",countV)
print("number of constants",countC)
print("number of words",countW)
        
        
    




# Online Python - IDE, Editor, Compiler, Interpreter
N = int(input("enter the number :"))
X = int(input("x :"))
sum = 1
a = 1
for i in range(1, N + 1):
    sum += (X**a/a)
    a += 1
b = round(sum,9)
print(b)
        
    



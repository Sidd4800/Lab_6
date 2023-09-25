
# Online Python - IDE, Editor, Compiler, Interpreter
N = int(input("enter the number :"))
sum = 0
a = 1
fac = 1
for a in range(1, N + 1):
    fac *= a
    sum += 1 / fac
    a += 1
b = round(sum,9)
print(b)
        
    



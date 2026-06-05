"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n -1)
    
n=int(input("ingresa el numero "))
print(factorial(n))
"""
"""
def fibonachi(n):
    if n == 0 or n== 1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)

print(fibonachi(5))
"""
"""
def digitos(n):
    suma=0
    if n==0:
        return 0
    else:
        return n%10 +  digitos(n//10)

print(digitos(1234))
"""
"""
dic={}
num=[1,1,1,3]
for i in range(len(num)):
    if num[i] not in dic:
        dic[num[i]]=1
    else:
        dic[num[i]]+=1

print(dic)
"""
"""
dic={}
num=[3,2,3,5,3,1,1,3]
def numeros(mayor):
    if len(num)==0:
        return dic,mayor
    else:
        if num[0] not in dic:
            dic[num[0]]=1
        else:
            dic[num[0]]+=1
        if num[0]>mayor:
            mayor=num[0]
        num.pop(0)
        return numeros(mayor)
    
dic_2={}
def ordenar(dic,mayor,i):
    if i==mayor+1:
        return dic_2
    else:
        if i in dic:
            dic_2[i]=dic[i]
        else:
            dic_2[i]=0

        i+=1
        return ordenar(dic,mayor,i)

dic, mayor=numeros(num[0])
print(ordenar(dic,mayor,1))
"""

def palindromos(palabra):
    if palabra=="":
        return True
    else:
        if palabra[0]==palabra[-1]:
            palabra=palabra[1:]
            palabra=palabra[:-1]
            return palindromos(palabra)
        else:
            return False
        
print(palindromos("agua"))
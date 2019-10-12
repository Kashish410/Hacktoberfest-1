
#https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
w = int(input())
n = int(input())
l=[]
for i in range (0,x+1):
    for j in range (0,y+1):
        for k in range (0,z+1):
            for m in range (0, w+1):
            if i + j + k + m != n:
                l1=[i,j,k,m]
                l.append(l1)
print(l)                


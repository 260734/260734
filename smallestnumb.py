# program to find second smallest number in a list
m=[]
x=int(input())
for i in range(x):
    a=int(input())
    m.append(a)
print("List")
print(m)
m.sort(reverse=True)
print("Second largest number", m[1])
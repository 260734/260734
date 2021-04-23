# program to find maximum and minimum value in a set.
h=set()
f=int(input("Enter the number of elements"))
for i in range(f):
    p=int(input())
    h.add(p)
print("Maximum element in set", max(h))
print("Minimum element in set", min(h))
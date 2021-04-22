#return the number of times it appears in the tuple.
t = (2, 5, 5, 6, 5, 3, 4, 4, 8, 10, 5, 2)
print()
count = t.count(5)
print(count)

#convert a list of tuples into a dictionary
l1=[("Kunal", 21), ("Sarthak", 45), ("dipro", 22),
        ("shubham", 88), ("tushar", 46), ("Suraj", 28)]
d1=dict()

for student,score in l1:
    d1.setdefault(student, []).append(score)
print(d1)
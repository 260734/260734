# Python script to merge two Python dictionaries
s1 = {'qw': 45, 'er': 67}
s2 = {'as': 23, 'df': 87}
d = s1.copy()
d.update(s2)
print(d)
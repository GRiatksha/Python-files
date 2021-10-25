class student:
    def __init__(myself, m1, m2):
        myself.m1 = m1
        myself.m2 = m2

    def sum(myself, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        return s

a1=student(50, 60)
print(a1.sum())
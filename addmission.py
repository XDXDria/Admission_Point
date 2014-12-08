lis = []
pass_faculty = input()
gpa = lis.append(raw_input())
thai = lis.append(raw_input())
social = lis.append(raw_input())
eng = lis.append(raw_input())
math = lis.append(raw_input())
science = lis.append(raw_input())
physical = lis.append(raw_input())
art = lis.append(raw_input())
work = lis.append(raw_input())
gat = lis.append(raw_input())
pat1 = lis.append(raw_input())
pat2 = lis.append(raw_input())
pat3 = lis.append(raw_input())
pat4 = lis.append(raw_input())
pat5 = lis.append(raw_input())
pat6 = lis.append(raw_input())
pat7 = lis.append(raw_input())
print lis
nlis = []
for i in lis:
    if i == '-':
        i = float(0)
        nlis.append(i)
    else:
       i = float(i)
       nlis.append(i)
print nlis

gpa = nlis[0]*1500
thai = nlis[1]*15
social = nlis[2]*15
eng = nlis[3]*15
math = nlis[4]*15
science = nlis[5]*15
physical = nlis[6]*5
art = nlis[7]*5
work = nlis[8]*5

if pass_faculty >= 2024 and pass_faculty <= 2042:
    gat = nlis[9]*15
    pat2 = nlis[11]*15
    pat3 = nlis[12]*20
elif pass_faculty == 2043:
    gat = nlis[9]*30
    pat7 = nlis[16]*20
elif pass_faculty == 2044:
    gat = nlis[9]*50
elif pass_faculty == 2045:
    gat = nlis[9]*10
    pat3 = nlis[12]*20
    pat5 = nlis[14]*20
elif pass_faculty >= 2046 and pass_faculty <= 2048:
    gat = nlis[9]*10
    pat4 = nlis[13]*20
    pat5 = nlis[14]*20
elif pass_faculty == 2049:
    gat = nlis[9]*10
    pat2 = nlis[11]*20
    pat5 = nlis[14]*20
elif pass_faculty >= 2050 and pass_faculty <= 2067:
    gat = nlis[9]*10
    pat1 = nlis[10]*10
    pat2 = nlis[11]*30
elif pass_faculty == 2068:
    gat = nlis[9]*15
    pat2 = nlis[11]*15
    pat3 = nlis[12]*20
elif pass_faculty >= 2069 and pass_faculty <= 2071:
    gat = nlis[9]*30
    pat1 = nlis[10]*20
elif pass_faculty >= 2072 and pass_faculty <= 2074:
    gat = nlis[9]*10
    pat1 = nlis[10]*10
    pat2 = nlis[11]*30
elif pass_faculty >= 2075 and pass_faculty <= 2076:
    gat = nlis[9]*15
    pat2 = nlis[11]*15
    pat3 = nlis[12]*20
    
print gpa,gat,pat2,pat3




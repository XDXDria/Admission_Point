from Tkinter import *
master = Tk()
master.title("ADMISSION")
Label(master, text="Faculty Number").grid(row=0,column=0)
Label(master, text="Thai").grid(row=1,column=0)
Label(master, text="Social").grid(row=2,column=0)
Label(master, text="Eng").grid(row=3,column=0)
Label(master, text="Math").grid(row=4,column=0)
Label(master, text="Science").grid(row=5,column=0)
Label(master, text="Physical").grid(row=6,column=0)
Label(master, text="Art").grid(row=7,column=0)
Label(master, text="Work").grid(row=8,column=0)
Label(master, text="GPA").grid(row=0,column=2)
Label(master, text="Gat").grid(row=1,column=2)
Label(master, text="Pat1").grid(row=2,column=2)
Label(master, text="Pat2").grid(row=3,column=2)
Label(master, text="Pat3").grid(row=4,column=2)
Label(master, text="Pat4").grid(row=5,column=2)
Label(master, text="Pat5").grid(row=6,column=2)
Label(master, text="Pat6").grid(row=7,column=2)
Label(master, text="Pat7").grid(row=8,column=2)

e0 = Entry(master)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)
e15 = Entry(master)
e16 = Entry(master)
e17 = Entry(master)

e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=0, column=3)
e10.grid(row=1, column=3)
e11.grid(row=2, column=3)
e12.grid(row=3, column=3)
e13.grid(row=4, column=3)
e14.grid(row=5, column=3)
e15.grid(row=6, column=3)
e16.grid(row=7, column=3)
e17.grid(row=8, column=3)


def get():
    lis= []
    pass_faculty = lis.append(e0.get())
    thai = lis.append(e1.get())
    social = lis.append(e2.get())
    eng = lis.append(e3.get())
    math = lis.append(e4.get())
    science = lis.append(e5.get())
    physical = lis.append(e6.get())
    art = lis.append(e7.get())
    work = lis.append(e8.get())
    gpa = lis.append(e9.get())
    gat = lis.append(e10.get())
    pat1 = lis.append(e11.get())
    pat2 = lis.append(e12.get())
    pat3 = lis.append(e13.get())
    pat4 = lis.append(e14.get())
    pat5 = lis.append(e15.get())
    pat6 = lis.append(e16.get())
    pat7 = lis.append(e17.get())
    nlis = []
    for i in lis:
        if i == '-':
            i = float(0)
            nlis.append(i)
        else:
           i = float(i)
           nlis.append(i)

    gpa = nlis[9]*1500
    thai = nlis[1]*15
    social = nlis[2]*15
    eng = nlis[3]*15
    math = nlis[4]*15
    science = nlis[5]*15
    physical = nlis[6]*5
    art = nlis[7]*5
    work = nlis[8]*5
    ans = 0
    if  nlis[0] >= 2024 and nlis[0] <= 2042:
        gat = nlis[10]*15
        pat2 = nlis[12]*15
        pat3 = nlis[13]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
        if nlis[0] == 2024:
            if ans >= 19055.35:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2025:
            if ans >= 17602.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2026:
            if ans >= 15965.9:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2027:
            if ans >= 17904.45:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2028:
            if ans >= 18131.4:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2029:
            if ans >= 17647.15:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2030:
            if ans >= 15795.3:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2031:
            if ans >= 16556.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2032:
            if ans >= 18002.05:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2033:
            if ans >= 17737.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2034:
            if ans >= 16298.65:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2035:
            if ans >= 16861.95:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2036:
            if ans >= 17148.75:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2037:
            if ans >= 16302.95:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2038:
            if ans >= 17170.7:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2039:
            if ans >= 16646.25:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2040:
            if ans >= 18353.75:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2041:
            if ans >= 17175.7:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2042:
            if ans >= 17499.55:
                print "PASS"
            else:
                print "NOT PASS"
    elif nlis[0] == 2043:
        gat = nlis[10]*30
        pat7 = nlis[17]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat7
        if ans >= 16876.95:
            print "PASS"
        else:
            print "NOT PASS"
    elif nlis[0] == 2044:
        gat = nlis[10]*50
        ans = thai+social+math+science+physical+art+work+gpa+gat
        if ans >= 19904.45:
            print "PASS"
        else:
            print "NOT PASS"
    elif nlis[0] == 2045:
        gat = nlis[10]*10
        pat3 = nlis[13]*20
        pat5 = nlis[15]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat3+pat5
        if ans >= 14999.45:
            print "PASS"
        else:
            print "NOT PASS"
    elif nlis[0] >= 2046 and nlis[0] <= 2048:
        gat = nlis[10]*10
        pat4 = nlis[14]*20
        pat5 = nlis[15]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat4+pat5
        if nlis[0] == 2046:
            if ans >= 15811.25:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2047:
            if ans >= 16136.3:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2048:
            if ans >= 15420:
                print "PASS"
            else:
                print "NOT PASS"
    elif nlis[0] == 2049:
        gat = nlis[10]*10
        pat2 = nlis[12]*20
        pat5 = nlis[15]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat5
        if ans >= 13261:
            print "PASS"
        else:
            print "NOT PASS"
    elif nlis[0] >= 2050 and nlis[0] <= 2067:
        gat = nlis[10]*10
        pat1 = nlis[11]*10
        pat2 = nlis[12]*30
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat1+pat2
        if nlis[0] == 2050:
            if ans >= 8968.25:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2051:
            if ans >= 12505.35:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2052:
            if ans >= 11939.35:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2053:
            if ans >= 11702.6:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2054:
            if ans >= 12400:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2055:
            if ans >= 13133.2:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2056:
            if ans >= 13839.35:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2057:
            if ans >= 14271.3:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2058:
            if ans >= 14277.55:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2059:
            if ans >= 13933.8:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2060:
            if ans >= 11243.2:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2061:
            if ans >= 13724.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2062:
            if ans >= 13213.2:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2063:
            if ans >= 12953.25:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2064:
            if ans >= 14944.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2065:
            if ans >= 13168.8:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2066:
            if ans >= 13852.55:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2067:
            if ans >= 14337.55:
                print "PASS"
            else:
                print "NOT PASS"
    elif nlis[0] == 2068:
        gat = nlis[10]*15
        pat2 = nlis[12]*15
        pat3 = nlis[13]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
        if ans >= 17757.85:
            print "PASS"
        else:
            print "NOT PASS"
    elif nlis[0] >= 2069 and nlis[0] <= 2071:
        gat = nlis[10]*30
        pat1 = nlis[11]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat1
        if nlis[0] == 2069:
            if ans >= 15257.5:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2070:
            if ans >= 15497.45:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2071:
            if ans >= 15943.2:
                print "PASS"
            else:
                print "NOT PASS"
    elif nlis[0] >= 2072 and nlis[0] <= 2074:
        gat = nlis[10]*10
        pat1 = nlis[11]*10
        pat2 = nlis[12]*30
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat1+pat2
        if nlis[0] == 2072:
            if ans >= 10783.2:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2073:
            if ans >= 11013.2:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2074:
            if ans >= 9789.4:
                print "PASS"
            else:
                print "NOT PASS"
    elif nlis[0] >= 2075 and nlis[0] <= 2076:
        gat = nlis[10]*15
        pat2 = nlis[12]*15
        pat3 = nlis[13]*20
        ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
        if nlis[0] == 2075:
            if ans >= 11161.25:
                print "PASS"
            else:
                print "NOT PASS"
        elif nlis[0] == 2076:
            if ans >= 10295.7:
                print "PASS"
            else:
                print "NOT PASS"

    print 'Your admission point is '+str(ans)+' Points.'

            
Button(master, text="Submit",command = get).grid(row=9,column=1)
Button(master, text="Close",command=master.destroy).grid(row=9,column=2)

mainloop( )

from Tkinter import *
def main():
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
    e0.grid(row=0, column=1)
    e1 = Entry(master)
    e1.grid(row=1, column=1)
    e2 = Entry(master)
    e2.grid(row=2, column=1)
    e3 = Entry(master)
    e3.grid(row=3, column=1)
    e4 = Entry(master)
    e4.grid(row=4, column=1)
    e5 = Entry(master)
    e5.grid(row=5, column=1)
    e6 = Entry(master)
    e6.grid(row=6, column=1)
    e7 = Entry(master)
    e7.grid(row=7, column=1)
    e8 = Entry(master)
    e8.grid(row=8, column=1)
    e9 = Entry(master)
    e9.grid(row=0, column=3)
    e10 = Entry(master)
    e10.grid(row=1, column=3)
    e11 = Entry(master)
    e11.grid(row=2, column=3)
    e12 = Entry(master)
    e12.grid(row=3, column=3)
    e13 = Entry(master)
    e13.grid(row=4, column=3)
    e14 = Entry(master)
    e14.grid(row=5, column=3)
    e15 = Entry(master)
    e15.grid(row=6, column=3)
    e16 = Entry(master)
    e16.grid(row=7, column=3)
    e17 = Entry(master)
    e17.grid(row=8, column=3)
    def get():
        lis = []
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
        pare = ''
        err = []
        faculty = [2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,
                   2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,
                   2072,2073,2074,2075,2076]
        point = [19055.35, 17602.5, 15965.9, 17904.45, 18131.4, 17647.15, 15795.3,
                  16556.5, 18002.05, 17737.5, 16298.65, 16861.95, 17148.75, 16302.95,
                  17170.7, 16646.25, 18353.75, 17174.7, 17499.55, 16876.95, 19904.45,
                  14999.45, 15811.25, 16136.3, 15420.0, 13261.0, 8968.25, 12505.35,
                  11939.35, 11702.6, 12400.0, 13133.2, 13839.35, 14271.3, 14277.55,
                  13933.8, 11243.2, 13724.5, 13213.2, 12953.25, 14944.5, 13168.8,
                  13852.55, 14337.55, 17757.85, 15257.5, 15497.45, 15943.2, 10783.2,
                  11013.2, 9789.4, 11161.25, 10295.7]
        for i in xrange(1,9):
            if nlis[i] < 0 or nlis[i] > 100:
                err.append(i)
        for i in xrange(10,18):
            if nlis[i] < 0 or nlis[i] > 300:
                err.append(i)
        if nlis[9] < 0 or nlis[9] > 4:
            err.append(9)
        if  nlis[0] >= 2024 and nlis[0] <= 2042:
            gat = nlis[10]*15
            pat2 = nlis[12]*15
            pat3 = nlis[13]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
            if nlis[0] == 2024:
                if ans >= point[0]:
                    pare = "You are PASS! and different point is "+str(ans-point[0]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[0]))
            elif nlis[0] == 2025:
                if ans >= point[1]:
                    pare = "You are PASS! and different point is "+str(ans-point[1]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[1]))
            elif nlis[0] == 2026:
                if ans >= point[2]:
                    pare = "You are PASS! and different point is "+str(ans-point[2]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[2]))
            elif nlis[0] == 2027:
                if ans >= point[3]:
                    pare = "You are PASS! and different point is "+str(ans-point[3])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[3]))
            elif nlis[0] == 2028:
                if ans >= point[4]:
                    pare = "You are PASS! and different point is "+str(ans-point[4])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[4]))
            elif nlis[0] == 2029:
                if ans >= point[5]:
                    pare = "You are PASS! and different point is "+str(ans-point[5])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[5]))
            elif nlis[0] == 2030:
                if ans >= point[6]:
                    pare = "You are PASS! and different point is "+str(ans-point[6])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[6]))
            elif nlis[0] == 2031:
                if ans >= point[7]:
                    pare = "You are PASS! and different point is "+str(ans-point[7])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[7]))
            elif nlis[0] == 2032:
                if ans >= point[8]:
                    pare = "You are PASS! and different point is "+str(ans-point[8])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[8]))
            elif nlis[0] == 2033:
                if ans >= point[9]:
                    pare = "You are PASS! and different point is "+str(ans-point[9])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[9]))
            elif nlis[0] == 2034:
                if ans >= point[10]:
                    pare = "You are PASS! and different point is "+str(ans-point[10])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[10]))
            elif nlis[0] == 2035:
                if ans >= point[11]:
                    pare = "You are PASS! and different point is "+str(ans-point[11])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[11]))
            elif nlis[0] == 2036:
                if ans >= point[12]:
                    pare = "You are PASS! and different point is "+str(ans-point[12])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[12]))
            elif nlis[0] == 2037:
                if ans >= point[13]:
                    pare = "You are PASS! and different point is "+str(ans-point[13])
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[13]))
            elif nlis[0] == 2038:
                if ans >= point[14]:
                    pare = "You are PASS! and different point is "+str(ans-point[14]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[14]))
            elif nlis[0] == 2039:
                if ans >= point[15]:
                    pare = "You are PASS! and different point is "+str(ans-point[15]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[15]))
            elif nlis[0] == 2040:
                if ans >= point[16]:
                    pare = "You are PASS! and different point is "+str(ans-point[16]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[16]))
            elif nlis[0] == 2041:
                if ans >= point[17]:
                    pare = "You are PASS! and different point is "+str(ans-point[17]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[17]))
            elif nlis[0] == 2042:
                if ans >= point[18]:
                    pare = "You are PASS! and different point is "+str(ans-point[18]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[18]))
        elif nlis[0] == 2043:
            gat = nlis[10]*30
            pat7 = nlis[17]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat7
            if ans >= point[19]:
                pare = "You are PASS! and different point is "+str(ans-point[19]) 
            else:
                pare = "You are NOT PASS and different point is "+str(abs(ans-point[19]))
        elif nlis[0] == 2044:
            gat = nlis[10]*50
            ans = thai+social+math+science+physical+art+work+gpa+gat
            if ans >= point[20]:
                pare = "You are PASS! and different point is "+str(ans-point[20]) 
            else:
                pare = "You are NOT PASS and different point is "+str(abs(ans-point[20]))
        elif nlis[0] == 2045:
            gat = nlis[10]*10
            pat3 = nlis[13]*20
            pat5 = nlis[15]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat3+pat5
            if ans >= point[21]:
                pare = "You are PASS! and different point is "+str(ans-point[21]) 
            else:
                pare = "You are NOT PASS and different point is "+str(abs(ans-point[21]))
        elif nlis[0] >= 2046 and nlis[0] <= 2048:
            gat = nlis[10]*10
            pat4 = nlis[14]*20
            pat5 = nlis[15]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat4+pat5
            if nlis[0] == 2046:
                if ans >= point[22]:
                    pare = "You are PASS! and different point is "+str(ans-point[22]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[22]))
            elif nlis[0] == 2047:
                if ans >= point[23]:
                   pare = "You are PASS! and different point is "+str(ans-point[23]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[23]))
            elif nlis[0] == 2048:
                if ans >= point[24]:
                    pare = "You are PASS! and different point is "+str(ans-point[24]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[24]))
        elif nlis[0] == 2049:
            gat = nlis[10]*10
            pat2 = nlis[12]*20
            pat5 = nlis[15]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat5
            if ans >= point[25]:
                pare = "You are PASS! and different point is "+str(ans-point[25]) 
            else:
                pare = "You are NOT PASS and different point is "+str(abs(ans-point[25]))
        elif nlis[0] >= 2050 and nlis[0] <= 2067:
            gat = nlis[10]*10
            pat1 = nlis[11]*10
            pat2 = nlis[12]*30
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat1+pat2
            if nlis[0] == 2050:
                if ans >= point[26]:
                    pare = "You are PASS! and different point is "+str(ans-point[26]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[26]))
            elif nlis[0] == 2051:
                if ans >= point[27]:
                    pare = "You are PASS! and different point is "+str(ans-point[27]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[27]))
            elif nlis[0] == 2052:
                if ans >= point[28]:
                    pare = "You are PASS! and different point is "+str(ans-point[28]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[28]))
            elif nlis[0] == 2053:
                if ans >= point[29]:
                    pare = "You are PASS! and different point is "+str(ans-point[29]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[29]))
            elif nlis[0] == 2054:
                if ans >= point[30]:
                    pare = "You are PASS! and different point is "+str(ans-point[30]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[30]))
            elif nlis[0] == 2055:
                if ans >= point[31]:
                    pare = "You are PASS! and different point is "+str(ans-point[31]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[31]))
            elif nlis[0] == 2056:
                if ans >= point[32]:
                    pare = "You are PASS! and different point is "+str(ans-point[32]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[32]))
            elif nlis[0] == 2057:
                if ans >= point[33]:
                    pare = "You are PASS! and different point is "+str(ans-point[33]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[33]))
            elif nlis[0] == 2058:
                if ans >= point[34]:
                    pare = "You are PASS! and different point is "+str(ans-point[34]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[34]))
            elif nlis[0] == 2059:
                if ans >= point[35]:
                    pare = "You are PASS! and different point is "+str(ans-point[35]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[35]))
            elif nlis[0] == 2060:
                if ans >= point[36]:
                    pare = "You are PASS! and different point is "+str(ans-point[36]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[36]))
            elif nlis[0] == 2061:
                if ans >= point[37]:
                    pare = "You are PASS! and different point is "+str(ans-point[37]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[37]))
            elif nlis[0] == 2062:
                if ans >= point[38]:
                    pare = "You are PASS! and different point is "+str(ans-point[38]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[38]))
            elif nlis[0] == 2063:
                if ans >= point[39]:
                    pare = "You are PASS! and different point is "+str(ans-point[39]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[39]))
            elif nlis[0] == 2064:
                if ans >= point[40]:
                    pare = "You are PASS! and different point is "+str(ans-point[40]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[40]))
            elif nlis[0] == 2065:
                if ans >= point[41]:
                    pare = "You are PASS! and different point is "+str(ans-point[41]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[41]))
            elif nlis[0] == 2066:
                if ans >= point[42]:
                    pare = "You are PASS! and different point is "+str(ans-point[42]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[42]))
            elif nlis[0] == 2067:
                if ans >= point[43]:
                    pare = "You are PASS! and different point is "+str(ans-point[43]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[43]))
        elif nlis[0] == 2068:
            gat = nlis[10]*15
            pat2 = nlis[12]*15
            pat3 = nlis[13]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
            if ans >= point[44]:
                pare = "You are PASS! and different point is "+str(ans-point[44]) 
            else:
                pare = "You are NOT PASS and different point is "+str(abs(ans-point[44]))
        elif nlis[0] >= 2069 and nlis[0] <= 2071:
            gat = nlis[10]*30
            pat1 = nlis[11]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat1
            if nlis[0] == 2069:
                if ans >= point[45]:
                    pare = "You are PASS! and different point is "+str(ans-point[45]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[45]))
            elif nlis[0] == 2070:
                if ans >= point[46]:
                    pare = "You are PASS! and different point is "+str(ans-point[46]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[46]))
            elif nlis[0] == 2071:
                if ans >= point[47]:
                    pare = "You are PASS! and different point is "+str(ans-point[47]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[47]))
        elif nlis[0] >= 2072 and nlis[0] <= 2074:
            gat = nlis[10]*10
            pat1 = nlis[11]*10
            pat2 = nlis[12]*30
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat1+pat2
            if nlis[0] == 2072:
                if ans >= point[48]:
                    pare = "You are PASS! and different point is "+str(ans-point[48]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[48]))
            elif nlis[0] == 2073:
                if ans >= point[49]:
                    pare = "You are PASS! and different point is "+str(ans-point[49]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[49]))
            elif nlis[0] == 2074:
                if ans >= point[50]:
                    pare = "You are PASS! and different point is "+str(ans-point[50]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[50]))
        elif nlis[0] >= 2075 and nlis[0] <= 2076:
            gat = nlis[10]*15
            pat2 = nlis[12]*15
            pat3 = nlis[13]*20
            ans = thai+social+math+science+physical+art+work+gpa+gat+pat2+pat3
            if nlis[0] == 2075:
                if ans >= point[51]:
                    pare = "You are PASS! and different point is "+str(ans-point[51]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[51]))
            elif nlis[0] == 2076:
                if ans >= point[52]:
                    pare = "You are PASS! and different point is "+str(ans-point[52]) 
                else:
                    pare = "You are NOT PASS and different point is "+str(abs(ans-point[52]))
        
        if  nlis[0] not in faculty:
            print "Invalid faculty number plese enter correct number"
        elif len(err) != 0:
            print "You score range in is invalid "
        else:
            print 'Your admission point is '+str(ans)+' Points.'
            print pare
    Button(master, text="Submit",command = get).grid(row=9,column=1)
    Button(master, text="Close",command=master.destroy).grid(row=9,column=2)
    mainloop()
main()

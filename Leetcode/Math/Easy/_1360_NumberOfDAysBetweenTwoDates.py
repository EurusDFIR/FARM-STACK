

def daysBetweenDates( date1: str, date2: str) -> int:
    
    def isLeapYear(x:int)->bool:
        return  x %400==0 or (x %4==0 and x%100 !=0)

    def switchDate(date:str)->int:
        #2019-06-29

        d = int(date[-2:])
        m = int(date[5:7])
        y = int(date[0:4])
        s =0
        for i in range(0, y):
            #is leapyear
            if isLeapYear(i): s+=366
            else: s+=365
        
        # get day in specific year
        sWday =0
        x = 29 if isLeapYear(y) else 28
        lw = [0,31,x,31,30,31,30,31,31,30,31,30,31]
        for i in range(1, m):
            sWday+=lw[i]
        sWday +=d
        
        # get absolute day 
        s+=sWday
        return s
    return max(switchDate(date2), switchDate(date1)) - min(switchDate(date2), switchDate(date1))


# date1 = "2019-06-29"
# date2 = "2019-06-30"
# date1 = "2020-01-15"
# date2 = "2019-12-31"
date1 ="2009-08-18"
date2 ="2080-08-08"
res = daysBetweenDates(date1,date2)
print(res)



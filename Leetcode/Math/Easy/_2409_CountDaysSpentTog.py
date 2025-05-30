

def switchDays(day: str)-> int:
    lM= [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = int(day[-2:]) #18
    m = int(day[0:2]) #8

    mSw = 0
    for i in range(1,m):
        mSw += lM[i]
    mSw+=d
    return mSw
def test (day: str)->int:
    return switchDays(testDAy)


def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    startDay = max(switchDays(arriveAlice), switchDays(arriveBob))
    endDay = min(switchDays(leaveAlice), switchDays(leaveBob))

    return endDay - startDay +1 if startDay <= endDay else 0

testDAy = "01-15"
print(test(testDAy))
# arriveAlice = "08-15"
# leaveAlice = "08-18"
# arriveBob = "08-16"
# leaveBob = "08-19"
arriveAlice ="09-01"
leaveAlice ="10-19"
arriveBob ="06-19"
leaveBob ="10-20"
# arriveAlice = "10-01"
# leaveAlice = "10-31"
# arriveBob = "11-01"
# leaveBob = "12-31"
# res = countDaysTogether(arriveAlice,leaveAlice, arriveBob,leaveBob)

# print(res)
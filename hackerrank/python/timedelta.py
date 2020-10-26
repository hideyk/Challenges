import os
from datetime import datetime as dt, timedelta
import unittest

date_file = r"misc/testdates"
delta_file = r"misc/deltaresult"
with open(date_file, "r") as istr:
    datetext = istr.read().split("\n")
with open(delta_file, "r") as istr:
    deltatext = istr.read().split("\n")

# Complete the time_delta function below.
def time_delta(t1, t2):
    T1, z1 = dt.strptime(" ".join(t1.split()[:-1]), "%a %d %b %Y %H:%M:%S"), t1.split()[-1]
    T2, z2 = dt.strptime(" ".join(t2.split()[:-1]), "%a %d %b %Y %H:%M:%S"), t2.split()[-1]
    T1 = T1 - timedelta(hours=int(z1[1:3])) - timedelta(minutes=int(z1[-2:])) if z1[0] == "+" else \
        T1 + timedelta(hours=int(z1[1:3])) + timedelta(minutes=int(z1[-2:]))
    T2 = T2 - timedelta(hours=int(z2[:3])) - timedelta(minutes=int(z2[-2:])) if z2[0] == "+" else \
        T2 + timedelta(hours=int(z2[1:3])) + timedelta(minutes=int(z2[-2:]))
    timediff = abs(T1-T2)
    return str(timediff.seconds + timediff.days * 60 * 60 * 24)

class Test(unittest.TestCase):
    def testTimeDelta(self):
        for i in range(len(deltatext)):
            with self.subTest(msg=datetext[2*i] + " " + datetext[2*i+1]):
                self.assertEquals(time_delta(datetext[2*i],datetext[2*i+1]), deltatext[i])


if __name__ == '__main__':
    unittest.main()

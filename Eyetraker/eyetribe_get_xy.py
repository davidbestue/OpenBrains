




from peyetribe import EyeTribe
import time

tracker = EyeTribe()
tracker.connect()
n = tracker.next()

print("eT;dT;aT;Fix;State;Rwx;Rwy;Avx;Avy;LRwx;LRwy;LAvx;LAvy;LPSz;LCx;LCy;RRwx;RRwy;RAvx;RAvy;RPSz;RCx;RCy")

tracker.pushmode()
count = 0
while count < 100:
    n = tracker.next()
    print(n)
    count += 1

tracker.pullmode()

tracker.close()


















from pupil_support import *
import numpy as np



v_tr = 0.5
subject_name = 'name'

pupil = Pupil(subject_name=subject_name,v_tr=v_tr)
pupil_on = pupil.test_pupil()

import time as t
def testFn():
    pass
    startTime = t.time()
    testFn()
    endTime = t.time()
    runTimeInSec = endTime.startTime
    print(f"\n time to execute function is {runTimeInSec/60} min")
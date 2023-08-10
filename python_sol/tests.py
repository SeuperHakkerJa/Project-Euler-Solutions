from utils import *
import time

@timeout(1)
def test_timeout():
    for _ in range(5):
        print("running...")
        time.sleep(0.5)

test_timeout()
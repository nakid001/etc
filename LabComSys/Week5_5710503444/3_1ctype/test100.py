import ctypes
import time

start = time.time()

testlib = ctypes.CDLL('./my100c.so')
testlib.myprint()
end = time.time()
print(end - start)

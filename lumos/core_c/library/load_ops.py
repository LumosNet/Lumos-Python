from ctypes import *

class CBias():
    def __init__(self):
        self.add_bias = None

class CLumos():
    def __init__(self):
        self.library = None
        self.bias = None
        self.cpu = None
        self.gemm = None
        self.im2col = None
        self.image = None
        self.pooling = None
        self.random = None

liblumos = cdll.LoadLibrary("/usr/local/lumos/lib/liblumos.so")
add_bias = liblumos.add_bias()

cbias = CBias()
cbias.add_bias = add_bias

clumos = CLumos()
clumos.library = liblumos
clumos.bias = cbias

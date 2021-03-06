import math
from getch import getch

import tg

x = 1024	# Window width
xs = 10		# Graph width
g = 1		# Distance between grid lines

tg.theme("dark.json")
tg.Mkrs = [-3,5]

### Math functions
def Log(x): # f(x) = log x
	return math.log(x,10)

def Arit(x): # f(x) = 2x
	return 2*x

def Sin(x): # f(x) = sin(x)
	return math.sin(x)

def Exp(x): # f(x) = 2^x
	return 2**x

def Mod(x): # f(x) = |x|
	return math.sqrt(x**2)

def Quad(x): # f(x) = x²
	return x**2

tg.init(x,xs,g)

tg.plot(Quad)
tg.plot(Sin)
tg.plot(Log)
tg.plot(Arit)
tg.plot(Exp)
tg.plot(Mod)

getch()
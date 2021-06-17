import math
## Task 0.1
## Mathematical operators

def mul(x, y):
	return x * y

def id(x):
	return x

def neg(x):
	return -x

def add(x, y):
	return x + y

def lt(x, y):
	return 1.0 if x < y else 0.0

def eq(x, y):
	return 1.0 if x == y else 0.0

def max(x, y):
	return x if x > y else y

def sigmoid(x):
	return (
		1.0 / (1.0 + math.pow(math.e, -x))
		if x >= 0
		else math.pow(math.e, x) / (1.0 + math.pow(math.e, x))
	)

def relu(x):
	return x if x > 0 else 0

def relu_back(x, y):
	return y if x > 0 else 0

EPS = 1e-6

def log(x):
	return math.log(x + EPS)


def exp(x):
	return math.exp(x)


def log_back(a, b):
	return b / (a + EPS)


def inv(x):
	return 1.0 / x

def inv_back(a, b):
	return -(1.0 / a ** 2) * b


## Task 0.3
## Higher-order functions.


def map(fn):
	def process(ls):
		arr = []
		for item in ls:
			arr.append(fn(item))
		return arr

	return process

# ~ mapear = map
# ~ fn = mapear(2*x)
# ~ procesar_fn = fn([1,2,3])
# ~ result : [2,4,6]


def negList(ls):
	return map(neg)(ls)


def zipWith(fn):
	def process(ls1, ls2):
		arr = []
		for i in range(len(ls1)):
			arr.append(fn(ls1[i], ls2[i]))
		return arr

	return process


def addLists(ls1, ls2):
	return zipWith(add)(ls1, ls2)


def reduce(fn, start):
	def process(ls):
		ans = start
		for item in ls:
			ans = fn(ans, item)
		return ans

	return process

def sum(ls):
	return reduce(add, 0)(ls)


def prod(ls):
	return reduce(mul, 1)(ls)

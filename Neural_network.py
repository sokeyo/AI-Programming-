import numpy
def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

w1 = numpy.random.rand()
w2 = numpy.random.rand()
b = numpy.random.rand()

print(w1)
print(w2)
print(b)





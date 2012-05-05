import numpy

from Pycluster import kcluster

data = numpy.array([
    (1, 1, 0),
    (1, 0, 0),
    (0, 0, 0)
])

print data

labels, error, nfound = kcluster(data, 2)
print labels

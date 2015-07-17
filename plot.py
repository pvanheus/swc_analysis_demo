import numpy
import matplotlib.pyplot
import glob

# Here's a small change: now we only read the file in once and pass the data array into the functions.
# How can we do this better?
# We keep recalculating the minima and maxima. Why don't we calculate these values once, and pass them into the functions?

def check(data):

    # check if the maxima are linear
    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        print "These maxima are suspicious"
    else:
        print "These maxima look OK"

    # check if the minima are zero
    if data.min(axis=0).sum() == 0:
        print "These minima are suspicious"
    else:
        print "These minima look OK"

def plot(data):
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()

    matplotlib.pyplot.show(fig)

filenames = glob.glob("data/inflammation-*.csv")

for filename in filenames:
    print filename
    data = numpy.loadtxt(fname=filename, delimiter=',')
    check(data)
    plot(data)

import numpy
import matplotlib.pyplot
import glob

# Now we only calculate the means, maxima and minima once. Not only are we not repeating calculations unnecessarily, but we now use meaningful labels for these values when we use them.
# How can we do this better?
# There's a lot of repetition inside these functions. Can we split them up into smaller functions?

def check(maxima, minima):

    # check if the maxima are linear
    if maxima[0] == 0 and maxima[20] == 20:
        print "These maxima are suspicious"
    else:
        print "These maxima look OK"

    # check if the minima are zero
    if minima.sum() == 0:
        print "These minima are suspicious"
    else:
        print "These minima look OK"

def plot(means, maxima, minima):
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(means)

    axes2.set_ylabel('max')
    axes2.plot(maxima)

    axes3.set_ylabel('min')
    axes3.plot(minima)

    fig.tight_layout()

    matplotlib.pyplot.show(fig)

filenames = glob.glob("data/inflammation-*.csv")
filenames.sort()

for filename in filenames:
    print filename

    data = numpy.loadtxt(fname=filename, delimiter=',')
    minima = data.min(axis=0)
    maxima = data.max(axis=0)
    means = data.mean(axis=0)
    
    check(maxima, minima)
    plot(means, maxima, minima)

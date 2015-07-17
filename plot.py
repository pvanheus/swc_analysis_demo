import numpy
import matplotlib.pyplot
import glob

# use glob.glob to find all the files
filenames = glob.glob("data/inflammation-*.csv")
# uncomment to temporarily pick just the first three
# leaving this in here in case we need to test stuff later
# filenames = filenames[:3]

for filename in filenames:
    data = numpy.loadtxt(fname=filename, delimiter=',')

    print filename # so that we can see which datasets trigger warnings

    # check for suspicious features in the data

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

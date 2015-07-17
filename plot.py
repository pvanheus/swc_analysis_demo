import numpy
import matplotlib.pyplot
import glob

# Let's refactor the problem checking functions first.

#We can make some very simple functions which only check for one problem, and don't print anything.

def check_linear(values):
    "Return True if the values look linear, otherwise return False"
    return values[0] == 0 and values[20] == 20

def check_zero(values):
    "Return True if the values add up to zero, otherwise return False"
    return values.sum() == 0

# Now we can make one function that prints stuff.  This function takes another function as a parameter.
# We'll be able to call it with the functions we defined above, or any other compatible function we define in the future.
# In this way we have separated the printing code from the checking code, and we only define each part in one place.

def warn_if_problem_found(values, check_function, name):
    "Call this check function on these values, and print whether a problem is found"
    # check_function with no parentheses is the variable name which stores the function.
    # check_function(...) is how we call the function. This does the same thing as calling check_linear(...) or check_zero(...) directly.
    if check_function(values):
        print "These", name, "are suspicious"
    else:
        print "These", name, "look OK"

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
    
    # We have eliminated our old check function entirely, and just call our message-printing function from here directly.
    # We can mix and match any values with any check function now -- we could check if the minima are linear or if the means are zero.
    warn_if_problem_found(maxima, check_linear, "maxima")
    warn_if_problem_found(minima, check_zero, "minima")
    
    plot(means, maxima, minima)

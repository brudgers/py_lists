from functools import reduce as reduce
import operator

# Helpers

def identity(x):
    return x

less_than = operator.lt
lt = operator.lt
less_than_or_equal = operator.le
le = operator.le
equal = operator.eq
eq = operator.eq
non_equal = operator.ne
ne = operator.ne
greater_than_or_equal = operator.ge
ge = operator.ge

# List Basics

def cons (element, a_list):
    """
    Adds an elment to the *front* of a_list.
    If a_list is not a list, cons creates a list of one element holding a_list.
    """
    if not type(a_list) == list:
        a_list = [a_list]
    a = [element]
    a.extend(a_list)
    return a

def first(a_list):
    """
    Returns the first elment of a list.
    Returns False if the list is empty.
    """
    if len(a_list)==0:
        return False
    else:
        return a_list[0]

def rest(a_list):
    """
    Returns a list minus its first elment.
    Returns false if list is empty.
    Returns the empty list if list has one element.
    """
    if len(a_list)==0:
        return False
    elif len(a_list)==1:
        return []
    else:
        return a_list[1:]

def list_append(*args):
    return reduce(list.__add__, args)

# Non Destructive List functions

def copy_list(ls):
    return [i for i in ls]

def remove(item, sequence, from_end=False, test=equal, test_not=False, start=None, end=None, count=False, key=identity):

    # chop the front off the sequence if only
    # using part of it
    if start:
        front = sequence[:start]
    else:
        front = []
    # chop the rear off the sequence if only
    # using part of it
    if end:
        rear = sequence[rear:]
    else:
        rear = []

    # make a copy of the sequence for local mutation
    # and cut to length
    seq = copy_list(sequence)[start:end]

    # reverse the target sequence if requested
    if from_end:
        seq = seq.reverse()

    # If there's no count, let it be seq length
    if not count:
        _count = len(seq)
    else:
        _count = count

    # Add the iterate closure
    def iterate():
        c = 0
        ret = []
        for i in seq:
            if c < _count:
                if test(key(i),item):
                    c += 1
                else:
                    ret += [i]
            else:
                ret += [i]
        return ret

    # Add iterate_not closure
    

    # Main logic
    if not test_not:
        middle = iterate()
        # return values in the same order
        if from_end:
            middle.reverse()
        return list_append(front,middle,rear)
    else:
        middle = iterate_not()
        # return values in the same order        
        if from_end:
            middle.reverse()
        return list_append(front,middle,rear)

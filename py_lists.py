import operator
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

def identity(x):
    return x

def copy_list(ls):
    return [i for i in ls]

def remove(item, sequence, from_end=False, test=equal, test_not=False, start=0, end=False, count=False, key=identity):
    # make a copy of the sequence for local mutation
    seq = copy_list(sequence)
    # if no end is specified, use the end of seq
    if not end:
        end = len(seq) - 1
    # chop the sequence before possible reversing    
    seq = seq[start:end]
    # reverse the target sequence if requested
    if from_end:
        seq = seq.reverse()
    # If there's no count, let it be seq length
    if not count:
        count = len(seq)

    # Add the iterate closure
    def iterate():
        c = 0
        ret = []
        for i in seq:
            if c < count:
                if test(key(i),item):
                    c += 1
                else:
                    ret += [i]
            else:
                ret += [i]
        return ret
    # Add iterate_not closure
    def iterate():
        c = 0
        ret = []
        for i in seq:
            if c < count:
                if not test(key(i),item):
                    c += 1
                else:
                    ret += [i]
            else:
                ret += [i]
        return ret

    # Main logic
    if test_not:
        return iterate()
    else:
        return iterate_not()

def remove_if(pred, seq):
    return [i for i in pred if not pred(i)]

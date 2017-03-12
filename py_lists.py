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

def remove(item, sequence, from_end=False, test=identity, test_not=False, start=False, end=False, count=False, key=identity):
    return [i for i in sequence if not test(key(i)) == item]

def remove_if(pred, seq):
    return [i for i in pred if not pred(i)]

def std(lst):
    mean = sum(lst)/len(lst)
    std = (sum([(i-mean)**2 for i in lst])/len(lst))**0.5
    return std


def var(lst):
    mean = sum(lst)/len(lst)
    var = sum([(i-mean)**2 for i in lst])/len(lst)
    return var


def mean(lst):
    return sum(lst)/len(lst)


def median(lst):
    lst.sort()
    if(len(lst)%2 != 0):
        return lst[len(lst)//2]
    else:
        return (lst[(len(lst)//2)-1] + lst[len(lst)//2])/2


def mode(lst):
    return max(set(lst), key=lst.count)


def range(lst):
    return max(lst)-min(lst)

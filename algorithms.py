def mystd(lst):
    mean = sum(lst)/len(lst)
    std = (sum([(i-mean)**2 for i in lst])/len(lst))**0.5
    return std


def myvar(lst):
    mean = sum(lst)/len(lst)
    var = sum([(i-mean)**2 for i in lst])/len(lst)
    return var


if __name__ == "__main__":
    import numpy as np
    speed = [32,111,138,28,59,77,97]

    # checking mystd
    std = np.std(speed)
    mystd = mystd(speed)
    if mystd == std:
        print('mystd is ok...')
    else:
        print('something went wrong in mystd...')
    del std, mystd

    # checking myvar
    var = np.var(speed)
    myvar = myvar(speed)
    if myvar == var:
        print('myvar is ok...')
    else:
        print('something went wrong in myvar...')
    del var, myvar

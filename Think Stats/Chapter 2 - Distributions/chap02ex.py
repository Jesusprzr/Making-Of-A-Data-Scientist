"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2

hist = thinkstats2.Hist([1, 2, 2, 3, 5])
import thinkplot
thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')

def Mode(hist):
    """ (hist) -> number
    Returns the value with the highest frequency.
    """
#The mode of the author:
    p, x = max([(p, x) for x, p in hist.Items()])
    return x
#My mode (sexier but a lot worst LMAO):
def mode(hist):
    lst = []
    kl = []
    tl = []
    for k, i in hist.Items():
        lst.append(i)
        kl.append(k)
        tl.append([k, i])
    defl = []
    for pair in tl:
        if max(lst) == pair[1]:
            defl.append(pair)
    for k in kl:
        if k == defl[0][0]:
            return k
    print(lst, kl, tl, defl)


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
#Author's allmodes:
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

#My allmodes (it works, differently to authors one but works):
def allmodes(hist):
    lst = []
    for k, i in hist.Items():
        lst.append([i, k])
    for item in lst:
        lst.sort(reverse=True)
    for pair in lst:
        pair.reverse
            
    return lst
#Example that it works:
hist1 = thinkstats2.Hist([1, 2, 2, 2, 3, 3, 3, 3, 5, 5])
allmodes(hist)

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

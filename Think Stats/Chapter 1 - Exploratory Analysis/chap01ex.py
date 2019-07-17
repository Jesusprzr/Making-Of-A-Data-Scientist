"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
from collections import defaultdict
import numpy as np
import sys
import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    ''' (str file name, str file name) -> DataFrame
    
    Reads the NSFG respondents data file and returns a DataFrame.
    '''
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    ''' (df) -> Nonetype
    Recodes variables of the respondent frame.
    '''
    pass

def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df

def CleanFemPreg(df):
    ''' (df) -> Nonetype
    Recodes variables of the pregnancy frame.
    '''
    # Convert mothers ages from centiyears to years:
    df.agepreg /= 100.0
    # Replace with NaN possible bogus values from birthwgt_lb:
    df.loc[df.birthwgt_lb > 20, 'birthwgtlb'] = np.nan
    
    # replace 'not ascertained', 'refused', 'don't know' with NaN
    # For weight
    na_values = [97, 98, 99]
    df.birthwgt_lb.replace(na_values, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_values, np.nan, inplace=True)
    df.hpagelb.replace(na_values, np.nan, inplace=True)
    
    # For sexuality
    df.babysex.replace([7, 9], np.nan, inplace=True)
    df.nbrnaliv.replace([9], np.nan, inplace=True)
    
    # Now group birthwgt into a single variable in lb:
    # Dictionary syntax is needed because we are going to create a new row
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
    
    # due to a bug in ReadStataDct, the last variable gets clipped;
    # so for now set it to NaN
    df.cmintvw = np.nan

def ValidatePregnum(resp, preg):
    ''' (int, int) -> bool
    Returns True if the pregnum of the respondent file is equal to
    the number of records on the pregnancy file.
    '''
    # Mapping claseid with it's respective pregnancy indices:
    preg_map = MakePregMap(preg) 
    # Iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        
        # Check for equality between pregnancy file and respondent file:
        if len(indices) != pregnum:
            print('ID :', caseid, len(indices), '!=', pregnum)
            return False
    return True

    
def MakePregMap(df):
    ''' (DataFrame) -> Dict
    Returns a dictionary of the DataFrame that maps every caseid
    with it's respective indices in the dataframe.    
    '''
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d
    
def main():
    """Tests the functions in this module.

    script: string script name
    """
    # Read and validate the respondent file:
    resp = ReadFemResp()
    
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    
    # Read and validate the pregnancy file:
    preg = ReadFemPreg()
    print(preg.shape)
    
    assert len(preg) == 13593
    assert preg.caseid[13592] == 12571
    assert preg.nbrnaliv.value_counts()[1] == 8981
    assert preg.babysex.value_counts()[1] == 4641
    assert preg.birthwgt_lb.value_counts()[7] == 3049
    assert preg.birthwgt_oz.value_counts()[0] == 1037
    assert preg.prglngth.value_counts()[39] == 4744
    assert preg.outcome.value_counts()[1] == 9148
    assert preg.birthord.value_counts()[1] == 4413
    assert preg.agepreg.value_counts()[22.75] == 100
    assert preg.totalwgt_lb.value_counts()[7.5] == 302
    
    weights = preg.finalwgt.value_counts()
    key = max(weights.keys())
    assert preg.finalwgt.value_counts()[key] == 6
    
    # Check for equality between pregnum column in resp and
    #number of entries in preg:
    assert(ValidatePregnum(resp, preg))
    
    print('All tests passed.')


if __name__ == '__main__':
    main()

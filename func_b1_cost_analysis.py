# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:57:50 2021

@author: matko
"""

def quantity_discount_factor(F_EXP=0.95,N=1000):
    """
    

    Parameters
    ----------
    F_EXP : float, range 0.01-0.99
        Experience effectiveness (learning curve)
        0.01 - Max experience
        0.99 - Min experience
        
        80% experience effectiveness means that if it takes a technician
        100 hrs to put together, say, a batch of 10 assemblies, the next
        batch will only take 80% of that time, or 80 hrs, and the next
        batch will take 64 hrs, and so on.
    N : integer
        Number of units produced.

    Returns
    -------
    QDF - Quantity Discount Factor.
    -------
    Source: Snorri pg 36

    """
    import numpy as np
    QDF = F_EXP**(1.4427*np.log(N))
    return QDF
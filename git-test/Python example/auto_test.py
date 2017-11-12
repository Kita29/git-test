def func_m(v1,v2,v3):
    """Average three numbers

    >>> func_m(20, 30, 70)
    40.0
    
    >>> func_m(1, 5, 8)
    6.667
    
    """
    return round((v1+v2+v3)/3,3)

import doctest
#automatic test in documentation
doctest.testmod()

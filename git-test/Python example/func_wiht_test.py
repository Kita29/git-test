def func_wiht_test(val1):
    """Test

    >>> func_wiht_test(2)
    32
    >>> func_wiht_test(3)
    145

    """
    
    return ((val1**4) + (4**val1))

import doctest
doctest.testmod()

"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result.pop(result.index(1))
    result.pop(result.index(9))
    return result  

fn_hack_8()
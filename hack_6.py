"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    return [i for i in range(6)]
print(fn_hack_6())
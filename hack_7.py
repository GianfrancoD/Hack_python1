"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    result = range(0,5+1)
    number_result = []

    for i in result[::-1]:
        number_result.append(i)
    return number_result

print(fn_hack_7())
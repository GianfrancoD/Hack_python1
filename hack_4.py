"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    resultado = result[:-1] + result[-1].upper()
    return resultado
print(fn_hack_4())
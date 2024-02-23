"""
text: "fooziman" output => "f00z1m@n"
"""
def fn_hack_5():
    result = list("fooziman")
    result[1] = "0"
    result[2] = "0"
    result[4] = "1"
    result[6] = "@"

    """
    OTRA FORMA DE HACERLO

    new_result = ""
    for i in result:
        if i == "o":
            new_result += "0"
        elif i == "i":
            new_result += "1"
        elif i == "a":
            new_result += "@"
        else:
            new_result += i
    """
    return result
print(fn_hack_5())
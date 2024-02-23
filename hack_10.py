"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
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
    result_list = list(new_result.upper())
    return result_list

print(fn_hack_10())
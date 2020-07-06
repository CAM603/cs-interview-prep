# Need reps on this
def decodeStr(s):
    stack = []
    currCount = 0
    currStr = ""

    for char in s:
        if char == '[':
            stack.append(currStr)
            stack.append(currCount)
            currStr = ""
            currCount = 0
        elif char == ']':
            count = stack.pop()
            prevStr = stack.pop()
            currStr = prevStr + currStr * count
        elif char.isdigit():
            currCount = currCount * 10 + int(char)
        else:
            currStr += char

    return currStr


print(decodeStr("3[a]2[bc]"))

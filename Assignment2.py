#1
def reversed_string(text):
result = ""
index = len(text) - 1
while index >= 0:
result += text[index]
index -= 1
return result

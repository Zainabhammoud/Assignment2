#1
def reverse(s,i):
  
  s=input("Enter the list to be reversed: ")
  i=int(input("Enter the number of concatenation: "))
  
  if i == 0:
    return " "
  else:
    reverse_s = s[::-1]
    new = reverse_s * i
  return new
print("Reversed list is :" + reverse(" ",0))

#2
def sort(s):
  s = input("Add the word: ")
  lower = []
  upper = []
  for char in s:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
      
  sorted_str = ''.join(upper + lower)
  print('Result:', sorted_str)



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

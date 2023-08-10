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
  count=0  
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

print("************")


#3
def test_for_anagrams (s1, s2):

  s1 = s1.lower()
  s2 = s2.lower()
  count = 0
  if (len(s1) != len(s2)):
        return (False)
  else:
        for i in range(0, len(s1)):
            for j in range(0, len(s2)):
                if(s1[i] == s2[j]):
                    count += 1
            if (count == len(s1)):
              return (True)
        else:
            return (False)
s1 = input("Enter a string 1: ")
s2 = input("Enter a string 2: ")
result = test_for_anagrams (s1, s2)
print (result)  
print("************")





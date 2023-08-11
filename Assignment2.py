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
print("************")


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


#4
def max_value(l):
  l=[]
l = [5,6,3,2,7,4,0,1,6,-2]
print("From th list: ",l)
l.sort()
max_index = l.index(l[-1])
min_index = l.index(l[0])
print("The highest value in the list is ",l[-1]," at index ",max_index)
print('The lowest value in the list is ', l[0]," at index ",min_index)
print("************")







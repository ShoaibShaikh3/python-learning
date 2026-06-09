word1 = input("Enter 1st String: ")
word2 = input("Enter 2nd String: ")

if sorted(word1) == sorted(word2):
  print("Anagram")
else: 
  print("Not Anagram")

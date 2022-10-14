# find Digits, words,letters:
numofwords=0
numofletters=0
numofdigits=0
txt=input("Eneter a txt : ")
for x in txt:
   x=x.upper()
   if x>='A' and x<='Z':
    numofletters=numofletters+1
   elif x>='0' and x<='9':
     numofdigits=numofdigits+1
   elif x==' ':
     numofwords=numofwords+1

print("Number of letter is ",numofletters)
print("Number of Digit is ",numofdigits)
print("Number of Word is ",numofwords+1)



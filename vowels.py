count = input("Type in a word to see how many vowels there are: ")

vowels = 0
for i in count:
      if(i =='a' or i =='e' or i =='i' or i =='o' or i =='u' or
         i =='A' or i =='E' or i =='I' or i =='O' or i =='U'):
            vowels=vowels+1
print("Number of vowels: " + str(vowels))

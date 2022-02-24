Sentence = input("Enter your Sentence: ")

words = 0
space = False
for char in Sentence:
  if char==" ":
     if space==False:
       words += 1
       space = True
  else:
      space = False
if(len(Sentence) == 0 or Sentence == space):
    print("There isnt any word in your sentence.")
else:
    print("There is ",{words+1}," word in your sentence.")
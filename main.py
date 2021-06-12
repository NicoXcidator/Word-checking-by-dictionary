word = input("Word to check: ")
word_dict = {}
for letter in word:
  if letter in word_dict:
    word_dict[letter] += 1
  else:
    word_dict[letter] = 1

for key in word_dict:
  print(f"The word {word} has {word_dict[key]} {key}.")
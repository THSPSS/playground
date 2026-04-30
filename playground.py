#reverse the character

word_from_user = input("Please Type the word that want to reverse : ")


#========set Variable======================

if len(word_from_user) == 1:
    print(f"word has one character : {word_from_user}")
else:
    result = word_from_user[::-1]
    print(result)




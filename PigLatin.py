#This program converts normal sentence into PigLatin and back to Normal

#Convert from Normal Sentence to PigLatin
def normal_to_pigLatin(text): 
    newText=""
    for eachWord in text.split():
        #print (eachWord)
        eachWord+= eachWord[0]
        newText += eachWord[1:] + "ay "
        #print (newText)
    return (newText)

#Convert from PigLatin to Normal Sentence 
def pigLatin_to_normal(text):
    newText = ""
    for eachWord in text.split():
        #print(eachWord)
        newText+=eachWord[-3]
        newText+=eachWord[:-3] + " "
        #print(newText)
    return (newText)

#text = "The quick brown fox"
normal_to_pigLatin("The quick brown fox")
pigLatin_to_normal("heTay uickqay rownbay oxfay")
# Count how many words are in a Sentence
# It counts everything between spaces as words
def wordCount(s = None):
    if s == None:
        return 0
    sSplit = s.split(' ')
    print("Output: ",len(sSplit))
    return len(sSplit)
#sentence = input('\nEnter Sentence: ')
#wordCount(sentence)

import string
#find if a sentence contains only ascii letters
#-we determine class of Stringlibrary
#-we define the class and initialse with __init__
#-we define if is_appening
#
class StringLibrary:  # this is a camelcase namimg
    
    def __init__(self, sentence):
        self.sentence = sentence
        

    def is_ascii_letters(self):
        res = self.sentence.split()
        for word in res:
            for char in word:
                print(char)
                if char not in string.ascii_letters:
                    return False
        return True

sentence_ = "This; is what I can do"     

StringLibrary_ = StringLibrary(sentence_)

print(StringLibrary_.is_ascii_letters())

        





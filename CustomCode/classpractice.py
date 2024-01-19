class TextAnalyzer(object):
    def __init__(self, text):
        formattedtext = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedtext = formattedtext.lower()
        self.text = formattedtext

    def freqof(self):
        freqword = {}
        wordlist  = self.text.split()
        for word in set(wordlist):
            freqword[word] = wordlist.count(word)

        return freqword


givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
abc = TextAnalyzer(givenstring)
print(abc.freqof())
from collections import Counter
class TextAnalyzer():
    characters_to_remove = ".!,?"
    stopwords = ["the", "is", "in", "and", "to", "a", "of" , "it","this"]
    def __init__ (self, text,filter_choice):
        self.unprocessed_text = text
        # make text lowercase
        processed_text = text.lower()
        # remove punctuation
        for char in self.characters_to_remove:
            processed_text = processed_text.replace(char,"")
        self.fmtText = processed_text
        self.filter_choice = filter_choice
        
        self.freq_Dict = self.freqAll() ## compute frequency dictionary once during initialization

        
    def freqAll(self):        
        # split text into words
        word_list = self.fmtText.split()
        word_counts = Counter(word_list)
        if self.filter_choice == 'n':
            return dict(word_counts)
        else:
            frequency_dict = {word: count for word, count in word_counts.items() if word not in self.stopwords}
            return frequency_dict
        

           
    def freqOf(self,word):
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
    def countSentences(self):
        sentences = self.unprocessed_text.split('.')
        return len([s for s in sentences if s.strip()]) # count non-empty sentences only
    
    def countParagraphs(self):
        paragraphs = self.fmtText.split('\n\n')
        return len([p for p in paragraphs if p.strip()]) # count non-empty paragraphs only
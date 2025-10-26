from collections import Counter
import csv
import json

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
        self.total_sentences = self.countSentences() ## compute total sentences once during initialization
        self.total_paragraphs = self.countParagraphs() ## compute total paragraphs once during initialization

        
    def freqAll(self):        
        # split text into words
        word_list = self.fmtText.split()
        word_counts = Counter(word_list)
        if self.filter_choice == 'n':
            return dict(word_counts)
        else:
            frequency_dict = {word: count for word, count in word_counts.items() if word not in self.stopwords}
            return frequency_dict
        
    
    
    
    #def create_content_summary(self):
        words_dict = "\n".join([f"{word}: {count}" for word, count in self.freqAll().items()])
        total_sentences = self.countSentences()
        total_paragraphs = self.countParagraphs()
        summary = ("=== Text Analysis Summary ===\n"
                   f"Word Frequencies:\n{words_dict}\n\n"
                   f"Total number of sentences: {total_sentences}\n"
                   f"Total number of paragraphs: {total_paragraphs}\n")
        return summary
    
    def write_to_file(self,filename):
        if filename.endswith('.csv'):
            self.export_to_csv(filename)
        elif filename.endswith('.json'):
            self.export_to_json(filename)
        elif filename.endswith('.txt'):
            self.export_to_txt(filename)
        else:
            print("Error: Unsupported file format. Please use .csv, .json, or .txt")

    def export_to_csv(self, filename):
      
        try:
            with open(filename, 'w', newline='') as csvfile: #newline='' to avoid blank lines in Windows
                writer = csv.writer(csvfile)
                writer.writerow(['Word', 'Frequency']) # write header
                for word, freq in self.freqAll().items():
                    writer.writerow([word, freq])
                writer.writerow(['Total Sentences', self.total_sentences])
                writer.writerow(['Total Paragraphs', self.total_paragraphs])
            print(f"Word frequencies successfully exported to {filename}")
        except IOError:
            print("Error: Could not write to CSV file.")



    def export_to_json(self, filename):
        try:
            data = {
                'word_frequencies': self.freqAll(),
                'total_sentences': self.total_sentences,
                'total_paragraphs': self.total_paragraphs   
            } # prepare data dictionary
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4) 
            print(f"Word frequencies successfully exported to {filename}")
        except IOError:
            print("Error: Could not write to JSON file.")

    def export_to_txt(self, filename):
        try:
            with open(filename, 'w') as txtfile:
                for word, freq in self.freqAll().items():
                    txtfile.write(f"{word}: {freq}\n")
                txtfile.write(f"\nTotal Sentences: {self.total_sentences}\n")
                txtfile.write(f"Total Paragraphs: {self.total_paragraphs}\n")
            print(f"Word frequencies successfully exported to {filename}")
        except IOError:
            print("Error: Could not write to TXT file.")
        
       
           
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
    
  
import string 
filename = input("please enter the file name: ")
sentences = 0 
paragraphs = 0
with open(filename,'r') as f:
    text = f.read()


# first we clean the text from punctuation and lowercase everything and split the text by space 

for char in text:
    if char in ".!?":
        sentences+=1

paragraphs = text.split("\n\n")
paragraphs = [p for p in paragraphs if p.strip() != ""]
paragraph_count = len(paragraphs)



text = text.lower()
for char in string.punctuation:
    text = text.replace(char,"") #remove punctuation 

words = len(text.split())

print(words)
print(sentences)
print(paragraph_count)


from analyzer import TextAnalyzer

while True:
    x = input("Please enter the name of the text file to analyze: ")
    
    try:
        if x.strip().lower() in ['exit', 'quit','q']:
            print("Exiting the program.")
            break
        else:
            with open(x, "r") as f: # using with so file is properly closed after its suite finishes
                choice = input("Would you like to filter out common stopwords? (y/n): ").strip().lower()
                text_content = f.read()
                text_analyzer = TextAnalyzer(text_content, choice)
            
            print("Word frequencies: \n")
            print(text_analyzer.freqAll())
            print(f"\nTotal number of sentences: {text_analyzer.countSentences()}")
            print(f"Total number of paragraphs: {text_analyzer.countParagraphs()}\n")
            word = input("Please enter a word to get its frequency: ")
            count = text_analyzer.freqOf(word)
            print(f"The word '{word}' appears {count} time{'s' if count != 1 else''}.")
            text_analyzer.write_to_file(input("Enter the output filename (txt, json, cs) to save the analysis: "))
            
      

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except IOError:
        print("Error: There was a problem reading the file.")
        
    
    print("Would you like to analyze another file? (y/n):")
    answer = input().strip().lower()
    if answer != 'y':
        print("Thank you for using the Text Analyzer.")
        break
    


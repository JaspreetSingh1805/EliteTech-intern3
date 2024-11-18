
def generate_acronym(phrase):
   
    # Splitting the phrase into words
    words = phrase.split()
    
    # Creating an acronym by taking the first letter of each word and capitalizing it
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def main():
    print("Welcome to the Acronyms Creator!")
    while True:
        # Asking user for input
        phrase = input("Enter a phrase (or type 'exit' to quit): ").strip()
        
        # Exit condition
        if phrase.lower() == 'exit':
            print("Thank you for using the Acronyms Creator. Goodbye!")
            break
        
        # Check if input is valid
        if phrase:
            # Generate acronym and display result
            acronym = generate_acronym(phrase)
            print(f"Phrase: {phrase}")
            print(f"Acronym: {acronym}")
        else:
            print("Please enter a valid phrase!")

if __name__ == "__main__":
    main()

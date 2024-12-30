def main():
    with open("/home/ec2-user/workspace/github.com/Shyam-Prag/bookbot/books/frankenstein.txt") as file:
        content = file.read()
        return content

def count_words(text):
    counter = 0
    for i in text:
        counter += 1
    return counter

#Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any character to lowercase, we don't want duplicates.
def count_chars(text):
    lowered_text = text.lower()
    char_counter = {}

    for letter in lowered_text:
        if letter.isalpha():           
            if letter in char_counter:
                char_counter[letter] += 1
            else:
                char_counter[letter] = 1
    
    return char_counter

def print_report():
    print('--- Begin report of books/frankenstein.txt ---')
    
    #get words from main
    text = main() 

    # use created func to get word count 
    total_word_count = count_words(text)
    print(f"{total_word_count} words found in the document")

    # initialize dict
    counter = count_chars(text=text)
    
    #print(counter.items())
    """
    The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

    counter.items() --> converts item in dict to tuple which can be accessed via indexes. 

    returns a list of tuples like below:
    [('p', 6121), ('r', 20818), ('o', 25225), ('j', 504), ('e', 46043), ('c', 9243), ('t', 30365), ('g', 5974), ('u', 10407), ('n', 24367), ('d', 16863), ('h', 19725), ('v', 3833), ('z', 243), ('x', 677), ('q', 324)]
    """
    
    
    sorted_dict = sorted(counter.items(), key = lambda kv: (kv[1], kv[0]), reverse=True)
    for element in sorted_dict:
        print(f"The '{element[0]}' character was found {element[1]} times")

    print("------ END REPORT ------")
    

print_report()
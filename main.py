#need to take in a paper, assuming no abstract
#use example.txt for this
#use one shrink to ensure the paper is the right size?
#call our model for it, make sure they know to have to provide an api key
#print the result

import sys
from fine_tune.finetune_summary import summarize_text
from utils.one_shrink import shrink_one

def main():
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Use "example.txt" as the default file if no argument is provided
        file_path = "example.txt"

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Call the shrink function
        shrunk_data = shrink_one(file_content, file_path)

        # Call the abstract making function
        abstract = summarize_text(shrunk_data)

        # Print the result
        print("Abstract:")
        print(abstract)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

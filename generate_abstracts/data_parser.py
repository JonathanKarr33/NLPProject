
import os
import json
# Function to read text from a file


def read_file(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data = json.loads(line)
                data_list.append(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line}")
                print(e)
    return data_list


# Main program
if __name__ == "__main__":
    # Example usage
    input_file_path = 'data/thousand_papers/thousand_papers_700_1700.txt'
    output_directory = "data/thousand_papers"
    output_file_path = f"{output_directory}/parsed_data.json"

# Ensure the output directory exists

    # Read all lines as dictionaries
    result_list = []
    result = read_file(input_file_path)
    for article in result:
        article_text = ""
        # Iterate through the outer list
        for sublist in article["article_text"]:
            article_text += sublist + " "
        abstract_text = ""
        for sublist in article["abstract_text"]:
            abstract_text += sublist + " "
        abstract_text = abstract_text.replace("<S>", "").replace(
            "</S>", "").replace("\n", "")
        result_dict = {"article_id": article["article_id"],
                       "abstract_text": abstract_text, "article_text": article_text}
        result_list.append(result_dict)

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Write each line to the file
    with open(output_file_path, 'w') as file:
        json.dump(result_list, file, indent=2)

    print(f"Data has been written to {output_file_path}")

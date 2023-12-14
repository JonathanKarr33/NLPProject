import tiktoken
import json

def calculate_token_count(text, model_name='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = len(encoding.encode(text))
    return tokens


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
    input_file_path = 'data/smallest_100/smallest_arxiv_600_700.txt'

    # Read all lines as dictionaries
    result = read_file(input_file_path)
    for article in result:
        # print(len(article["article_text"]))
        text = ""
        # Iterate through the outer list
        for sublist in article["article_text"]:
            text += sublist + "\n"

        token_count = calculate_token_count(text)
        print(f"Token count for the input text: {token_count}")

    '''prompt = "Once upon a time in a"
    generated_text = generate_response(prompt)
    print(f"Generated text: {generated_text}")'''

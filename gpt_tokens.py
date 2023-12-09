import tiktoken
# import openai

# Function to calculate token count for a given text


def calculate_token_count(text, model_name='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = len(encoding.encode(text))
    return tokens

# Function to interact with the GPT-3.5-turbo model


'''def generate_response(prompt, model_name='text-davinci-003'):
    # Assuming you have OpenAI Python library installed and configured with your API key
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=100  # You can adjust the parameters based on your requirements
    )
    return response.choices[0].text.strip()'''
# Function to read text from a file


def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


# Main program
if __name__ == "__main__":
    # Example usage
    input_file_path = 'data/short/main_paper/2312.04318.txt'
    input_text = read_text_from_file(input_file_path)
    token_count = calculate_token_count(input_text)
    print(f"Token count for the input text: {token_count}")

    '''prompt = "Once upon a time in a"
    generated_text = generate_response(prompt)
    print(f"Generated text: {generated_text}")'''

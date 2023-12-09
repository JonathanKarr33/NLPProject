from openai import OpenAI
client = OpenAI()

response = client.files.create(
  file=open("test.jsonl", "rb"), #! need to make this file
  purpose="fine-tune"
)
print(response)
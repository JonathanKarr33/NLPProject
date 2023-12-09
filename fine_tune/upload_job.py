from openai import OpenAI
client = OpenAI()

response = client.files.create(
  file=open("train.jsonl", "rb"), # change if needed
  purpose="fine-tune"
)
response = client.files.create(
  file=open("val.jsonl", "rb"), #! does this work
  purpose="fine-tune"
)
print(response)
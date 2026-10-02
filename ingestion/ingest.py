import json

yokai_data = 0

with open("data/yokai.json", "r", encoding="utf-8") as f:
  yokai_data = json.load(f)

def generate_chunks(items, size):
  for i in range(0, len(items), size):
    yield items[i:i + size]


for batch in generate_chunks(yokai_data, 10):
  chunk = dict(batch)
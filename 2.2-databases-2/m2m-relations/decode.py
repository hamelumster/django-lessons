import json

with open('articles.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

with open('articles_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
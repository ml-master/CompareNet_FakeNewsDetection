import json


num = 0
with open('./data/gossipcop_v3_origin.json', 'r', encoding='utf-8') as file:
    buf = json.load(file)

dict_list = []
length = 100

for person, info in buf.items():
    dict_list.append({'tag': '2' if info['label'] == 'fake' else '4',
                      'text': info['text']})
    length = len(info['text']) if len(info['text']) > length else length

num = 1
print(length)
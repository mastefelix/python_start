import json

with open('text_7.json', 'w', encoding='utf-8') as new_f:
    with open('text_7.txt', 'r', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                           len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, new_f, ensure_ascii=False, indent=2)

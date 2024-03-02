import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = {}
    with open(csv_file_path, 'r', encoding='euc-kr') as csvfile:  # 인코딩을 변경합니다.
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            item = {
                "weight": row[1],
                "vesa_size": row[2],
                "screw_size": row[3] if len(row) > 3 else ""
            }
            data[row[0]] = item

    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

csv_file_path = 'tvsize.csv' # 변경 필요
json_file_path = 'tvsize.json' # 변경 필요
csv_to_json(csv_file_path, json_file_path)
print("JSON 파일이 성공적으로 생성되었습니다.")

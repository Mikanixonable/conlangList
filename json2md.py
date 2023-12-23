import json
from pprint import pprint
import chardet
def detect_encoding(file_path):
    # ファイルのエンコーディングを検出
    with open(file_path, 'rb') as file:
        detector = chardet.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']


"""
  "entries": [
    {
      "normalized": "kn_ja_jpx_kwn",
      "bcp47": "x-v3-kwnjpxja-kn",
      "codes": {
        "dialect": "kn",
        "language": "ja",
        "family": "jpx",
        "user": "kwn"
      },
      "names": {
        "dialect": "川音方言",
        "language": "日本語",
        "family": "日流語族",
        "user": "川音リオ"
      },
      "approved": true,
      "createdDate": "2022-08-22T11:14:13.553Z",
      "approvedDate": "2022-11-23T11:09:10.072Z"
    },"""

def dic2md(dic):
    md = ''
    for lang in dic:
        family=''
        language = ''
        dialect = ''
        user = lang["names"]["user"]


        if "family" in lang["names"]:
            family=f'{lang["names"]["family"]} '

        if "language" in lang["names"]:
            language=f'{lang["names"]["language"]} '

        if "dialect" in lang["names"]:
            dialect=f'{lang["names"]["dialect"]}'

        md+=f'\n|{user}|{family}|{language}|{dialect}|{lang["normalized"]}|'
    return md

# JSONファイルのパス
file_path = './clacode2022-11-23.json'
encoding = detect_encoding(file_path)
# JSONファイルを読み込んで辞書に変換
with open(file_path, 'r',encoding=encoding) as json_file:
    dic = json.load(json_file)["entries"]

md = """
|user|family|language|dialect|CLAコード|
|---|---|---|---|---|"""
md += dic2md(dic)
# 辞書オブジェクトを使って何かをする（例: 表示）
pprint(md)
with open("clacode.md", 'w', encoding='utf-8') as file:
    file.write(md)

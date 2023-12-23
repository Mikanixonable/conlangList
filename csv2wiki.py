import csv
import chardet
from pprint import pprint 

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

def csv2dic(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', newline='', encoding=encoding) as file:
        reader = csv.DictReader(file, delimiter=',')
        dic = []
        for row in reader:
            for key,value in list(row.items()):
                row[key] = row[key].split(",")
                #空なら入れない
                if value =='':
                    del row[key]
                
            #空なら入れない
            if len(row.keys()) != 0:
                dic.append(row)

        return dic
    



def dic2md(dic):
    md = """
{| class="wikitable" style="margin:auto"
|+ 人工言語一覧
|-
! 言語名 !! 年代 !! 作者

"""
    for lang in dic:
        md+='\n|-\n'

        name = ''
        if 'サイト' in lang:
            name += "[{b} {a}]".format(a=lang["言語名"][0],b=lang['サイト'][0])
        else:
            name += "{a}".format(a=lang["言語名"][0])

 
        if len(lang['言語名'])>2:
            for i in range(len(lang['言語名']) - 1):
                name += ', '+lang['言語名'][i+1]
        year = ''
        if '年代' in lang:

            year = lang['年代'][0]


        artist = ''
        if '作者' in lang:
            if '作者Twitter' in lang:
                artist += '[{b} {a}]'.format(a=lang['作者'][0],b=lang['作者Twitter'][0])
            else:
                artist += lang['作者'][0]
        if '作者' in lang:
            if len(lang['作者'])>2:
                for i in range(len(lang['作者']) - 1):
                    artist+= ', '+lang['作者'][i+1]
        
        
        links = '   '
        if 'サイト' in lang:
            if len(lang['サイト'])>2:
                for i in range(len(lang['サイト']) - 1):
                    links+= '([{a} サイト{i}])'.format(i=str(i+2),a = lang['サイト'][i+1])
        if '文法' in lang:
            links += '([{a} 文法])'.format(a = lang['文法'][0])
            
        if '文法' in lang:
            if len(lang['文法'])>2:
                for i in range(len(lang['文法']) - 1):
                    links+= '([{a} 文法{i}])'.format(i=str(i+2),a = lang['文法'][i+1])
        
        if '辞書' in lang:
            links += '([{a} 辞書])'.format(a = lang['辞書'][0])

        if '辞書' in lang:
            if len(lang['辞書'])>2:
                for i in range(len(lang['辞書']) - 1):
                    links+= '([{a} 辞書{i}])'.format(i=str(i+2),a = lang['辞書'][i+1])

        md +="| {a} {d}|| {b} || {c}".format(a=name,b=year,c=artist,d=links)
    md+="|}\n"
    return md


md = """

# 日本語圏人工言語リスト(2023年12月)
　日本語圏の人工言語のリストが最近作られていないと思ったので、底となるリストを参考に、新しい言語も合わせてつくったものです。リストのすべての言語の情報は私がアクセスして確認しなおしています。
　このリストは後で作るリストのための下準備という位置づけで、人工言語として言及されているものは見つけ次第すべて入れています。そのため、創作世界の設定に名前だけ登場するような言語や、ツイッター上で思い付きで作られた言語も含んでいます。
　言語の説明やCLAコードの入った生データは以下のリンクからアクセスできます。tsv(タブ区切り値)形式であり、Excelから開けます。私は著作権を放棄するので、利用したい方は使ってください。
https://mikanixonable.github.io/data/conlang.tsv

追記 utf-8でcsv形式に書き直しました
https://mikanixonable.github.io/data/conlang.csv

## 底としたリスト
* [http://dos.chottu.net/conlang_link.html?l=index 人工言語リスト 日本人による人工言語（アイウエオ順] - 2nd LVG IMG.The Second Living Image.
2004年

* [https://conlinguistics.org/link.html 人工言語リンク集] - 人工言語学
2012年

* [https://conlinguistics.fandom.com/ja/wiki/%E8%A8%80%E8%AA%9E%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7 言語記事一覧] - 人工言語wiki
2016年ごろと思われる

* [https://itest.5ch.net/test/read.cgi/twwatch/1513511369/ 人工言語界隈リスト] - 5ch
2017-12-17

* [https://docs.google.com/spreadsheets/d/1t_WxHJ_b39PWXIMauHwnSww_Ac2m_Mw7zC-vQkp59PQ/edit#gid=0 人工言語を作ってるor勉強してる人が少し分かるリスト] - Maycia Arenberg
2018-02-24
現在はリクエスト承認が必要という表示が出る
[https://x.com/mayciaarenberg/status/963447200087879680?s=46&t=rWvY73qZa5Ie23yU0UA6WA 紹介ツイート]
[https://twitter.com/jin_kou_gengo 人工言語クラスタフォロー]というこのリストに入っていたアカウントをフォローするアカウントがあったため、少し漏れがあるがリストを復元することができる。@2me_ma_sagiさんありがとう

* [http://twoc.ever.jp/twoc/conlang.cgi?mode=list 辞書リスト] - The world of conlangs
 2020年ごろ

* [https://sites.google.com/site/moyacilang/conlanglist 人工言語リスト] - slaimsan
たぶんもっとも網羅的
2020年

* [https://ziphil.com/other/other/1.html リンク集 人工言語] - Ziphil
文法が確認できるものに絞って載せている
2021年3月

* [https://x.com/i/lists/994189952551346176 conlanger] - Mikanixonable
私みかぶるが手当たり次第人工言語作者っぽい人を入れているツイッターの人工言語ラーのリスト
2023年

* [https://tanukipedia.miraheze.org/wiki/%E6%9E%B6%E7%A9%BA%E8%A8%80%E8%AA%9E 架空言語] - Tanukipedia (タヌキペディア) 
2023年

* [https://sites.google.com/view/ryuuka/k-ren-gong-yan-yurinku-ji?authuser=0 人工言語 柳霞] - J．人工言語リンク集
2020年ごろ?

* [https://japan.fandom.com/wiki/%E6%9E%B6%E7%A9%BA%E3%81%AE%E8%A8%80%E8%AA%9E%E4%B8%80%E8%A6%A7 架空の言語一覧] - 架空の言語一覧 | Japan | Fandom

* [https://w.atwiki.jp/kakis/pages/5471.html#id_1b7f8ccd アーカイブ] - atwiki（アットウィキ） 

* [https://sites.google.com/site/faraspalt/links?authuser=0 Faras' Room] - Links 

* [https://w.atwiki.jp/kursodeesperanto/pages/36.html アルカ-リンク] - はじめてのエスペラント - atwiki（アットウィキ）  

* [https://w.atwiki.jp/koreori/ 世界模擬実験塔設定集] - atwiki（アットウィキ） 
"""



dic = csv2dic('conlang.csv')
for lang in dic:
    if '年代' not in lang:
        print(lang['言語名'])
pprint(dic)
# dic = sorted(dic, key=lambda x: int(x['年代'][0][0:4]))

md += dic2md(dic)

with open("conlangWiki.md", 'w', encoding='utf-8') as file:
    file.write(md)

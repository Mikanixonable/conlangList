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
    md = '|言語名|活動年代|作者|'
    md += '\n|---|---|---|'
    for lang in dic:
        name = ''
        if 'サイト' in lang:
            name += "[{a}]({b})".format(a=lang["言語名"][0],b=lang['サイト'][0])
        else:
            name += "{a}".format(a=lang["言語名"][0])

 
        if len(lang['言語名'])>2:
            for i in range(len(lang['言語名']) - 1):
                name += ', '+lang['言語名'][i+1]

     
        year = lang['年代'][0]
 


        artist = ''
        if '作者' in lang:
            if '作者Twitter' in lang:
                artist += '[{a}]({b})'.format(a=lang['作者'][0],b=lang['作者Twitter'][0])
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
                    links+= '([サイト{i}]({a}))'.format(i=str(i+2),a = lang['サイト'][i+1])
        if '文法' in lang:
            links += '([文法]({a}))'.format(a = lang['文法'][0])
            
        if '文法' in lang:
            if len(lang['文法'])>2:
                for i in range(len(lang['文法']) - 1):
                    links+= '([文法{i}]({a}))'.format(i=str(i+2),a = lang['文法'][i+1])
        
        if '辞書' in lang:
            links += '([辞書]({a}))'.format(a = lang['辞書'][0])

        if '辞書' in lang:
            if len(lang['辞書'])>2:
                for i in range(len(lang['辞書']) - 1):
                    links+= '([辞書{i}]({a}))'.format(i=str(i+2),a = lang['辞書'][i+1])

        md +="\n|{a}{d}|{b}|{c}|".format(a=name,b=year,c=artist,d=links)
        md+="|  "
    return md


md = """

# 日本語圏人工言語リスト5版(2023年12月)
　日本語圏の人工言語のリストが最近作られていないと思ったので、底となるリストを参考に、新しい言語も合わせてつくったものです。リストのすべての言語の情報は私がアクセスして確認しなおしています。
　このリストは後で作るリストのための下準備という位置づけで、人工言語として言及されているものは見つけ次第すべて入れています。そのため、創作世界の設定に名前だけ登場するような言語や、ツイッター上で思い付きで作られた言語も含んでいます。
　言語の説明やCLAコードの入った生データは以下のリンクからアクセスできます。tsv(タブ区切り値)形式であり、Excelから開けます。私は著作権を放棄するので、利用したい方は使ってください。

参照用url: https://mikanixonable.github.io/conlangList/conlang.csv
GitHub:  https://github.com/Mikanixonable/conlangList/blob/main/conlang.csv
更新履歴(GitHub): https://github.com/Mikanixonable/conlangList/commits/main/conlang.csv

## 更新履歴
1版 2023-12-17
2版 2023-12-18
3版 2023-12-19
4版 2023-12-21
5版 2023-12-23

## Babel Index Viewerの紹介
[かえる](https://twitter.com/kaeru2193)さんが、人工言語リストの検索システムを作ってくれました!この検索システムでは説明欄やモユネ分類など、この表では表示の都合上省いている要素も調べることができます。
https://tools.kaeru2193.net/Babel-Index-Viewer/
万が一私のgithubリポジトリにアクセスできなくなればかえるさんのリポジトリから復元することができます
https://github.com/kaeru2193/Conlang-List-Works/tree/main


## 底としたリスト
- [人工言語リスト 日本人による人工言語（アイウエオ順）](http://dos.chottu.net/conlang_link.html?l=index) - 2nd LVG IMG.The Second Living Image.
2004年

- [人工言語憩いの場アーカイブ](https://w.atwiki.jp/kakis/pages/5471.html#id_1b7f8ccd) - atwiki（アットウィキ） 
2007年

- [人工言語リンク集](https://conlinguistics.org/link.html) - 人工言語学
2012年

- [架空の言語一覧](https://japan.fandom.com/wiki/%E6%9E%B6%E7%A9%BA%E3%81%AE%E8%A8%80%E8%AA%9E%E4%B8%80%E8%A6%A7) - 架空の言語一覧 | Japan | Fandom
2014年

- [アルカ-リンク](https://w.atwiki.jp/kursodeesperanto/pages/36.html) - はじめてのエスペラント - atwiki（アットウィキ）  
2014年

- [世界模擬実験塔設定集](https://w.atwiki.jp/koreori/) - atwiki（アットウィキ） 
2015年

- [Faras' Room](https://sites.google.com/site/faraspalt/links?authuser=0 ) - Links 
2015年ごろ?

- [言語記事一覧](https://conlinguistics.fandom.com/ja/wiki/%E8%A8%80%E8%AA%9E%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7) - 人工言語wiki
2016年ごろと思われる

- [人工言語界隈リスト](https://itest.5ch.net/test/read.cgi/twwatch/1513511369/) - 5ch
2017-12-17

- [人工言語を作ってるor勉強してる人が少し分かるリスト](https://docs.google.com/spreadsheets/d/1t_WxHJ_b39PWXIMauHwnSww_Ac2m_Mw7zC-vQkp59PQ/edit#gid=0) - Maycia Arenberg
2018-02-24
現在はリクエスト承認が必要という表示が出る
[紹介ツイート](https://x.com/mayciaarenberg/status/963447200087879680?s=46&t=rWvY73qZa5Ie23yU0UA6WA)
[人工言語クラスタフォロー](https://twitter.com/jin_kou_gengo)というこのリストに入っていたアカウントをフォローするアカウントがあったため、少し漏れがあるがリストを復元することができる。@2me_ma_sagiさんありがとう

- [辞書リスト](http://twoc.ever.jp/twoc/conlang.cgi?mode=list) - The world of conlangs
 2020年ごろ

- [人工言語 柳霞](https://sites.google.com/view/ryuuka/k-ren-gong-yan-yurinku-ji?authuser=0) - J．人工言語リンク集
2020年ごろ?

- [人工言語リスト](https://sites.google.com/site/moyacilang/conlanglist) - slaimsan
たぶんもっとも網羅的
2020年

- [リンク集 人工言語](https://ziphil.com/other/other/1.html) - Ziphil
文法が確認できるものに絞って載せている
2021年3月

- [conlanger](https://x.com/i/lists/994189952551346176) - Mikanixonable
私みかぶるが手当たり次第人工言語作者っぽい人を入れているツイッターの人工言語ラーのリスト
2023年

- [架空言語](https://tanukipedia.miraheze.org/wiki/%E6%9E%B6%E7%A9%BA%E8%A8%80%E8%AA%9E) - Tanukipedia (タヌキペディア) 
2023年

"""

dic = csv2dic('conlang.csv')
for lang in dic:
    if '年代' not in lang:
        print(lang['言語名'])
# pprint(dic)
# dic = sorted(dic, key=lambda x: int(x['年代'][0][0:4]))
print(len(dic))


md +="""
## 人工言語リスト
"""
md += dic2md(dic)

md += """

2023年12月 Mikanixonable
"""

with open("notsort.md", 'w', encoding='utf-8') as file:
    file.write(md)

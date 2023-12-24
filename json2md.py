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

tsuika = """~_tp_~_kar　TOPUI 　by かえる
~_ia_~_hal　Inhaik=Ailetphĩna語(𐓮𐓶𐓤𐓙𐓧𐓟 𐒿𐓘̄𐓩𐓶𐓮 𐓮𐓘𐓰𐓙 𐒻𐓩𐓡𐓙𐓤=𐒱𐓧𐓟𐓰𐓬𐓸𐓣̄𐓩𐓘)　by 佐藤陽花
~_oi_~_hal　オイナルシャルム語(外語; Oinarшalm)　by 佐藤陽花
~_jb_~_hal　Jejbiq語(Los y'Jejbiq)　by 佐藤陽花
jo_fn_fun_kar　雰語上都方言　by かえる
~_fn_fun_kar 　雰語　by かえる
~_pn_phn_kar　雰語　by かえる
~_do_~_sky　120210823語　by Skytomo"""
dic += [{"normalized": lang.split('　')[0],"names":{"language": lang.split('　')[1],"user":lang.split('　')[2].split(' ')[1]}} for lang in tsuika.split('\n')]
dic = sorted(dic, key=lambda x: x['names']['user'])

header = """
　最新のCLAコードを管理していたconlang portalが2022-11-23に停止してから一年以上CLAコードの登録は人力で行われ、コードの閲覧にはCL-KIITAのdiscordサーバーに参加する必要があり、日本語圏の人工言語の規格として公共性が不十分に感じたので、現在の管理者佐藤陽花氏[@Distr_to_Yonder](https://twitter.com/Distr_to_Yonder)に許可をもらって一覧記事を作ることにしました。新しい管理システムができるまでのあいだ、コードを簡単に確認するために非公式に設けた仮の一覧であり、登録作業を反映して更新されるわけではないので、最新の情報ではないことに注意してください。根拠となるデータは、CLA v1については[人工言語学wikiの記事](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)、CLA v3についてはCL-KIITAのdiscordにあるconlang portalのログファイル"message.txt"および「各種人工言語コードアナウンス」チャンネルでの手動追加報告です。
## CLAコードとは
　[CLAコード](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)とは、国際的な言語コード[ISO-639](https://ja.wikipedia.org/wiki/ISO_639)に似せて、日本語圏の人工言語コミュニティーが2015年から発行してきた人工言語の識別符号です。CLAコードには、おかゆ氏の管理していたCLA v1と、そのコードを改良・移管した佐藤陽花氏の管理するCLA v3があります。英語圏の人工言語コミュニティーでは、似た試みとして[kreativekorp.com](https://www.kreativekorp.com/clcr/)が[ISO-639-3](https://ja.wikipedia.org/wiki/ISO_639-3)互換コードを発行・管理しています。
### CLA v1(2015-07-21から2021-08-03)
　2015-07-21から2021-08-03までのCLA v1はおかゆ氏[@oka_iu_tcan](https://twitter.com/oka_iu_tcan)によって管理され、google formによる申請フォームから登録申請し、おかゆ氏が手動で登録作業を行い、CLAコードの情報は[人工言語学wikiの記事](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)で確認できました。
　CLA v1は
- 語族が存在する架空世界のある芸術言語の創作スタイルを前提にしている
- ISOの言語コードと衝突する
- すべての制作者がコードを共有するためコードを巡って争いが起きることが予想される
- 開発停止した言語が名前空間を占有し続ける

という問題があり、語族を持たない言語については、無所属の語族コード「**」が提案され、トキポナに割り当てられました。
### CLA v2の提案(2021-08-03から2021-08-20)
2021-08-03に最後のCLA v1の登録が行われてから2021-08-20までの間に、佐藤陽花氏によってCLA v1の語族コードを語族以外にも使えるように拡張した私案CLA v2が提案されました。CLA v2では、ラテン小文字3字の言語コードと、ラテン小文字2字からなる語族領域をスラッシュでつなげますが、
- 語族領域がチルダ~で始まる場合は製作者領域(~**)
- ハッシュ#で始まる場合は無所属領域(#**)
- クエスチョン?で始まる場合は未定領域(?**)

として、語族以外の情報を扱えるように語族コードが拡張されています。CLA v2は例示のためにオ゛ェｼﾞｭルニョェーッ語に「fez/fb」が割り当てられた他は運用されませんでした。
### CLA v3のconlang portalによる運用(2021-08-20から2022-11-23)
　2021-08-20に、CLA v2をもとに佐藤陽花氏、Ziphil氏、 Xirdim氏,、フルヒト氏を始めとするメンバーによってCLA v3の大枠が[決まり](https://twitter.com/Distr_to_Yonder/status/1428400052658053120)、2021-08-31にZiphil氏[@Ziphil](https://twitter.com/Ziphil)によるCLA v3の申請、閲覧サイトであるconlang portalが[開設](https://x.com/Ziphil/status/1432665606034116616?s=20)され、翌2021-09-01にCLA v1の申請受付が[停止されました](https://twitter.com/oka_iu_tcan/status/1433031033008525312)。2021-09-02には[CLA v3仕様書](https://github.com/CL-KIITA/CLACode_SRI/blob/conla/docs/spec/cla_code.md)が公開されました。
　2021-08-20から2022-11-23までconlang portalでCLA v3を申請し、閲覧することができました。
### CLA v3のCL-KIITA discordサーバー上の手動運用(2022-11-23以降)
　2022-11-23にconlang portalをホスティングしていたherokuの無料プランが終了しconlang portalは閉鎖しました。以降2023-12-24現在までCL-KIITAのdiscordサーバーで佐藤陽花氏が人力でCLA v3を発行しています。"""

md = """
## CLA v3一覧
CLA v3はラテン小文字3字の製作者コード、ラテン小文字3字の語族コード、ラテン小文字2字の言語コード、ラテン小文字2字の方言コードをアンダーバーでつなげた文字列で、例えば雰語上都方言は「jo_fn_fun_kar」というCLA v3コードを持ちます。言語により方言や語族を持たない場合は、代わりにチルダ\~で値を埋めます。 

|user|family|language|dialect|CLA v3|
|---|---|---|---|---|"""
md += dic2md(dic)


clav1 = """シャレイア語 (qixaléh)　xal　zp
ロジバン(lojban)　jbo　lg
クレリカ(qreriqa)　qre　hr
アルテナ語(altenam qeras)　alt　ll
シヴァン(xivan)　xiv　am
アルカ(arka)　ark　rx
(三代目)リパライン語(lineparine)　lpa　lp
ヴェフィス語(四代目リパライン語)(Vaifise)　vef　lp
ワコファル語(wakofal syal)　wkf　ll
イジェール語(Etube Id'erin)　idz　id
トキポナ(toki Pona)　tpn　**
カルコレーシュ語(Calcoradetár)　cal　ca
凪霧（nagili）　alt　rx
モヤシ語（moiacis）　mic　mc
レテシミ語（letesimi）　lsm　mc
ビウ語（biwe）　biw　vl
ヴォレモ（Volxemo）　vlm　vl
レクステンス（lekustens）　lst　ls
フィダーヌス語（Heb Fidana）　fid　ht
ミ・デア語（Żea Mi-Dea）　nkl　md
アポート語（uptohgikulecsepi）　upt　ni
デーレ語（aulakk derle）　del　et
ボウニム語（bohnimik）　bnm　xr
オ゛ェｼﾞｭルニョェーッ語（Ƣeznē'bix）　fez　fb"""

v1dic = [row.split('　') for row in clav1.split('\n')]
v1dic = sorted(v1dic, key=lambda x: x[0])
pprint(v1dic)

md2 = """
## CLA v1一覧  
CLA v1は、ラテン小文字3文字の言語コードと、ラテン文字2文字の語族コードがハイフンでつなげた文字列で、例えばシャレイア語は「xal-zp」というCLA v1コードを持っています(語族コードを持たない言語もあります)。  

|name|CLA v1|  
|---|----|  """
for lang  in v1dic:
    md2+= f'\n|{lang[0]}|{lang[1]}-{lang[2]}|  '

md0 = header + md2 + md


with open("clacode.md", 'w', encoding='utf-8') as file:
    file.write(md0.replace('_',r'\_'))

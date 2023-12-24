
　最新のCLAコードを管理していたconlang portalが2022-11-23に停止してから一年以上CLAコードの登録は人力で行われ、コードの閲覧にはCL-KIITAのdiscordサーバーに参加する必要があり、日本語圏の人工言語の規格として公共性が不十分に感じたので、現在の管理者佐藤陽花氏[@Distr\_to\_Yonder](https://twitter.com/Distr\_to\_Yonder)に許可をもらって一覧記事を作ることにしました。新しい管理システムができるまでのあいだ、コードを簡単に確認するために非公式に設けた仮の一覧であり、登録作業を反映して更新されるわけではないので、最新の情報ではないことに注意してください。根拠となるデータは、CLA v1については[人工言語学wikiの記事](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)、CLA v3についてはCL-KIITAのdiscordにあるconlang portalのログファイル"message.txt"および「各種人工言語コードアナウンス」チャンネルでの手動追加報告です。
## CLAコードとは
　[CLAコード](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)とは、国際的な言語コード[ISO-639](https://ja.wikipedia.org/wiki/ISO\_639)に似せて、日本語圏の人工言語コミュニティーが2015年から発行してきた人工言語の識別符号です。CLAコードには、おかゆ氏の管理していたCLA v1と、そのコードを改良・移管した佐藤陽花氏の管理するCLA v3があります。英語圏の人工言語コミュニティーでは、似た試みとして[kreativekorp.com](https://www.kreativekorp.com/clcr/)が[ISO-639-3](https://ja.wikipedia.org/wiki/ISO\_639-3)互換コードを発行・管理しています。
### CLA v1(2015-07-21から2021-08-03)
　2015-07-21から2021-08-03までのCLA v1はおかゆ氏[@oka\_iu\_tcan](https://twitter.com/oka\_iu\_tcan)によって管理され、google formによる申請フォームから登録申請し、おかゆ氏が手動で登録作業を行い、CLAコードの情報は[人工言語学wikiの記事](https://conlinguistics.fandom.com/ja/wiki/CLA%E3%82%B3%E3%83%BC%E3%83%89)で確認できました。
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
　2021-08-20に、CLA v2をもとに佐藤陽花氏、Ziphil氏、 Xirdim氏,、フルヒト氏を始めとするメンバーによってCLA v3の大枠が[決まり](https://twitter.com/Distr\_to\_Yonder/status/1428400052658053120)、2021-08-31にZiphil氏[@Ziphil](https://twitter.com/Ziphil)によるCLA v3の申請、閲覧サイトであるconlang portalが[開設](https://x.com/Ziphil/status/1432665606034116616?s=20)され、翌2021-09-01にCLA v1の申請受付が[停止されました](https://twitter.com/oka\_iu\_tcan/status/1433031033008525312)。2021-09-02には[CLA v3仕様書](https://github.com/CL-KIITA/CLACode\_SRI/blob/conla/docs/spec/cla\_code.md)が公開されました。
　2021-08-20から2022-11-23までconlang portalでCLA v3を申請し、閲覧することができました。
### CLA v3のCL-KIITA discordサーバー上の手動運用(2022-11-23以降)
　2022-11-23にconlang portalをホスティングしていたherokuの無料プランが終了しconlang portalは閉鎖しました。以降2023-12-24現在までCL-KIITAのdiscordサーバーで佐藤陽花氏が人力でCLA v3を発行しています。
## CLA v1一覧  
CLA v1は、ラテン小文字3文字の言語コードと、ラテン文字2文字の語族コードがハイフンでつなげた文字列で、例えばシャレイア語は「xal-zp」というCLA v1コードを持っています(語族コードを持たない言語もあります)。  

|name|CLA v1|  
|---|----|  
|(三代目)リパライン語(lineparine)|lpa-lp|  
|アポート語（uptohgikulecsepi）|upt-ni|  
|アルカ(arka)|ark-rx|  
|アルテナ語(altenam qeras)|alt-ll|  
|イジェール語(Etube Id'erin)|idz-id|  
|オ゛ェｼﾞｭルニョェーッ語（Ƣeznē'bix）|fez-fb|  
|カルコレーシュ語(Calcoradetár)|cal-ca|  
|クレリカ(qreriqa)|qre-hr|  
|シャレイア語 (qixaléh)|xal-zp|  
|シヴァン(xivan)|xiv-am|  
|デーレ語（aulakk derle）|del-et|  
|トキポナ(toki Pona)|tpn-**|  
|ビウ語（biwe）|biw-vl|  
|フィダーヌス語（Heb Fidana）|fid-ht|  
|ボウニム語（bohnimik）|bnm-xr|  
|ミ・デア語（Żea Mi-Dea）|nkl-md|  
|モヤシ語（moiacis）|mic-mc|  
|レクステンス（lekustens）|lst-ls|  
|レテシミ語（letesimi）|lsm-mc|  
|ロジバン(lojban)|jbo-lg|  
|ワコファル語(wakofal syal)|wkf-ll|  
|ヴェフィス語(四代目リパライン語)(Vaifise)|vef-lp|  
|ヴォレモ（Volxemo）|vlm-vl|  
|凪霧（nagili）|alt-rx|  
## CLA v3一覧
CLA v3はラテン小文字3字の製作者コード、ラテン小文字3字の語族コード、ラテン小文字2字の言語コード、ラテン小文字2字の方言コードをアンダーバーでつなげた文字列で、例えば雰語上都方言は「jo\_fn\_fun\_kar」というCLA v3コードを持ちます。言語により方言や語族を持たない場合は、代わりにチルダ\~で値を埋めます。 

|user|family|language|dialect|CLA v3|
|---|---|---|---|---|
|+merlan #flirora|The conworld that includes Crîþja |Ŋarâþ Crîþ ||~\_nc\_cri\_fli|
|A.I.| |フュトル ||~\_yh\_~\_aii|
|Brxōdƣez, lanva?!|Ƣeznē'bix voб.(オ゛ェｼﾞｭルニョェーッ語族) |Osjernje'bix[bixnē'ex](ウシェルニェク語[方言]) ||~\_os\_fzb\_brl|
|Brxōdƣez, lanva?!|Ƣeznē'bix voб.(オ゛ェｼﾞｭルニョェーッ語族) |Ƣeznē'bix(オ゛ェｼﾞｭルニョェーッ語) ||~\_fz\_fzb\_brl|
|Brxōdƣez, lanva?!|Ƣeznē'bix voб.(オ゛ェｼﾞｭルニョェーッ語族) |Ƣeznē'bix(オ゛ェｼﾞｭルニョェーッ語) |Grwenbixnē'ex(碧雲方言)<北部方言群>|gr\_fz\_fzb\_brl|
|Example Creator(s)|Example Family |Example Language |Example Dialect|dd\_ll\_fff\_ccc|
|Nihil|コルサレス言語群 |ネサルゼルデ語 ||~\_ne\_klt\_nhl|
|Phenyllithium|ウュス語群 |ディミト語/うぐ語 ||~\_dm\_wys\_phe|
|Qunoxts|レミール大陸語族 |ルエン語 ||~\_ln\_lml\_qnt|
|Skytomo||120210823語 ||~\_do\_~\_sky|
|Voidies／kyomu\_aniki|ハン語族 |クァン語 ||~\_kw\_han\_vid|
|Voidies／kyomu\_aniki|ソウキ語族 |ソウキ語 ||~\_sw\_swq\_vid|
|Zaslon| |イジェール語 ||~\_id\_~\_zas|
|Ziphil| |シャレイア語 ||~\_xl\_~\_zph|
|skytomo| |22（国際補助語） ||~\_zz\_~\_sky|
|Лωξիωſ| |クェントーレ語 ʕ Խ̆ωζψo˞ճω-vωζճ ʔ ||~\_qe\_~\_ver|
|かえる|雰語族 |雰語 |上都標準語|jo\_fn\_fun\_kar|
|かえる||TOPUI  ||~\_tp\_~\_kar|
|かえる||雰語上都方言 ||jo\_fn\_fun\_kar|
|かえる||雰語 ||~\_fn\_fun\_kar |
|かえる||雰語 ||~\_pn\_phn\_kar|
|らんべ| |カルコレーシュ語 ||~\_ca\_~\_lmb|
|アルシディア| |アルカ ||~\_as\_~\_arx|
|アルシディア| |凪霧 ||~\_ng\_~\_arx|
|マクェン語| |玄縁語 ||~\_tl\_~\_mqe|
|マクェン語| |マクェン語 ||~\_bm\_~\_mqe|
|ラクシュ語|アルパヌ語 |アルパヌ語 ||~\_au\_aru\_lak|
|ラクシュ語| |ラクシュ語 ||~\_lk\_~\_lak|
|人工言語ランディ| |ランディ ||~\_di\_~\_lan|
|佐藤陽花|Fogiel Group(フォギール語群) |Algelang(アルゲラン) ||~\_al\_fog\_hal|
|佐藤陽花||Inhaik=Ailetphĩna語(𐓮𐓶𐓤𐓙𐓧𐓟 𐒿𐓘̄𐓩𐓶𐓮 𐓮𐓘𐓰𐓙 𐒻𐓩𐓡𐓙𐓤=𐒱𐓧𐓟𐓰𐓬𐓸𐓣̄𐓩𐓘) ||~\_ia\_~\_hal|
|佐藤陽花||オイナルシャルム語(外語; Oinarшalm) ||~\_oi\_~\_hal|
|佐藤陽花||Jejbiq語(Los y'Jejbiq) ||~\_jb\_~\_hal|
|川音リオ|日流語族 |日本語 |川音方言|kn\_ja\_jpx\_kwn|
|暁理|暁錬語族 |暁祖語 |暁国首都弁|go\_gy\_grx\_ghr|
|空気。| |グェーゼル語 |西方方言|we\_gw\_~\_kuk|
|空気。| |グェーゼル語 |東方方言|es\_gw\_~\_kuk|
|総合創作サークル「悠里」|リパラオネ語族 |リパライン語 |現代標準語|nf\_ll\_rfl\_jrl|
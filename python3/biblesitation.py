import re 

vs2book_dict = {
1:'創世',
2:'出エジプト',
3:'レビ',
4:'民数',
5:'申命',
6:'ヨシュア',
7:'裁き人',
8:'ルツ',
9:'サムエル第一',
10:'サムエル第二',
11:'列王第一',
12:'列王第二',
13:'歴代第一',
14:'歴代第二',
15:'エズラ',
16:'ネヘミヤ',
17:'エステル',
18:'ヨブ',
19:'詩編',
20:'格言',
21:'伝道',
22:'ソロモンの歌',
23:'イザヤ',
24:'エレミヤ',
25:'哀歌',
26:'エゼキエル',
27:'ダニエル',
28:'ホセア',
29:'ヨエル',
30:'アモス',
31:'オバデヤ',
32:'ヨナ',
33:'ミカ',
34:'ナホム',
35:'ハバクク',
36:'ゼパニヤ',
37:'ハガイ',
38:'ゼカリヤ',
39:'マラキ',
40:'マタイ',
41:'マルコ',
42:'ルカ',
43:'ヨハネ',
44:'使徒',
45:'ローマ',
46:'コリント第一',
47:'コリント第二',
48:'ガラテア',
49:'エフェソス',
50:'フィリピ',
51:'コロサイ',
52:'テサロニケ第一',
53:'テサロニケ第二',
54:'テモテ第一',
55:'テモテ第二',
56:'テトス',
57:'フィレモン',
58:'ヘブライ',
59:'ヤコブ',
60:'ペテロ第一',
61:'ペテロ第二',
62:'ヨハネ第一',
63:'ヨハネ第二',
64:'ヨハネ第三',
65:'ユダ',
66:'啓示'}


book2vs_dict = {
    '創世': 1,
    '出エジプト': 2,
    'レビ': 3,
    '民数': 4,
    '申命': 5,
    'ヨシュア': 6,
    '裁き人': 7,
    'ルツ': 8,
    'サムエル第一': 9,
    'サムエル第二': 10,
    '列王第一': 11,
    '列王第二': 12,
    '歴代第一': 13,
    '歴代第二': 14,
    'エズラ': 15,
    'ネヘミヤ': 16,
    'エステル': 17,
    'ヨブ': 18,
    '詩編': 19,
    '格言': 20,
    '伝道': 21,
    'ソロモンの歌': 22,
    'イザヤ': 23,
    'エレミヤ': 24,
    '哀歌': 25,
    'エゼキエル': 26,
    'ダニエル': 27,
    'ホセア': 28,
    'ヨエル': 29,
    'アモス': 30,
    'オバデヤ': 31,
    'ヨナ': 32,
    'ミカ': 33,
    'ナホム': 34,
    'ハバクク': 35,
    'ゼパニヤ': 36,
    'ハガイ': 37,
    'ゼカリヤ': 38,
    'マラキ': 39,
    'マタイ': 40,
    'マルコ': 41,
    'ルカ': 42,
    'ヨハネ': 43,
    '使徒': 44,
    'ローマ': 45,
    'コリント第一': 46,
    'コリント第二': 47,
    'ガラテア': 48,
    'エフェソス': 49,
    'フィリピ': 50,
    'コロサイ': 51,
    'テサロニケ第一': 52,
    'テサロニケ第二': 53,
    'テモテ第一': 54,
    'テモテ第二': 55,
    'テトス': 56,
    'フィレモン': 57,
    'ヘブライ': 58,
    'ヤコブ': 59,
    'ペテロ第一': 60,
    'ペテロ第二': 61,
    'ヨハネ第一': 62,
    'ヨハネ第二': 63,
    'ヨハネ第三': 64,
    'ユダ': 65,
    '啓示': 66,
}

prog_bi_01 = re.compile(r'^創$|^創世記$')
prog_bi_02 = re.compile(r'^出$|^出エジプト記$')
prog_bi_03 = re.compile(r'^レビ記$')
prog_bi_04 = re.compile(r'^民$|^民数記$')
prog_bi_05 = re.compile(r'^申$|^申命記$')
prog_bi_06 = re.compile(r'^ヨシ$|^ヨシュ$|^ヨシュア記$')
prog_bi_07 = re.compile(r'^裁$|^裁き人の書$|^士師記$|^士師$')
prog_bi_08 = re.compile(r'^ルツ記$')
prog_bi_09 = re.compile(r'^サムエル記第一$|^サム一$|^サ一$|^サムエル記上$|^サムエル上$|^サム上$|^サ上$|^サムエル記前$|^サムエル前$|^サム前$|^サ前$')
prog_bi_10 = re.compile(r'^サムエル記第二$|^サム二$|^サ二$|^サムエル記下$|^サムエル下$|^サム下$|^サ下$|^サムエル記後$|^サムエル後$|^サム後$|^サ後$')
prog_bi_11 = re.compile(r'^列王記第一$|^王一$|^列王紀上$|^列王上$|^列王紀前$|^列王前$')
prog_bi_12 = re.compile(r'^列王記第二$|^王二$|^列王紀下$|^列王下$|^列王紀後$|^列王後$')
prog_bi_13 = re.compile(r'^歴代誌第一$|^代一$|^歴代志上$|^歴代上$|^歴代志前$|^歴代前$')
prog_bi_14 = re.compile(r'^歴代誌第二$|^代二$|^歴代志下$|^歴代下$|^歴代志後$|^歴代後$')
prog_bi_15 = re.compile(r'^エズ$|^エズラ記$')
prog_bi_16 = re.compile(r'^ネヘ$|^ネヘミヤ記$')
prog_bi_17 = re.compile(r'^エス$|^エステル記$')
prog_bi_18 = re.compile(r'^ヨブ記$')
prog_bi_19 = re.compile(r'^詩$|^詩篇$')
prog_bi_20 = re.compile(r'^格$|^格言の書$|^箴$|^箴言$')
prog_bi_21 = re.compile(r'^伝$|^伝道の書$')
prog_bi_22 = re.compile(r'^ソロ$|^ソロモンの歌$|^雅歌$')
prog_bi_23 = re.compile(r'^イザ$|^イザヤ書$')
prog_bi_24 = re.compile(r'^エレ$|^エレミヤ書$')
prog_bi_25 = re.compile(r'^哀$')
prog_bi_26 = re.compile(r'^エゼ$|^エゼキエル書$')
prog_bi_27 = re.compile(r'^ダニ$|^ダニエル書$')
prog_bi_28 = re.compile(r'^ホセ$|^ホセア書$')
prog_bi_29 = re.compile(r'^ヨエ$|^ヨエル書$')
prog_bi_30 = re.compile(r'^アモ$|^アモス書$')
prog_bi_31 = re.compile(r'^オバ$|^オバデヤ書$')
prog_bi_32 = re.compile(r'^ヨナ書$')
prog_bi_33 = re.compile(r'^ミカ書$')
prog_bi_34 = re.compile(r'^ナホ$|^ナホム書$')
prog_bi_35 = re.compile(r'^ハバ$|^ハバクク書$')
prog_bi_36 = re.compile(r'^ゼパ$|^ゼパニヤ書$')
prog_bi_37 = re.compile(r'^ハガ$|^ハガイ書$')
prog_bi_38 = re.compile(r'^ゼカ$|^ゼカリヤ書$')
prog_bi_39 = re.compile(r'^マラ$|^マラキ書$')
prog_bi_40 = re.compile(r'^マタ$|^マタイによる福音書$|^マタイ伝$')
prog_bi_41 = re.compile(r'^マル$|^マルコによる福音書$|^マルコ伝$')
prog_bi_42 = re.compile(r'^ルカによる福音書$|^ルカ伝$')
prog_bi_43 = re.compile(r'^ヨハ$|^ヨハネによる福音書$|^ヨハネ伝$')
prog_bi_44 = re.compile(r'^使徒の活動$|^使徒行伝$|^使行$')
prog_bi_45 = re.compile(r'^ロマ$|^ローマのクリスチャンへの手紙$|^ローマ人への手紙$')
prog_bi_46 = re.compile(r'^コリントのクリスチャンへの第一の手紙$|^コリ一$|^コ一$|^コリント人への第一の手紙$|^コリント前$')
prog_bi_47 = re.compile(r'^コリントのクリスチャンへの第二の手紙$|^コリ二$|^コ二$|^コリント人への第二の手紙$|^コリント後$')
prog_bi_48 = re.compile(r'^ガラ$|^ガラテアのクリスチャンへの手紙$|^ガラテア人への手紙$|^ガラテヤ人への手紙$|^ガラテヤ$')
prog_bi_49 = re.compile(r'^エフ$|^エフェ$|^エフェソスのクリスチャンへの手紙$|^エフェソス人への手紙$|^エペソ人への手紙$|^エペソ$')
prog_bi_50 = re.compile(r'^フィリ$|^フィリピのクリスチャンへの手紙$|^フィリピ人への手紙$|^ピリピ人への手紙$|^ピリピ$')
prog_bi_51 = re.compile(r'^コロ$|^コロサイのクリスチャンへの手紙$|^コロサイ人への手紙$')
prog_bi_52 = re.compile(r'^テサロニケのクリスチャンへの第一の手紙$|^テサ一$|^テサロニケ人への第一の手紙$|^テサロニケ前$')
prog_bi_53 = re.compile(r'^テサロニケのクリスチャンへの第二の手紙$|^テサ二$|^テサロニケ人への第二の手紙$|^テサロニケ後$')
prog_bi_54 = re.compile(r'^テモテへの第一の手紙$|^テモ一$|^テモテ前$')
prog_bi_55 = re.compile(r'^テモテへの第二の手紙$|^テモ二$|^テモテ後$')
prog_bi_56 = re.compile(r'^テト$|^テトスへの手紙$')
prog_bi_57 = re.compile(r'^フィレ$|^フィレモンへの手紙$|^ピレモンへの手紙$|^ピレモン$')
prog_bi_58 = re.compile(r'^ヘブ$|^ヘブライ人のクリスチャンへの手紙$|^ヘブライ人への手紙$|^ヘブル人への手紙$|^ヘブル$')
prog_bi_59 = re.compile(r'^ヤコ$|^ヤコブの手紙$')
prog_bi_60 = re.compile(r'^ペテロの第一の手紙$|^ペテ一$|^ペ一$|^ペテロ前$')
prog_bi_61 = re.compile(r'^ペテロの第二の手紙$|^ペテ二$|^ペ二$|^ペテロ後$')
prog_bi_62 = re.compile(r'^ヨハネの第一の手紙$|^ヨハ一$|^ヨ一$')
prog_bi_63 = re.compile(r'^ヨハネの第二の手紙$|^ヨハ二$')
prog_bi_64 = re.compile(r'^ヨハネの第三の手紙$|^ヨハ三$|^ヨ三$|^ヨ二$')
prog_bi_65 = re.compile(r'^ユダの手紙$')
prog_bi_66 = re.compile(r'^ヨハネへの啓示$|^啓$|^ヨハネの黙示録$|^黙示録$|^黙示$')

def normalizeBookname(book):
    if prog_bi_01.search(book): result = prog_bi_01.sub('創世', book)
    elif prog_bi_02.search(book): result = prog_bi_02.sub('出エジプト', book)
    elif prog_bi_03.search(book): result = prog_bi_03.sub('レビ', book)
    elif prog_bi_04.search(book): result = prog_bi_04.sub('民数', book)
    elif prog_bi_05.search(book): result = prog_bi_05.sub('申命', book)
    elif prog_bi_06.search(book): result = prog_bi_06.sub('ヨシュア', book)
    elif prog_bi_07.search(book): result = prog_bi_07.sub('裁き人', book)
    elif prog_bi_08.search(book): result = prog_bi_08.sub('ルツ', book)
    elif prog_bi_09.search(book): result = prog_bi_09.sub('サムエル第一', book)
    elif prog_bi_10.search(book): result = prog_bi_10.sub('サムエル第二', book)
    elif prog_bi_11.search(book): result = prog_bi_11.sub('列王第一', book)
    elif prog_bi_12.search(book): result = prog_bi_12.sub('列王第二', book)
    elif prog_bi_13.search(book): result = prog_bi_13.sub('歴代第一', book)
    elif prog_bi_14.search(book): result = prog_bi_14.sub('歴代第二', book)
    elif prog_bi_15.search(book): result = prog_bi_15.sub('エズラ', book)
    elif prog_bi_16.search(book): result = prog_bi_16.sub('ネヘミヤ', book)
    elif prog_bi_17.search(book): result = prog_bi_17.sub('エステル', book)
    elif prog_bi_18.search(book): result = prog_bi_18.sub('ヨブ', book)
    elif prog_bi_19.search(book): result = prog_bi_19.sub('詩編', book)
    elif prog_bi_20.search(book): result = prog_bi_20.sub('格言', book)
    elif prog_bi_21.search(book): result = prog_bi_21.sub('伝道', book)
    elif prog_bi_22.search(book): result = prog_bi_22.sub('ソロモンの歌', book)
    elif prog_bi_23.search(book): result = prog_bi_23.sub('イザヤ', book)
    elif prog_bi_24.search(book): result = prog_bi_24.sub('エレミヤ', book)
    elif prog_bi_25.search(book): result = prog_bi_25.sub('哀歌', book)
    elif prog_bi_26.search(book): result = prog_bi_26.sub('エゼキエル', book)
    elif prog_bi_27.search(book): result = prog_bi_27.sub('ダニエル', book)
    elif prog_bi_28.search(book): result = prog_bi_28.sub('ホセア', book)
    elif prog_bi_29.search(book): result = prog_bi_29.sub('ヨエル', book)
    elif prog_bi_30.search(book): result = prog_bi_30.sub('アモス', book)
    elif prog_bi_31.search(book): result = prog_bi_31.sub('オバデヤ', book)
    elif prog_bi_32.search(book): result = prog_bi_32.sub('ヨナ', book)
    elif prog_bi_33.search(book): result = prog_bi_33.sub('ミカ', book)
    elif prog_bi_34.search(book): result = prog_bi_34.sub('ナホム', book)
    elif prog_bi_35.search(book): result = prog_bi_35.sub('ハバクク', book)
    elif prog_bi_36.search(book): result = prog_bi_36.sub('ゼパニヤ', book)
    elif prog_bi_37.search(book): result = prog_bi_37.sub('ハガイ', book)
    elif prog_bi_38.search(book): result = prog_bi_38.sub('ゼカリヤ', book)
    elif prog_bi_39.search(book): result = prog_bi_39.sub('マラキ', book)
    elif prog_bi_40.search(book): result = prog_bi_40.sub('マタイ', book)
    elif prog_bi_41.search(book): result = prog_bi_41.sub('マルコ', book)
    elif prog_bi_42.search(book): result = prog_bi_42.sub('ルカ', book)
    elif prog_bi_43.search(book): result = prog_bi_43.sub('ヨハネ', book)
    elif prog_bi_44.search(book): result = prog_bi_44.sub('使徒', book)
    elif prog_bi_45.search(book): result = prog_bi_45.sub('ローマ', book)
    elif prog_bi_46.search(book): result = prog_bi_46.sub('コリント第一', book)
    elif prog_bi_47.search(book): result = prog_bi_47.sub('コリント第二', book)
    elif prog_bi_48.search(book): result = prog_bi_48.sub('ガラテア', book)
    elif prog_bi_49.search(book): result = prog_bi_49.sub('エフェソス', book)
    elif prog_bi_50.search(book): result = prog_bi_50.sub('フィリピ', book)
    elif prog_bi_51.search(book): result = prog_bi_51.sub('コロサイ', book)
    elif prog_bi_52.search(book): result = prog_bi_52.sub('テサロニケ第一', book)
    elif prog_bi_53.search(book): result = prog_bi_53.sub('テサロニケ第二', book)
    elif prog_bi_54.search(book): result = prog_bi_54.sub('テモテ第一', book)
    elif prog_bi_55.search(book): result = prog_bi_55.sub('テモテ第二', book)
    elif prog_bi_56.search(book): result = prog_bi_56.sub('テトス', book)
    elif prog_bi_57.search(book): result = prog_bi_57.sub('フィレモン', book)
    elif prog_bi_58.search(book): result = prog_bi_58.sub('ヘブライ', book)
    elif prog_bi_59.search(book): result = prog_bi_59.sub('ヤコブ', book)
    elif prog_bi_60.search(book): result = prog_bi_60.sub('ペテロ第一', book)
    elif prog_bi_61.search(book): result = prog_bi_61.sub('ペテロ第二', book)
    elif prog_bi_62.search(book): result = prog_bi_62.sub('ヨハネ第一', book)
    elif prog_bi_63.search(book): result = prog_bi_63.sub('ヨハネ第二', book)
    elif prog_bi_64.search(book): result = prog_bi_64.sub('ヨハネ第三', book)
    elif prog_bi_65.search(book): result = prog_bi_65.sub('ユダ', book)
    elif prog_bi_66.search(book): result = prog_bi_66.sub('啓示', book)
    else : result = book
    
    return result

BOOKS = r'(アモ|アモス|アモス書|イザ|イザヤ|イザヤ書|エス|エステル|エステル記|エズ|エズラ|エズラ記|エゼ|エゼキエル|エゼキエル書|エフ|エフェ|エフェソス|エフェソスのクリスチャンへの手紙|エレ|エレミヤ|エレミヤ書|オバ|オバデヤ|オバデヤ書|ガラ|ガラテア|ガラテアのクリスチャンへの手紙|コリントのクリスチャンへの第一の手紙|コリントのクリスチャンへの第二の手紙|コリント第一|コリント第二|コリ一|コリ二|コロ|コロサイ|コロサイのクリスチャンへの手紙|コ一|コ二|サムエル記第一|サムエル記第二|サムエル第一|サムエル第二|サム一|サム二|サ一|サ二|ゼカ|ゼカリヤ|ゼカリヤ書|ゼパ|ゼパニヤ|ゼパニヤ書|ソロ|ソロモンの歌|ソロモンの歌|ダニ|ダニエル|ダニエル書|テサロニケのクリスチャンへの第一の手紙|テサロニケのクリスチャンへの第二の手紙|テサロニケ第一|テサロニケ第二|テサ一|テサ二|テト|テトス|テトスへの手紙|テモテへの第一の手紙|テモテへの第二の手紙|テモテ第一|テモテ第二|テモ一|テモ二|ナホ|ナホム|ナホム書|ネヘ|ネヘミヤ|ネヘミヤ記|ハガ|ハガイ|ハガイ書|ハバ|ハバクク|ハバクク書|フィリ|フィリピ|フィリピのクリスチャンへの手紙|フィレ|フィレモン|フィレモンへの手紙|ヘブ|ヘブライ|ヘブライ人のクリスチャンへの手紙|ペテロの第一の手紙|ペテロの第二の手紙|ペテロ第一|ペテロ第二|ペテ一|ペテ二|ペ一|ペ二|ホセ|ホセア|ホセア書|マタ|マタイ|マタイによる福音書|マラ|マラキ|マラキ書|マル|マルコ|マルコによる福音書|ミカ|ミカ書|ヤコ|ヤコブ|ヤコブの手紙|ユダ|ユダの手紙|ヨエ|ヨエル|ヨエル書|ヨシ|ヨシュ|ヨシュア|ヨシュア記|ヨナ|ヨナ書|ヨハ|ヨハネ|ヨハネによる福音書|ヨハネの第一の手紙|ヨハネの第三の手紙|ヨハネの第二の手紙|ヨハネへの啓示|ヨハネ第一|ヨハネ第三|ヨハネ第二|ヨハ一|ヨハ三|ヨハ二|ヨブ|ヨブ記|ヨ一|ヨ三|ヨ二|ルカ|ルカによる福音書|ルツ|ルツ記|レビ|レビ記|ロマ|ローマ|ローマのクリスチャンへの手紙|代一|代二|伝|伝道|伝道の書|使徒|使徒の活動|出|出エジプト|出エジプト記|列王第一|列王第二|列王記第一|列王記第二|創|創世|創世記|哀|哀歌|啓|啓示|格|格言|格言の書|歴代第一|歴代第二|歴代誌第一|歴代誌第二|民|民数|民数記|王一|王二|申|申命|申命記|裁|裁き人|裁き人の書|詩|詩編|箴|箴言|ローマ人への手紙|コリント人への第一の手紙|コリント人への第二の手紙|ガラテア人への手紙|エフェソス人への手紙|フィリピ人への手紙|コロサイ人への手紙|テサロニケ人への第一の手紙|テサロニケ人への第二の手紙|ヘブライ人への手紙|士師記|士師|サムエル記上|サムエル記下|サムエル上|サムエル下|サムエル記前|サムエル記後|サムエル前|サムエル後|列王紀上|列王紀下|列王上|列王下|列王紀前|列王紀後|列王前|列王後|歴代志上|歴代志下|歴代上|歴代下|歴代志前|歴代志後|歴代前|歴代後|詩篇|雅歌|マタイ伝|マルコ伝|ルカ伝|ヨハネ伝|使徒行伝|使行|コリント前|コリント後|テサロニケ前|テサロニケ後|テモテ前|テモテ後|ペテロ前|ペテロ後|ガラテヤ人への手紙|ガラテヤ|エペソ人への手紙|エペソ|ピリピ人への手紙|ピリピ|ピレモンへの手紙|ピレモン|ヘブル人への手紙|ヘブル|ヨハネの黙示録|黙示録|黙示|サム上|サ上|サム下|サ下|サム前|サ前|サム後|サ後|)'

# 1章のみの書のためのパターンマッチ:
# 本文中の "ヨハネ第二 3節" 等のマッチを避けるため、短縮形のみに
BOOKS_sp1 = r'(オバ|フィレ|ユダ|ヨハ三|ヨハ二)'

BOOKS_sp2 = r'(オバ|オバデヤ|オバデヤ書|フィレ|フィレモン|フィレモンへの手紙|ユダ|ユダの手紙|ヨハネの第三の手紙|ヨハネの第二の手紙|ヨハネ第三|ヨハネ第二|ヨハ三|ヨハ二)'

PATTERN_A = r"((%s)( |（)(\d+):(\d+)(((，|, ?)\d+)*(-\d+)*)*(; (\d+):(\d+)(((，|, ?)\d+)*(-\d+)*)*)*)"%(BOOKS)
PATTERN_A_sp = r"((%s)( |（)(\d+)(?!節)(((，|, ?)\d+)*(-\d+)*)*(; (\d+):(\d+)(((，|, ?)\d+)*(-\d+)*)*)*)"%(BOOKS_sp1)

PATTERN_B = r"((%s)( |（)((\d+)(章|編)\[?(\d+)節?\]?，?)*(((，|と|, )\d+)*((-|から)\d+)*)*節\]?((; |，|, |と|や|または?)*(\d+)(章|編)\[?(\d+)((，\d+)*((-|から)\d+)*)*節?\]?)*)"%(BOOKS)
PATTERN_B_sp =          r"((%s)( |（)(\[?(\d+)節?\]?，?)*(((，|と|, )\d+)*((-|から)\d+)*)*節\]?((; |，|, |と|や|または?)*(\d+)(章|編)\[?(\d+)((，\d+)*((-|から)\d+)*)*節?\]?)*)"%(BOOKS_sp2)

prog_A = re.compile(PATTERN_A)
prog_A_sp = re.compile(PATTERN_A_sp)
prog_B = re.compile(PATTERN_B)
prog_B_sp = re.compile(PATTERN_B_sp)
prog_C = re.compile(r'^\d+$')  # 最もシンプルな形 47 のみとマッチ
prog_D = re.compile(r'^\d+(，\d+)+$')  # 複数形式 マタイ 47, 49, 50 とマッチ
prog_E = re.compile(r'^\d+-\d+$')  # 複数形式 マタイ 10:47-50 とマッチ
prog_F1 = re.compile(r'^\d+(，\d+)+(，\d+-\d+)+(，\d+)*$') # 10:1,10,18-21　とマッチ
prog_F2 = re.compile(r'^\d+(，\d+-\d+)+(，\d+)+(，\d+-\d+)*$') # 10:1-10,1,2,3,
prog_F3 = re.compile(r'^(\d+-\d+)(，\d+-\d+)+$') # 10:1-10,1-10
prog_F4 = re.compile(r'^(\d+-\d+)(，\d+-\d+)*(，\d+)*(，\d+-\d+)*$') # 10:1-10,1-10
prog_F5 = re.compile(r'^\d+(，\d+-\d+)*(，\d+)*$') # 10:1-10,1-10

prog_0 = re.compile(r'[:\-，]')
prog_1 = re.compile(r'[;]')
prog_cap = re.compile(r'[: ]')

prog_ex1 = re.compile(r'，(\d+章)')

prog_DeniteBible = re.compile(r'^\d+((, ?|-)\d+)+$')

def citation_character(text):
    # マタイ 10章47節等の形式
    # 引数：テキスト
    # 返り値: リスト[ばらばらになった書 章:節] 
    #  m1 => マタ 10章47節 等の形式
    #  m2 => 1章のみの聖句の検出

    m1 = prog_B.findall(text)
    m2 = prog_B_sp.findall(text)

    result = []
    result += [k[0].replace("編",":").replace("章",":").replace("節","").replace("から","-").replace("と","; ").replace("[","").replace("]","").replace("詩:","詩編").replace("（"," ") for k in m1]
    #result += [k[0] for k in m1]
    result += [k[0].replace("編",":").replace("章",":").replace("節","").replace("から","-").replace("と","; ").replace("[","").replace("]","").replace("詩:","詩編").replace("（"," ") for k in m2]

    return result

def citation_symbole(text):
    # マタ 10:47 等の形式
    # 引数：テキスト
    # 返り値: リスト[ばらばらになった書 章:節] 
    #  m1 => マタ 10:47 等の形式
    #  m2 => 1章のみの聖句の検出

    m1 = prog_A.findall(text)
    m2 = prog_A_sp.findall(text)

    result = []
    result += [k[0].replace("（"," ") for k in m1]
    result += [k[0].replace("（"," ") for k in m2]
    return result

def splitVerse(nml_bookname,cap,v4):
    result = []
    if prog_C.match(v4):# 最もシンプルな形 マタイ 10:47 のみとマッチ
        result.append(nml_bookname + " " + cap + ":" + v4)
    
    # カンマで区切られた形 マタイ 10:48, 49 にマッチ
    elif prog_D.match(v4):
        for v in v4.split("，"):
            result.append(nml_bookname + " " + cap + ":" + v)
    
    # ハイフンで区切られた形　マタイ 10:21-23にマッチ
    elif prog_E.match(v4):
        txt1 = int(v4.split("-")[0])
        txt2 = int(v4.split("-")[1])
        count = txt2 - txt1
        for i in range(count + 1):
            result.append(nml_bookname + " " + cap + ":" + str(txt1 + i))

    # セミコロンで区切られた形に対応
    elif prog_F1.match(v4) or prog_F2.match(v4) or prog_F3.match(v4) or prog_F4.match(v4) or prog_F5.match(v4):
        for v5 in v4.split("，"):
            if prog_C.match(v5):# 最もシンプルな形 マタイ 10:47 のみとマッチ
                result.append(nml_bookname + " " + cap + ":" + v5)

            # ハイフンで区切られた形　マタイ 10:21-23にマッチ
            elif prog_E.match(v5):
                txt1 = int(v5.split("-")[0])
                txt2 = int(v5.split("-")[1])
                count = txt2 - txt1
                for i in range(count + 1):
                    result.append(nml_bookname + " " + cap + ":" + str(txt1 + i))

    elif prog_DeniteBible.match(v4):
        for v in v4.split(","):
            v = v.strip()

            if prog_C.match(v):# 最もシンプルな形 マタイ 10:47 のみとマッチ
                result.append(nml_bookname + " " + cap + ":" + v)

            # ハイフンで区切られた形　マタイ 10:21-23にマッチ
            elif prog_E.match(v):
                txt1 = int(v.split("-")[0])
                txt2 = int(v.split("-")[1])
                count = txt2 - txt1
                for i in range(count + 1):
                    result.append(nml_bookname + " " + cap + ":" + str(txt1 + i))
        #result.append(nml_bookname + " " + cap + ":" + v)

    else:
        return ["************",nml_bookname,cap,v4, "*****************"]
    
    return result

#'ヨハ 3:13; 6:38，62; 8:23，42，58'
def citationRange(bible_tx):
    bookname, vs1 = bible_tx.split(" ",1)
    nml_bookname = normalizeBookname(bookname)
    vs2 = vs1.split("; ")
    result = []
    for v3 in vs2:
        if len(v3.split(":")) == 2:
            cap, v4 = v3.split(":")
            result += splitVerse(nml_bookname,cap,v4)
        elif len(v3.split(":")) == 1:
            result += splitVerse(nml_bookname, "1",v3)
        else:
            result += ["******" + nml_bookname + " " + v3]
    return result

def citation_text(text):
    bibles = []
    result = []
    bibles += citation_symbole(text)
    bibles += citation_character(text)
    for bible_tx in bibles: 
        result += citationRange(bible_tx)
    return result


def vs2str(vs):
    # 66001001 という文字列を 啓示 1:1 に変換する
    # 文字列formatに対応しているため バッファ表示用
    varse = int(vs[-3:])
    chapter = int(vs[-6:-3])
    book = int(vs[:-6])

    #txt = '"'+vs2book_dict[int(book)]+" "+ str(chapter) +":"+ str(varse)+'"'
    txt = f'{vs2book_dict[int(book)]} {str(chapter)}:{str(varse)}'
    formated_txt = f'{txt:<20}'
    return formated_txt
    
def vs2str_ref(vs, ref_text):
    # 66001001 という文字列を 啓示 1:1 に変換する
    # 文字列formatに対応しているため バッファ表示用
    varse = int(vs[-3:])
    chapter = int(vs[-6:-3])
    book = int(vs[:-6])

    #txt = '"'+vs2book_dict[int(book)]+" "+ str(chapter) +":"+ str(varse)+'"'
    txt = f'{vs2book_dict[int(book)]} {str(chapter)}:{str(varse)} {ref_text}'
    formated_txt = f'{txt:<18}'
    return formated_txt

def str2vs_chapter_range(str_bi):
    chapter = str_bi.split(' ')[1].zfill(3)
    book = book2vs_dict[str_bi.split(' ')[0]]

    start_addr = f'{book}{chapter}000'
    end_addr   = f'{book}{chapter}999'

    return start_addr + '-' + end_addr

def str2vs(str_bi):
    book = book2vs_dict[str_bi.split(' ')[0]]
    chapter,verse = str_bi.split(' ')[1].split(':')
    result = f'{book}{int(chapter):03d}{int(verse):03d}'
    return result

#filepath = sys.argv[1]
#file = open(filepath)
#soup = BeautifulSoup(file, 'html.parser')
#
#pub_id = os.path.basename(filepath)
#article = soup.find('article')
##text = article.get_text()
#
#for p in article.find_all('p'):
#    output=""
#    bibles=[]
#
#    data_pid = p["data-pid"]
#    url = r"https://wol.jw.org/ja/wol/d/r7/lp-j/" + pub_id + r"#h=" + data_pid
#    text = p.get_text()
#    text.replace('\u200b','')
#
#    #text = "マタ 13:21，22，38-42; 21:42-44; 23:33; ユダ 15，16，31"
#
#    bibles += citation_symbole(text)
#    bibles += citation_character(text)
#    for bible_tx in bibles: 
#        bible = citationRange(bible_tx)
#        for b in bible:
#            output = '"{0}","{1}","{2}","{3}","{4}"'.format(pub_id,b,data_pid,text,url)
#            print(output)


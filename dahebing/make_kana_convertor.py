def _make_kana_convertor(text1):#可以把英语字母转化为片假名
    """ひらがな⇔カタカナ変換器を作る"""
    import re
    text2 = text1
    kata = {
        'A': 'エイ', 'a': 'エイ','B': 'ビー', 'b': 'ビー', 'C': 'シー',
        'c': 'シー', 'D': 'ディー', 'd': 'ディー', 'E': 'イー', 'e': 'イー',
        'F': 'エフ', 'f': 'エフ', 'G': 'ジー', 'g': 'ジー', 'H': 'エッチ',
        'h': 'エッチ', 'I': 'アイ', 'i': 'アイ', 'J': 'ジェイ', 'j': 'ジェイ',
        'K': 'ケイ', 'k': 'ケイ', 'L': 'エル', 'l': 'エル', 'M': 'エム',
        'm': 'エム', 'N': 'エヌ', 'n': 'エヌ', 'O': 'オー', 'o': 'オー',
        'P': 'ピー', 'p': 'ピー', 'Q': 'キュー', 'q': 'キュー', 'R': 'アール',
        'r': 'アール', 'S': 'エス', 's': 'エス', 'T': 'ティー', 't': 'ティー',
        'U': 'ユー', 'u': 'ユー', 'V': 'ブイ', 'v': 'ブイ', 'W': 'ダブリュー',
        'w': 'ダブリュー','X': 'エックス', 'x': 'エックス', 'Y': 'ワイ', 'y': 'ワイ',
        'Z': 'ズィー','z': 'ズィー','〇':'レイ','ω':'オメガ'
    }

    # ひらがな → カタカナ のディクショナリをつくる
    hira = dict([(v, k) for k, v in kata.items()])

    re_hira2kata = re.compile("|".join(map(re.escape, hira)))
    re_kata2hira = re.compile("|".join(map(re.escape, kata)))

    def _hiragana2katakana(text2):
        return re_hira2kata.sub(lambda x: hira[x.group(0)], text2)

    def _katakana2hiragana(text2):
        return re_kata2hira.sub(lambda x: kata[x.group(0)], text2)

    return _katakana2hiragana(text2)
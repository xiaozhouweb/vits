
from pypinyin import pinyin, Style
from pypinyin.style._utils import get_finals, get_initials


def chinese_cleaners2(text):
    temp = " ".join([
        p
        for phone in pinyin(text, style=Style.TONE3, v_to_u=True)
        for p in [
            get_initials(phone[0], strict=True),
            get_finals(phone[0][:-1], strict=True) + phone[0][-1]
            if phone[0][-1].isdigit()
            else get_finals(phone[0], strict=True)
            if phone[0][-1].isalnum()
            else phone[0],
        ]
        if len(p) != 0 and not p.isdigit()
    ])
    p = []
    for t in temp:
        if t not in """ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;:,.!?¡¿—…"«»“” _0123456789""":
            if t in '，。！？':
                if t == '，':
                    t = ','
                if t == '。':
                    t = '.'
                if t == '！':
                    t = '!'
                if t == '？':
                    t = '?'
                p.append(t)
            continue
        p.append(t)
    return ''.join(p)

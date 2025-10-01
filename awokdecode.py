import os, re

path = "/home/jiyel/15/unz/awok.txt"
out_dir = "/home/jiyel/15/unz"
out_path = os.path.join(out_dir, "decoded_concat.txt")

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

hex_matches = re.findall(r'HID Data:\s*([0-9A-Fa-f\s:]+)', data)
print("Found", len(hex_matches), "HID Data entries")

def parse_hex(hs):
    s = hs.replace("0x","").replace(":"," ").strip()
    parts = re.split(r'[\s]+', s)
    parts = [p for p in parts if p != '']
    if len(parts) == 1 and len(parts[0]) % 2 == 0 and len(parts[0]) > 2:
        p = parts[0]
        parts = [p[i:i+2] for i in range(0, len(p), 2)]
    try:
        return [int(x,16) for x in parts]
    except:
        return []

HID = {
    4:'a',5:'b',6:'c',7:'d',8:'e',9:'f',10:'g',11:'h',12:'i',13:'j',14:'k',15:'l',
    16:'m',17:'n',18:'o',19:'p',20:'q',21:'r',22:'s',23:'t',24:'u',25:'v',26:'w',27:'x',28:'y',29:'z',
    30:'1',31:'2',32:'3',33:'4',34:'5',35:'6',36:'7',37:'8',38:'9',39:'0',
    40:'\n',41:'[ESC]',42:'[BACKSPACE]',43:'[TAB]',44:' ',
    45:'-',46:'=',47:'[',48:']',49:'\\',50:'#',51:';',52:"'",53:'`',54:',',55:'.',56:'/'
}
HID_SHIFT = {
    4:'A',5:'B',6:'C',7:'D',8:'E',9:'F',10:'G',11:'H',12:'I',13:'J',14:'K',15:'L',
    16:'M',17:'N',18:'O',19:'P',20:'Q',21:'R',22:'S',23:'T',24:'U',25:'V',26:'W',27:'X',28:'Y',29:'Z',
    30:'!',31:'@',32:'#',33:'$',34:'%',35:'^',36:'&',37:'*',38:'(',39:')',
    45:'_',46:'+',47:'{',48:'}',49:'|',50:'~',51:':',52:'"',54:'<',55:'>',56:'?'
}

decoded_chunks = []

for hm in hex_matches:
    bytes_list = parse_hex(hm)
    if not bytes_list:
        continue
    if len(bytes_list) >= 8:
        window = bytes_list[:8]
        if window[1] == 0x00:
            mod = window[0]
            keycodes = window[2:8]
            shift = bool(mod & 0x02 or mod & 0x20)
            s = ""
            for kc in keycodes:
                if kc == 0: continue
                if shift:
                    s += HID_SHIFT.get(kc, HID.get(kc, ''))
                else:
                    s += HID.get(kc, '')
            if s:
                decoded_chunks.append(s)

joined = "".join(decoded_chunks)
joined_nosp = joined.replace(" ", "").replace("\t", "").replace("\n", "")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(joined_nosp)

print("Decoded chunks count:", len(decoded_chunks))
print("Final length (no spaces):", len(joined_nosp))
print("Saved to:", out_path)
print("Result preview:", joined_nosp[:100])

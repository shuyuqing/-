import re
import pykakasi #把平假名或片假名转化为读音


# m = re.match(r"(?P<first_name>\w+)(?P<last_name>\w+)", "Malcolm Reynolds")
# # m = re.match(r"\w+", "Malcolm Reynolds")
#
# a = m.group('first_name')
#
# b = m.group('last_name')
#
# c = m.group(1)
#
# print(c)

# a = 2
# b = 5
#
# for i in range(b):
#
#     print(i)

# a = 'abc'
# b = 'ab'
# c = 'abc'
#
# print(a[0])
# print(a[-1])

kakasi = pykakasi.kakasi()
kakasi.setMode("H", "a")  # Hiragana to ascii, default: no conversion
kakasi.setMode("K", "a")  # Katakana to ascii, default: no conversion
kakasi.setMode("J", "a")  # Japanese to ascii, default: no conversion
kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
kakasi.setMode("s", True)  # add space, default: no separator
conv = kakasi.getConverter()


a ='衆参'

print(conv.do(a))


# a = 'sp_S-a_B+n_I[sp-a_B+n_B]'
# b = a.replace(re.findall(r'\[.*\]',a)[0], '')
# print(b)
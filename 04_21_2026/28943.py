import re

with open("24_28943.txt") as f:
    s = f.read().strip()

split = re.split(r"[AEOUIY]", s)

m_len = 100_000_000
for i, subs in enumerate(split):
    if subs.count('20') < 26:
        continue
    if subs.count('20') == 26:
        m_len = min(m_len, len(subs[subs.find('20') + 2:]) + 1)
    if subs.count("20") > 26:
        subs1 = subs.split('20')[-26:]
        m_len = min(m_len, len('20'.join(subs1)) + 3)

print(m_len)

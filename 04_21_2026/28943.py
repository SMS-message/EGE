import re
import time

with open("24_28943.txt") as f:
    s = f.read().strip()


def first():
    split = re.split(r"[AEOUIY]", s)

    m_len = 100_000_000
    for subs in split:
        if subs.count('20') < 26:
            continue
        if subs.count('20') == 26:
            m_len = min(m_len, len(subs[subs.find('20') + 2:]) + 1)
        if subs.count("20") > 26:
            subs1 = subs.split('20')[-26:]
            m_len = min(m_len, len('20'.join(subs1)) + 3)
    print(m_len)

def second():
    vow = "AEIOUY"
    m_len = 100_000_000
    for i in range(len(s) - 53):
        for j in range(i + 53, len(s)):
            v = [x for x in s[i:j] if x in vow]
            if len(v) > 1:
                break
            if len(s[i:j]) > m_len:
                break
            if s[i:j][-1] not in vow:
                continue
            if s[i:j].count("20") == 26:
                m_len = min(m_len, len(s[i:j]))
                print(m_len)
    print(m_len)


def third():
    split = re.split(r"[AEIOUY]", s)
    m_len = 100_000_000
    for subs in split:
        if subs.count("20") < 26:
            continue
        elif subs.count("20") == 26:
            m_len = min(m_len, len(subs) + 1)
        else:
            for i in range(len(subs) - 53, -1, -1):
                if len(subs[i:]) > m_len:
                    break
                if subs[i:].count("20") == 26:
                    m_len = min(m_len, len(subs[i:]) + 1)
                    s1 = subs[i:]
    print(m_len)

if __name__ == '__main__':
    third()
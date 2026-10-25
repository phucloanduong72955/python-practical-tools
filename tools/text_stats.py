#!/usr/bin/env python3
"""统计文本。用法: python3 text_stats.py <文件>"""
import sys, re
from collections import Counter
def main():
    t=Path_text=open(sys.argv[1],encoding='utf-8').read()
    words=re.findall(r'\w+', t.lower())
    print(f"字符: {len(t)} 行: {t.count(chr(10))+1} 词: {len(words)}")
    print('高频词:', Counter(words).most_common(10))
if __name__=='__main__': main()

#!/usr/bin/env python3
"""按内容找重复文件，只列出不删除。用法: python3 find_duplicates.py <目录>"""
import hashlib, sys
from pathlib import Path
from collections import defaultdict
def h(f):
    m=hashlib.sha256()
    with open(f,'rb') as fh:
        for b in iter(lambda: fh.read(8192), b''): m.update(b)
    return m.hexdigest()
def main():
    groups=defaultdict(list)
    for f in Path(sys.argv[1]).rglob('*'):
        if f.is_file(): groups[h(f)].append(str(f))
    for files in groups.values():
        if len(files)>1: print('重复:'); [print(' ',x) for x in files]
if __name__=='__main__': main()

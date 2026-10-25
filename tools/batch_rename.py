#!/usr/bin/env python3
"""批量改名。用法: python3 batch_rename.py <目录> --prefix IMG_ --start 1"""
import argparse
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('dir'); p.add_argument('--prefix',default=''); p.add_argument('--start',type=int,default=1); a=p.parse_args()
    files=sorted([f for f in Path(a.dir).iterdir() if f.is_file()])
    for i,f in enumerate(files, start=a.start):
        new=f.with_name(f"{a.prefix}{i:03d}{f.suffix}")
        print(f"{f.name} -> {new.name}"); f.rename(new)
if __name__=='__main__': main()

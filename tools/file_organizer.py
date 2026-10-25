#!/usr/bin/env python3
"""按扩展名整理文件夹。用法: python3 file_organizer.py <目录> [--dry-run]"""
import argparse, shutil
from pathlib import Path
MAP={'.jpg':'图片','.png':'图片','.mp4':'视频','.mp3':'音频','.pdf':'文档','.docx':'文档','.txt':'文档','.zip':'压缩包'}
def main():
    p=argparse.ArgumentParser(); p.add_argument('dir'); p.add_argument('--dry-run',action='store_true'); a=p.parse_args()
    d=Path(a.dir)
    for f in d.iterdir():
        if f.is_file() and f.suffix.lower() in MAP:
            dest=d/MAP[f.suffix.lower()]/f.name
            print(('预览: ' if a.dry_run else '移动: ')+f"{f.name} -> {dest}")
            if not a.dry_run:
                dest.parent.mkdir(exist_ok=True); shutil.move(str(f),str(dest))
if __name__=='__main__': main()

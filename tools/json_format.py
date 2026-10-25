#!/usr/bin/env python3
"""格式化JSON。用法: python3 json_format.py <文件.json>"""
import sys, json
def main():
    data=json.load(open(sys.argv[1],encoding='utf-8'))
    print(json.dumps(data, ensure_ascii=False, indent=2))
if __name__=='__main__': main()

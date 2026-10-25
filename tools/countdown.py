#!/usr/bin/env python3
"""倒计时。用法: python3 countdown.py 25  (分钟)"""
import sys, time
def main():
    mins=int(sys.argv[1]) if len(sys.argv)>1 else 25
    for s in range(mins*60,0,-1):
        print(f"\r剩余 {s//60:02d}:{s%60:02d}", end='', flush=True); time.sleep(1)
    print("\n时间到！")
if __name__=='__main__': main()

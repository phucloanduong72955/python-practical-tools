#!/usr/bin/env python3
"""生成强密码。用法: python3 password_generator.py --length 16"""
import argparse, secrets, string
def main():
    p=argparse.ArgumentParser(); p.add_argument('--length',type=int,default=16); a=p.parse_args()
    chars=string.ascii_letters+string.digits+'!@#$%^&*'
    print(''.join(secrets.choice(chars) for _ in range(a.length)))
if __name__=='__main__': main()

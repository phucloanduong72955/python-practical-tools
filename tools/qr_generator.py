#!/usr/bin/env python3
"""生成二维码图片（需 qrcode 库）。用法: python3 qr_generator.py "https://example.com" out.png"""
import sys
try:
    import qrcode
except ImportError:
    print("请先安装: pip install qrcode[pil]"); sys.exit(1)
img=qrcode.make(sys.argv[1]); img.save(sys.argv[2] if len(sys.argv)>2 else "qr.png"); print("已生成")

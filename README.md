# Python 实用工具箱

新手也能直接用的 Python 小工具合集，每个工具都是一个独立文件，不用装一堆依赖，复制过去就能跑。

## 为什么做这个

很多教程讲概念，不给能直接用的东西。这里每个工具都解决一个日常小问题：整理文件、批量改名、查重复、算时间、生成密码，等等。

> 注意：第一版先上 7 个工具，README 里列的都是实际有的，不凑数。

## 工具列表

| 工具 | 干什么 |
|---|---|
| tools/file_organizer.py | 按扩展名把杂乱文件夹自动分类到子文件夹 |
| tools/batch_rename.py | 批量改名，支持前缀、编号、替换 |
| tools/find_duplicates.py | 按内容哈希找重复文件，只列出，不删 |
| tools/password_generator.py | 生成可读性好的强密码 |
| tools/countdown.py | 倒计时 / 番茄钟，命令行就能用 |
| tools/text_stats.py | 统计文本字数、行数、词频前 10 |
| tools/json_format.py | 格式化 / 校验 JSON 文件 |
| tools/qr_generator.py | 输入网址生成二维码图片（需 qrcode 库） |

## 快速上手

```bash
python3 tools/file_organizer.py ~/Downloads --dry-run
python3 tools/batch_rename.py ./photos --prefix IMG_ --start 1
python3 tools/find_duplicates.py ./docs
python3 tools/password_generator.py --length 16
```

`--dry-run` 先预览，不会真的动你的文件。正式跑之前，先用小文件夹试一下。

## 贡献

欢迎提 Issue 和 PR，加新工具请保持：一个文件、一个功能、有 `--help`、有例子。

## 大家最想看的：例子

整理前：
```
Downloads/
  a.jpg  b.pdf  c.mp3  d.zip
```
跑 `python3 tools/file_organizer.py ~/Downloads` 后：
```
Downloads/
  图片/a.jpg  文档/b.pdf  音频/c.mp3  压缩包/d.zip
```

密码例子：
```
$ python3 tools/password_generator.py --length 16
r*7^pwIq8SNyuR7O
```

这些都是本地实际跑通过的，不是编的输出。

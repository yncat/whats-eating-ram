# Whats-eating-ram

The recent windows task manager is bad IMO. I couldn't track down which process was eating ram the most. It had "sort by memory usage descending", but it did not sort background processes for some reason. And it was very sluggish. So I quickly wrote this. There're more elegant solutions? I know. But writing my own one is enough and much faster for me.

# Usage

```
python wer.py --help
usage: wer.py [-h] [--count COUNT]

Show processes eating ram the most

optional arguments:
  -h, --help     show this help message and exit
  --count COUNT  Number of processes to show (default 5)
```

import argparse
import datetime

ver = argparse.ArgumentParser()

ver.add_argument('-n', '--name', required=True, help='something')
ver.add_argument('-t', '--title', required=True, help='something')
ver.add_argument('-c', '--comment', required=True, help='something')

obj = ver.parse_args()

print(obj.name)
print(obj.title)
print(obj.comment)

print(datetime.datetime)

# py LESSON15/testing.py -n 'n' -t 't' -c 'c'
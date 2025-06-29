import argparse

value = argparse.ArgumentParser()

value.add_argument(
    '-n', '--name', required=True,
    help='Type your name'
)

obj = value.parse_args()

name = obj.name

# py LESSON16/Paper.py -n 'me'
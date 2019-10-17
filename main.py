import os

filename = 'text.txt'

if __name__ == '__main__':
    with os.open(filename, 'w') as fh:
        fh.write('b')

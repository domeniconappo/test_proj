import os

if __name__ == '__main__':
    with os.open('test.txt', 'w') as f:
        f.write('a')

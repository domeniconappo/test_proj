import os


if __name__ == '__main__':
    if not os.path.exists('./output'):
        os.mkdir('./output')
    with open('./output/text.txt', 'w') as fh:
        fh.write('D')

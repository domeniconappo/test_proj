import os


if __name__ == '__main__':
    if not os.path.exists('./output'):
        os.mkdir('./output')
    fh = open('./output/text.txt', 'w')
    fh.write('c')
    fh.close()

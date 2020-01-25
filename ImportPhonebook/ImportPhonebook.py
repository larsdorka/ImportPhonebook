import argparse


# main application
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CVS netphone phonebooks into XML import file')
    parser.add_argument('-i', help='csv file of internal entries')
    parser.add_argument('-e', help='csv file of external entries')
    parser.add_argument('-o', help='file to store the xml output in')
    parser.print_help()

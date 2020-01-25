import argparse
import csv


# main application
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CVS netphone phonebooks into XML import file')
    parser.add_argument('-i', help='csv file of internal entries')
    parser.add_argument('-e', help='csv file of external entries')
    parser.add_argument('-o', help='file to store the xml output in')
    parser.print_help()
    args = parser.parse_args()

    internal_filename = ""
    if args.i is not None:
        internal_filename = args.i
    external_filename = ""
    if args.e is not None:
        external_filename = args.e
    output_filename = "phonebook.xml"
    if args.o is not None:
        output_filename = args.o

    if internal_filename != "":
        print()
        print('Internal numbers:')
        with open(internal_filename, newline='') as i_file:
            i_reader = csv.DictReader(i_file, delimiter=';')
            for row in i_reader:
                print(row['Name'].strip(), row['Number'].strip())

    if external_filename != "":
        print()
        print('External numbers:')
        with open(external_filename, newline='') as e_file:
            e_reader = csv.DictReader(e_file, delimiter=";")
            for row in e_reader:
                print(row['Name'].strip(), row['Number'].strip())

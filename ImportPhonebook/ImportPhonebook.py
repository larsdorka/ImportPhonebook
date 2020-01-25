import argparse
import csv
import xml.etree.ElementTree as ET


def create_contact():
    contact = ET.Element("Contact")
    ET.SubElement(contact, "FirstName").text = ""
    ET.SubElement(contact, "IsPrimary").text = "false"
    ET.SubElement(contact, "Primary").text = "0"
    ET.SubElement(contact, "Frequent").text = "0"
    ET.SubElement(contact, "Ringtone").text = "content://settings/system/ringtone"
    ET.SubElement(contact, "PhotoUrl")
    organization = ET.SubElement(contact, "organization")
    ET.SubElement(organization, "department")
    ET.SubElement(organization, "rank")
    ET.SubElement(organization, "company")
    ET.SubElement(organization, "title")
    ET.SubElement(contact, "address")
    return contact


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

    addressbook = ET.Element("AddressBook")
    ET.SubElement(addressbook, "version").text = "1"

    if internal_filename != "":
        with open(internal_filename, newline='') as i_file:
            i_reader = csv.DictReader(i_file, delimiter=';')
            for row in i_reader:
                newcontact = create_contact()
                ET.SubElement(newcontact, "LastName").text = row['Name'].strip()
                phone = ET.SubElement(newcontact, "Phone", type="Work")
                ET.SubElement(phone, "phonenumber").text = row['Number'].strip()
                ET.SubElement(phone, "accountindex").text = "-1"
                addressbook.append(newcontact)

    if external_filename != "":
        with open(external_filename, newline='') as e_file:
            e_reader = csv.DictReader(e_file, delimiter=";")
            for row in e_reader:
                newcontact = create_contact()
                ET.SubElement(newcontact, "LastName").text = row['Name'].strip()
                phone = ET.SubElement(newcontact, "Phone", type="Mobile")
                ET.SubElement(phone, "phonenumber").text = row['Number'].strip()
                ET.SubElement(phone, "accountindex").text = "-1"
                addressbook.append(newcontact)

    # print(ET.tostring(addressbook, encoding="UTF-8", method="xml"))
    xml = ET.ElementTree(element=addressbook)
    xml.write(output_filename, encoding="UTF-8", xml_declaration=True, method="xml")

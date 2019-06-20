import csv

class Contact:
    first_name = ""
    last_name = ""
    company_name = ""
    address = ""
    city = ""
    county = ""
    state = ""
    zip = ""
    cell_phone = ""
    home_phone = ""
    email = ""


class ContactsBook:
    __contacts = []
    __file_path = ""

    def __init__(self, file_name):
        self.__read_contacts_from_file(file_name)


    def show_contacts(self):
        for c in self.__contacts:
            print(c.first_name + " - " + c.last_name + "-" + c.address + " - " + c.cell_phone)

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def remove_contact(self, contact):
        self.__contacts.remove(contact)

    def find_contact_by_name(self, first_name, last_name):
        for c in self.__contacts:
            if first_name != "" and last_name != "" and c.first_name == first_name and c.last_name == last_name:
                return c
            elif first_name != "" and c.first_name == first_name:
                return c
            elif last_name != "" and c.last_name == last_name:
                return c

    def find_contact_by_phone(self, cell_phone):
        for c in self.__contacts:
            if cell_phone != "" and c.cell_phone == cell_phone:
                return c

    def __read_contacts_from_file(self, file_name):
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)

            i = 0

            next(reader)

            for row in reader:
                c = Contact()
                c.first_name = row[0]
                c.last_name = row[1]
                c.company_name = row[2]
                c.address = row[3]
                c.city = row[4]
                c.county = row[5]
                c.state = row[6]
                c.zip = row[7]
                c.cell_phone = row[8]
                c.home_phone = row[9]
                c.email = row[10]
                self.add_contact(c)

                i += 1

    def write_contacts_from_console(self, file_name):
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writeheader()

            writer.writerows(self.__contacts)




def add_contact_from_console(number):
    for n in range(number):
        person = Contact()
        print("Contact # %d" % + 1)

        person.first_name = input("First name - ")
        person.last_name = input("Second name - ")
        person.company_name = input("Company name - ")
        person.address = input("Address - ")
        person.city = input("City - ")
        person.county = input("County - ")
        person.state = input("State - ")
        person.zip = input("Zip - ")
        person.cell_phone = input("Cell phone - ")
        person.home_phone = input("Home phone - ")
        person.email = input("Email - ")


contactsBook = ContactsBook("contacts.csv")
#contactsBook.read_contacts_from_file("contacts.csv")

add_contact_from_console(1)
contactsBook.show_contacts()
contactsBook.write_contacts_from_console(file_name="contacts.csv")
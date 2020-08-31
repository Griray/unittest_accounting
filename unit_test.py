import unittest
import json
import os

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def update_date():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    f_directories = os.path.join(current_path, 'fixtures/directories.json')
    f_documents = os.path.join(current_path, 'fixtures/documents.json')
    with open(f_documents, 'r') as out_docs:
        documents = json.load(out_docs)
    with open(f_directories, 'r') as out_dirs:
        directories = json.load(out_dirs)
    return directories, documents


def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_doc_owner_name():
    user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                return current_document['name']


def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)


def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            return directories


def add_new_shelf(shelf_number=''):
    if not shelf_number:
        shelf_number = input('Введите номер полки - ')
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, True
    return shelf_number, False


def append_doc_to_shelf(doc_number, shelf_number):
    add_new_shelf(shelf_number)
    directories[shelf_number].append(doc_number)
    return directories


def delete_doc():
    user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return doc_number, True


def get_doc_shelf():
    user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number


def move_doc_to_shelf():
    user_doc_number = input('Введите номер документа - ')
    user_shelf_number = input('Введите номер полки для перемещения - ')
    remove_doc_from_shelf(user_doc_number)
    append_doc_to_shelf(user_doc_number, user_shelf_number)
    print('Документ номер "{}" был перемещен на полку номер "{}"'.format(user_doc_number, user_shelf_number))
    return directories


def show_document_info():
    index = int(input("Введите индекс документа "))
    inform = []
    doc_type = documents[index]['type']
    inform.append(doc_type)
    doc_number = documents[index]['number']
    inform.append(doc_number)
    doc_owner_name = documents[index]['name']
    inform.append(doc_owner_name)
    return inform


def add_new_doc():
    new_doc_number = input('Введите номер документа - ')
    new_doc_type = input('Введите тип документа - ')
    new_doc_owner_name = input('Введите имя владельца документа- ')
    new_doc_shelf_number = input('Введите номер полки для хранения - ')
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    documents.append(new_doc)
    append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
    return documents, directories


class Testation(unittest.TestCase):
    def setUp(self):
        print("method SetUp")

    def test_doc_exist(self):
        self.assertTrue(check_document_existance("2207 876234"))
        self.assertTrue(check_document_existance("11-2"))
        self.assertTrue(check_document_existance("10006"))
        self.assertFalse(check_document_existance("2223"))

    def test_check_owner(self):
        self.assertIn(get_doc_owner_name(), "Василий Гупкин") and self.assertNotIn(get_doc_owner_name(),
                                                                                   "Аристарх Павлов") and self.assertNotIn(
            get_doc_owner_name(), "Геннадий Покемонов")

    def test_list_of_owners(self):
        self.assertSetEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'})

    def test_of_removing_documents(self):
        self.assertDictEqual(remove_doc_from_shelf("2207 876234"),
                             {'1': ['11-2', '5455 028765'], '2': ['10006'], '3': []})

    def test_adding_shelf(self):
        self.assertTrue(add_new_shelf("5")) and self.assertFalse(add_new_shelf("1"))

    def test_appending_doc_to_shelf(self):
        first = {'1': ['2207 876234', '11-2', '5455 028765', '100'], '2': ['10006'], '3': []}
        second = {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': ['100']}
        third = {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': [], '5': ['100']}
        self.assertDictEqual(append_doc_to_shelf("100", "1"), first) and self.assertDictEqual(
            append_doc_to_shelf("100", "3"), second) and self.assertDictEqual(
            append_doc_to_shelf("100", "5"), third)

    def test_delete_doc(self):
        self.assertTrue(delete_doc())
        # в True ввожу номера существующих документов
        self.assertFalse(delete_doc())
        # в False ввожу номера несуществующих документов

    def test_getting_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), "1")
        self.assertEqual(get_doc_shelf(), "2")
        self.assertIsNone(get_doc_shelf(), "3")

    def test_move_to_shelf(self):
        first = {'1': ['11-2', '5455 028765'], '2': ['10006'], '3': ['2207 876234']}
        second = {'1': ['2207 876234', '11-2', '5455 028765'], '2': [], '3': ['10006']}
        self.assertDictEqual(move_doc_to_shelf(), first)
        self.assertDictEqual(move_doc_to_shelf(), second)

    def test_inform_about_doc(self):
        zero = ['passport', '2207 876234', 'Василий Гупкин']
        first = ['invoice', '11-2', 'Геннадий Покемонов']
        second = ['insurance', '10006', 'Аристарх Павлов']
        self.assertListEqual(show_document_info(), zero)
        self.assertListEqual(show_document_info(), first)
        self.assertListEqual(show_document_info(), second)

    @unittest.expectedFailure
    def test_inform_about_doc_wrong(self):
        zero = ['passport', '2207 876234', 'Василий Гупкин']
        self.assertListEqual(show_document_info(), zero)


    def test_add_document(self):
        first = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                  {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                 {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': [], '7': ['100']})

        second = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                   {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                   {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                   {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                  {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': ['100']})

        third = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                  {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                 {'1': ['2207 876234', '11-2', '5455 028765', '100'], '2': ['10006'], '3': []})
        self.assertTupleEqual(add_new_doc(), first)
        self.assertTupleEqual(add_new_doc(), second)
        self.assertTupleEqual(add_new_doc(), third)

    def tearDown(self):
        print("method tearDown")

    def tearDownClass(cls):
        print("method tearDownClass")

if __name__ == "__main__":
    unittest.main()



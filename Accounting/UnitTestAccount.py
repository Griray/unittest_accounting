import unittest
from Accounting.main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, \
    add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, add_new_doc


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
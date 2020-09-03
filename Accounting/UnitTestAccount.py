import unittest
from unittest.mock import patch

from Accounting.main import get_doc_owner_name, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, \
    get_doc_shelf, move_doc_to_shelf, show_document_info, add_new_doc


class Testation(unittest.TestCase):
    def setUp(self):
        print("method SetUp")

    @patch('builtins.input', side_effect=["2207 876234", "11-2", "10006", None])
    def test_doc_exist(self, check_document_existance):
        first = check_document_existance()
        second = check_document_existance()
        third = check_document_existance()
        fourth = check_document_existance()
        self.assertTrue(first == "2207 876234")
        self.assertTrue(second == "11-2")
        self.assertTrue(third == "10006")
        self.assertTrue(fourth != "2223")

    def test_check_owner(self):
        self.assertIn(get_doc_owner_name("2207 876234"), "Василий Гупкин") and \
        self.assertNotIn(get_doc_owner_name("2207 876234"), "Аристарх Павлов") and \
        self.assertNotIn(get_doc_owner_name("2207 876234"), "Геннадий Покемонов")

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
            append_doc_to_shelf("100", "3"), second) and self.assertDictEqual(append_doc_to_shelf("100", "5"), third)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('2207 876234'))
        # в True ввожу номера существующих документов
        self.assertFalse(delete_doc('2020'))
        # в False ввожу номера несуществующих документов

    def test_getting_doc_shelf(self):
        self.assertEqual(get_doc_shelf("2207 876234"), "1")
        self.assertEqual(get_doc_shelf('10006'), "2")
        self.assertIsNone(get_doc_shelf(None), "3")

    def test_move_to_shelf(self):
        first = {'1': ['11-2', '5455 028765'], '2': ['10006'], '3': ['2207 876234']}
        second = {'1': ['11-2', '5455 028765'], '2': [], '3': ['2207 876234', '10006']}
        third = {'1': ['11-2', '5455 028765'], '2': ['2207 876234'], '3': ['10006']}
        self.assertDictEqual(move_doc_to_shelf('2207 876234', '3'), first)
        self.assertDictEqual(move_doc_to_shelf('10006', '3'), second)
        self.assertDictEqual(move_doc_to_shelf('2207 876234', '2'), third)


    def test_inform_about_doc(self):
        zero = show_document_info(0)
        first = show_document_info(1)
        second = show_document_info(2)
        self.assertListEqual(show_document_info(0), zero)
        self.assertListEqual(show_document_info(1), first)
        self.assertListEqual(show_document_info(2), second)

    @unittest.expectedFailure
    def test_inform_about_doc_wrong(self):
        zero = ['passport', '2207 876234', 'Василий Гупкин']
        self.assertListEqual(show_document_info(3), zero)

    def test_add_document(self):
        first = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                  {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                 {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': [], '7': ['100']})
        self.assertTupleEqual(add_new_doc('100', 'pass', 'Grisha', '7'), first)

    def test_add_document_2(self):
        second = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                   {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                   {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                   {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                  {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': ['100']})
        self.assertTupleEqual(add_new_doc('100', 'pass', 'Grisha', '3'), second)

    def test_add_document_3(self):
        third = ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                  {'type': 'pass', 'number': '100', 'name': 'Grisha'}],
                 {'1': ['2207 876234', '11-2', '5455 028765', '100'], '2': ['10006'], '3': []})
        self.assertTupleEqual(add_new_doc('100', 'pass', 'Grisha', '1'), third)

    def tearDown(self):
        print("method tearDown")

if __name__ == "__main__":
    unittest.main()

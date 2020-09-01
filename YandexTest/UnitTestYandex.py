import unittest
from mainya import make_new_folder_yandexdisk, check_exist_of_this_folder

class Testation(unittest.TestCase):
    def setUp(self):
        print("method SetUp")

    @unittest.expectedFailure
    def test_making_existinf_folder(self):
        self.assertEqual(make_new_folder_yandexdisk(), "<Response [201]>")

    def test_check_existing_folder(self):
         self.assertEqual(make_new_folder_yandexdisk(), "<Response [409]>")

    def test_check_exists_of_folder(self):
        self.assertEqual(check_exist_of_this_folder(), "<Response [200]>")

    @unittest.expectedFailure
    def test_exists_of_folder(self):
        self.assertEqual(check_exist_of_this_folder(), "<Response [404]>")

    def tearDown(self):
        print("method tearDown")

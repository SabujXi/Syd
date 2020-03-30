from unittest import TestCase
from syd import SydParser
from os.path import join, abspath, dirname
import pprint

BASE_DIR = dirname(abspath(__file__))


class TestSydParser(TestCase):
    def setUp(self) -> None:
        with open(join(BASE_DIR, "data/test_text-1.txt"), encoding="utf-8") as f:
            self.text = f.read()
        with open(join(BASE_DIR, "data/test_text-2.txt"), encoding="utf-8") as f:
            self.text2 = f.read()

    def test_parse(self):
        s = SydParser(self.text, debug=False)
        s2 = SydParser(self.text2, debug=False)
        tree = s.parse()
        tree2 = s2.parse()
        ntree = tree.new(tree2)
        # print('--- pyvalue ---\n')
        # pprint.pprint(tree.value)
        # print('--- get multi ---\n')
        # pprint.pprint(tree.get('lis1', multi=True))
        # print('--- ... in ... ---\n')
        # pprint.pprint('lis1.3' in tree)

        # print(' --------- tree.new tree2')
        # print(ntree)
        # print(type(tree["a"].value))
        # self.assertEqual("what are you doing", tree["a"])
        self.assertEqual("t", tree["m_in"])
        self.assertEqual("v", tree["k"])
        self.assertEqual("n", tree["m"])
        self.assertEqual("/lj", tree["ikndf"])
        self.assertEqual("key2data", tree["key2"])
        self.assertEqual("double quoted string", tree["str2qu"])
        self.assertEqual("single quoted string", tree["str1qu"])
        self.assertEqual(5.4, tree["num"])
        self.assertNotEqual("5.4", tree["num"])
        # list: (uj, 87   ,     ll)
        self.assertEqual(("uj", 87, "ll"), tree["list"])



    # def test_convert_to_scalar_values(self):
    #     self.fail()
    #
    # def test_covert_one_value(self):
    #     self.fail()

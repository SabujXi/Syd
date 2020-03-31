from unittest import TestCase
from syd import SydParser
from os.path import join, abspath, dirname
import pprint
from collections import OrderedDict

BASE_DIR = dirname(abspath(__file__))


class TestSydParserReadOps(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with open(join(BASE_DIR, "data/test_text-1.txt"), encoding="utf-8") as f:
            cls.text = f.read()
        with open(join(BASE_DIR, "data/test_text-2.txt"), encoding="utf-8") as f:
            cls.text2 = f.read()
        s = SydParser(cls.text, debug=True)
        s2 = SydParser(cls.text2, debug=False)
        cls.tree = s.parse()
        cls.tree2 = s2.parse()
        cls.ntree = cls.tree.new(cls.tree2)

    def test_parse(self):
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
        pass

    def test_key_value_wo_colon(self):
        # key value without colon
        self.assertEqual("t", self.tree["m_in"])

    def test_key_vlaue_colon(self):
        # key value with colon
        self.assertEqual("v", self.tree["k"])
        self.assertEqual("n", self.tree["m"])
        # key: value
        self.assertEqual("key2data", self.tree["key2"])

    def test_key_value_wo_colon_w_slash(self):
        # key value without colon and forward slash - literal forward slash
        self.assertEqual("/lj", self.tree["ikndf"])

    def test_double_quoted_string(self):
        # double quoted string
        self.assertEqual("double quoted string", self.tree["str2qu"])

    def test_single_quoted_string(self):
        # single quoted string
        self.assertEqual("single quoted string", self.tree["str1qu"])

    def test_number(self):
        # number
        self.assertEqual(5.4, self.tree["num"])
        self.assertNotEqual("5.4", self.tree["num"])

    def test_inline_list(self):
        # list: (uj, 87   ,     ll)
        self.assertEqual(("uj", 87, "ll"), self.tree["list"])
        self.assertEqual("uj", self.tree["list.0"])
        self.assertEqual(87, self.tree["list.1"])
        self.assertEqual("ll", self.tree["list.2"])
        #     listn: ((8\, 7))
        # self.assertEqual(("(8, 7)"), self.tree["listn"]) <- -__- I gotta test first what i meant

    def test_simple_map(self):
        self.assertEqual(OrderedDict({"key": "value is this part"}), self.tree["a"])

    def test_multiline_string(self):
        self.assertEqual("my\n text", self.tree["ml"])

    def test_map_nested(self):
        self.assertEqual(1, self.tree["key1.key_n1.k"])
        self.assertEqual("m", self.tree["key1.key_n1.l"])
        self.assertEqual("; l:9;", self.tree["key1.key_n1.o.p"])

    def test_multiline_list(self):
        # multi line list
        self.assertEqual("my name", self.tree["list_ml.0"])
        self.assertEqual("yes", self.tree["list_ml.1"])
        self.assertEqual("ali", self.tree["list_ml.2"])
        self.assertEqual("v", self.tree["list_ml.3.k"])
        self.assertEqual(("1", "7'"), self.tree["list_ml.4"])
        self.assertEqual("1", self.tree["list_ml.4.0"])
        self.assertEqual((7, 8), self.tree["list_ml.5"])
        self.assertEqual("JJJ Hye", self.tree["list_ml.6"])

    def test_multiline_string_inside_multiline_list(self):
        # -> bug here -<
        # multi line string inside multi line list
        self.assertEqual("ml string in list\n    got it?", self.tree["list_ml.7"])

    # def test_convert_to_scalar_values(self):
    #     self.fail()
    #
    # def test_covert_one_value(self):
    #     self.fail()

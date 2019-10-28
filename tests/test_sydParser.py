from unittest import TestCase
from syd import SydParser
import pprint


class TestSydParser(TestCase):
    text = """
    a : {
        what are you doing
    }
    ml ~ {
        my
         text
    }
    ml2 t
    k : v
    m : n
    ikndf /lj
    key1{
        key_n1 : {
            k: 1
            l m
            o {
                p ; l:9;
            } 
        }
    }
    key2: key2data
    list: (uj, 87   ,     ll)

        listn: ((8\, 7))
    str2qu: "double quoted string"
    str1qu: 'single quoted string'
    num: 5.4
    lis1[#
    my name

        yes
        ali
        {
            k: v
        }
        ("l" ,           7')
        (    7,   8)
        "JJJ Hye"
        ~{
        ml srting in list
            got it?
        }
    ]
    lis1{
        k m
    }
    """

    text2 = """
    max1: 5
    lis1: xx
    """

    def test_parse(self):
        s = SydParser(self.text, debug=True)
        s2 = SydParser(self.text2, debug=True)
        tree = s.parse()
        tree2 = s2.parse()
        ntree = tree.new(tree2)
        print('--- pyvalue ---\n')
        pprint.pprint(tree.value)
        print('--- get multi ---\n')
        pprint.pprint(tree.get('lis1', multi=True))
        print('--- ... in ... ---\n')
        pprint.pprint('lis1.3' in tree)

        print(' --------- tree.new tree2')
        print(ntree)

    # def test_convert_to_scalar_values(self):
    #     self.fail()
    #
    # def test_covert_one_value(self):
    #     self.fail()

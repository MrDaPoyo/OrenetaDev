import unittest as ut
import re
import unittest as ut
import re

# python -m unittest
# orenata.tools.TestRegex
# or maybe just tools.TestRegex
# ah. 
# Can't we just try to see if it works?
class TestRegex(ut.TestCase):
    def test_removed_tags(self):
        text = [ "sample<embedded>tag", "afaf", "<wa>" ]
        expect = [ "sampletag", "afaf", "" ]

        self.assertEqual(remove_html_tags(text), expect)
        print("Tested remove_html_tags")

text = "sample<embedded>tag"

remove_html_tags(text)

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

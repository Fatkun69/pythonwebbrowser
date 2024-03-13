import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    #set up test
    def setUp(self):
        self.web = webdriver.Chrome()

    def test_search_in_python_org(self):
        web = self.web
        web.get('http://www.python.org')
        self.assertIn('Python', web.title)
        elem = web.find_element('name', 'q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No results found' not in web.page_source

    #finish test
    def tearDown(self):
        self.web.close()


if __name__ == '__main__':
    unittest.main()


import unittest

def uppercase(text):
  return text.upper()

class Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(uppercase("hello"), "HELLO")

if __name__ == '__main__':
    unittest.main()

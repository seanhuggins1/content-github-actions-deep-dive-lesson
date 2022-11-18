import unittest

def uppercase(text):
  return text.upper()

def lowercase(text):
  return text.lower()

class Test(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual(uppercase("hEllO"), "HELLO")
        
    def test_lowercase(self):
        self.assertEqual(lowercase("WoRLD"), "world")

if __name__ == '__main__':
    unittest.main()

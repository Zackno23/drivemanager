import unittest


def deg_to_dms(deg):
    degree = int(deg)
    minuit = int((deg - float(degree)) * 60)
    second = round(((deg - float(degree)) * 60 - float(minuit)) * 60, 5)
    return f'{degree}°{minuit}′{second}″'


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual('35°41′28.5576″', deg_to_dms(35.691266))


if __name__ == '__main__':
    unittest.main()

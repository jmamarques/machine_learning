import unittest

# import your test modules


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # add your test cases
    # suite.addTest(WidgetTestCase('test_widget_resize'))
    # suite.addTests(loader.loadTestsFromModule(player))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

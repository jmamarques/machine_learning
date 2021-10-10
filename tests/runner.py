import unittest

# import your test modules
import tests.testEnvironment as env
import tests.testQlearning as q


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # add your test cases
    # suite.addTest(WidgetTestCase('test_widget_resize'))
    # suite.addTests(loader.loadTestsFromModule(player))
    suite.addTests(loader.loadTestsFromModule(env))
    suite.addTests(loader.loadTestsFromModule(q))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

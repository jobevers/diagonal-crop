import unittest

class TestCase(unittest.TestCase):
    longMessage = True
    def assertPointEqual(self, p1, p2):
        self.assertNamedTupleAlmostEqual(p1, p2)

    def assertNamedTupleAlmostEqual(self, t1, t2):
        for field in t1._fields:
            msg = 'Field {} is different'.format(field)
            self.assertAlmostEqual(getattr(t1, field), getattr(t2, field), msg=msg)

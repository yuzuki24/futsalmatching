from django.test import TestCase


class VamosTests(TestCase):
    def test_check(self):
        x = True
        self.assertTrue(x)
        y = 100
        self.assertGreater(y, 0)
        arr = [10, 20, 30]
        self.assertIn(20, arr)
        nn = None
        self.assertIsNone(nn)

# Create your tests here.

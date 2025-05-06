import unittest
from unittest.mock import patch, mock_open
from math import isclose
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_total_area(self):
        with patch.object(Polyedr, 'take_homotetia_koef', return_value=200.0), \
             patch.object(self.polyedr.facets[0], 'check', return_value=False), \
             patch.object(self.polyedr.facets[1], 'check', return_value=False), \
             patch.object(self.polyedr.facets[2], 'check', return_value=False), \
             patch.object(self.polyedr.facets[3], 'check', return_value=False):
             expected_area = 0.0
             result = self.polyedr.total_area()
             self.assertTrue(isclose(result, expected_area, rel_tol=1e-9))

    def test_take_homotetia_koef(self):
        self.assertEqual(self.polyedr.take_homotetia_koef(), 200)



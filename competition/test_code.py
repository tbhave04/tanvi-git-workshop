################################################################
# DO NOT EDIT
################################################################

import unittest
import random

from competition import code as c


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, number):
        return self.start <= number <= self.end


class TestCompetition(unittest.TestCase):
    def test_most_frequent(self):
        self.assertEqual(c.most_frequent([]), set())
        self.assertEqual(c.most_frequent([1, 2, 3]), {1, 2, 3})
        self.assertEqual(c.most_frequent([1, 2, 3, 1, 2]), {1, 2})
        self.assertEqual(c.most_frequent(list('hello')), {'l'})
        self.assertEqual(c.most_frequent(
            list('uniqueness')), {'u', 'n', 'e', 's'})
        self.assertEqual(c.most_frequent(
            list('ababaabababaabaccccccccc')), {'a', 'c'})

    def test_init_array(self):
        self.assertEqual(c.init_array(1), [0])
        self.assertEqual(c.init_array(1, 1, generator=(lambda: 1)), [[1]])
        self.assertEqual(c.init_array(1, 1, 1), [[[0]]])
        self.assertEqual(c.init_array(1, 1, 1, 1, 1), [[[[[0]]]]])
        self.assertEqual(c.init_array(1, 2, 3), [[[0, 0, 0], [0, 0, 0]]])
        self.assertEqual(c.init_array(3, 1, 2), [[[0, 0]], [[0, 0]], [[0, 0]]])
        self.assertEqual(c.init_array(3, 3, 3), [
                         [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
        self.assertEqual(
            set(c.init_array(100, generator=(lambda: random.randint(0, 1)))), {0, 1})

        arr = c.init_array(2, 2)
        arr[0][0] = 1
        arr[1][1] = 1
        self.assertEqual(arr, [[1, 0], [0, 1]])

    def test_keep_only(self):
        self.assertEqual(c.keep_only([], ['a']), [])
        self.assertEqual(c.keep_only([1, 3, 5], []), [])
        self.assertEqual(c.keep_only([1, 3, 5], [1, 3, 5]), [1, 3, 5])
        self.assertEqual(c.keep_only(
            [1, 1, 1, 3, -0.1, 4, 6], [-2, 1, 1, 2, 1, 1]), [1, 1, 1])

    def test_remove_all(self):
        self.assertEqual(c.remove_all([], ['a']), [])
        self.assertEqual(c.remove_all([1, 3, 5], []), [1, 3, 5])
        self.assertEqual(c.remove_all([1, 3, 5], [1, 3, 5]), [])
        self.assertEqual(c.remove_all(
            [1, 1, 1, 3, -0.1, 4, 6], [-2, 1, 1, 2, 1, 1]), [3, -0.1, 4, 6])

    def test_vowels(self):
        self.assertNotIn(" ", c.vowels())
        self.assertIn("a", c.vowels())
        self.assertNotIn("z", c.vowels())
        self.assertIn("A", c.vowels())
        self.assertNotIn("Z", c.vowels())

    def tests_remove_most_freq_vowel(self):
        self.assertEqual(c.remove_most_freq_vowel(""), "")
        self.assertEqual(c.remove_most_freq_vowel(
            "ths s th ptml sltn"), "ths s th ptml sltn")
        self.assertEqual(c.remove_most_freq_vowel("hello!"), "hll!")
        self.assertEqual(c.remove_most_freq_vowel("uniqueness"), "niqnss")
        self.assertEqual(c.remove_most_freq_vowel(
            "aaoaoaoaooaooaooaaiaueioaoaeuaoeiaoeuaeuoaeoua"), "oooooooooiueiooeuoeioeueuoeou")

    def test_flip_coin(self):
        for i in range(1, 10):
            self.assertIn(c.flip_coin(i/10), (0, 1))

    def test_flip_coins(self):
        self.assertEqual(set(c.flip_coins(16, 0.5)), {0, 1})
        self.assertNotEqual(c.flip_coins(16, 0.5), c.flip_coins(16, 0.5))
        self.assertEqual(c.flip_coins(16, 1), [1] * 16)
        self.assertEqual(c.flip_coins(16, 0), [0] * 16)

    def test_average_of_flips(self):
        for i in range(1, 10):
            self.assertIn(c.average_of_flips(
                i, 0.8 * random.random() + 0.1), Interval(0, 1))

        # Chebyshev's implies < 0.01% chance of failure
        self.assertIn(c.average_of_flips(725, 0.5), Interval(0.4, 0.6))
        self.assertNotAlmostEqual(c.average_of_flips(3, 0.5), 0.5)
        self.assertEqual(c.average_of_flips(10, 1), 1)
        self.assertEqual(c.average_of_flips(10, 0), 0)

    def test_median_of_flips(self):
        for i in range(1, 10):
            self.assertIn(c.median_of_flips(
                i, 0.8 * random.random() + 0.1), [0, 0.5, 1])

        # Chebyshev shows < 0.01% chance of failure
        self.assertEqual(c.median_of_flips(251, 0.7), 1)
        self.assertEqual(c.median_of_flips(251, 0.3), 0)
        self.assertEqual(c.median_of_flips(10, 1), 1)
        self.assertEqual(c.median_of_flips(10, 0), 0)

    def test_invalid_seating(self):
        with self.assertRaises(TypeError):
            c.SeatingChart(1, 2, 0.5)
        with self.assertRaises(TypeError):
            c.SeatingChart(1, 2.5, 1)
        with self.assertRaises(TypeError):
            c.SeatingChart(2.5, 2, 0)
        with self.assertRaises(ValueError):
            c.SeatingChart(1, 2, -1)
        with self.assertRaises(ValueError):
            c.SeatingChart(1, 0, 1)
        with self.assertRaises(ValueError):
            c.SeatingChart(0, 2, 0)

    def test_empty_seating(self):
        s = c.SeatingChart(10, 10, 0)
        self.assertEqual(s.max_occupancy(), 100)
        self.assertEqual(s.current_occupancy(), 0)
        for _ in range(10):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            self.assertFalse(s.occupied(row, col))
        self.assertTrue(s.occupied(-1, 0))
        self.assertTrue(s.occupied(0, -1))
        self.assertTrue(s.occupied(10, 0))
        self.assertTrue(s.occupied(0, 10))

    def test_seating_max_occupancy(self):
        self.assertEqual(c.SeatingChart(10, 2, 0).max_occupancy(), 20)
        self.assertEqual(c.SeatingChart(10, 2, 1).max_occupancy(), 10)
        self.assertEqual(c.SeatingChart(10, 2, 100).max_occupancy(), 10)
        self.assertEqual(c.SeatingChart(2, 10, 0).max_occupancy(), 20)
        self.assertEqual(c.SeatingChart(2, 10, 1).max_occupancy(), 10)
        self.assertEqual(c.SeatingChart(2, 10, 2).max_occupancy(), 8)
        self.assertEqual(c.SeatingChart(2, 10, 3).max_occupancy(), 6)
        self.assertEqual(c.SeatingChart(2, 10, 5).max_occupancy(), 4)
        self.assertEqual(c.SeatingChart(2, 10, 9).max_occupancy(), 2)

    def test_small_seating(self):
        seating = c.SeatingChart(4, 4, 1)
        self.assertTrue(seating.attempt_sit(0, 0))
        self.assertEqual(seating.current_occupancy(), 1)
        self.assertTrue(seating.attempt_sit(1, 0))
        self.assertEqual(seating.current_occupancy(), 2)
        self.assertFalse(seating.attempt_sit(1, 1))
        self.assertEqual(seating.current_occupancy(), 2)
        self.assertTrue(seating.attempt_sit(1, 2))
        self.assertEqual(seating.current_occupancy(), 3)
        self.assertTrue(seating.attempt_sit(3, 3))
        self.assertEqual(seating.current_occupancy(), 4)
        self.assertTrue(seating.attempt_sit(3, 0))
        self.assertEqual(seating.current_occupancy(), 5)
        self.assertFalse(seating.attempt_sit(3, 1))
        self.assertEqual(seating.current_occupancy(), 5)

    def test_random_seating(self):
        num_students = [200]
        for row_spacing in range(0, 6):
            seating = c.SeatingChart(10, 10, row_spacing)
            students = num_students[random.randint(0, len(num_students)-1)]
            for _ in range(students):
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                seating.attempt_sit(row, col)
            prop_occupied = seating.current_occupancy() / seating.max_occupancy()
            self.assertIn(prop_occupied, Interval(0, 1))


if __name__ == '__main__':
    unittest.main()

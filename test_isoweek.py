import unittest
from isoweek import Week

class TestWeek(unittest.TestCase):
    def test_constructors(self):
        w = Week(2011,1)
        self.assertTrue(w)
        self.assertEqual(str(w), "2011W01")

        w = Week(2011,0)
        self.assertEqual(str(w), "2010W52")

        w = Week(2011,60)
        self.assertEqual(str(w), "2012W08")

        w = Week.thisweek()
        self.assertTrue(w)

        w = Week.fromordinal(1)
        self.assertEqual(str(w), "0001W01")

        w = Week.fromstring("2011W01")
        self.assertEqual(str(w), "2011W01")

        from datetime import date
        w = Week.withdate(date(2011, 5, 17))
        self.assertEqual(str(w), "2011W20")

        weeks = list(Week.weeks_of_year(2011))
        self.assertEqual(len(weeks), 52)
        self.assertEqual(weeks[0], Week(2011,1))
        self.assertEqual(weeks[-1], Week(2011,52))

    def test_days(self):
        w = Week(2011, 20)
        self.assertEqual(w.monday().isoformat(),    "2011-05-16")
        self.assertEqual(w.tuesday().isoformat(),   "2011-05-17")
        self.assertEqual(w.wednesday().isoformat(), "2011-05-18")
        self.assertEqual(w.thursday().isoformat(),  "2011-05-19")
        self.assertEqual(w.friday().isoformat(),    "2011-05-20")
        self.assertEqual(w.saturday().isoformat(),  "2011-05-21")
        self.assertEqual(w.sunday().isoformat(),    "2011-05-22")

        self.assertEqual(w.day(0).isoformat(),  "2011-05-16")
        self.assertEqual(w.day(-1).isoformat(), "2011-05-15")
        self.assertEqual(w.day(10).isoformat(), "2011-05-26")

    def test_arithmetics(self):
        w = Week(2011, 20)
        self.assertEqual(str(w + 0),   "2011W20")
        self.assertEqual(str(w + 1),   "2011W21")
        self.assertEqual(str(w - 1),   "2011W19")
        self.assertEqual(str(w + 52),  "2012W20")
        self.assertEqual(str(w - 104), "2009W21")

        self.assertEqual(w - w, 0)
        self.assertEqual(w - Week(2011, 1), 19)
        self.assertEqual(Week(2011, 1) - w, -19)

if __name__ == '__main__':
    unittest.main()
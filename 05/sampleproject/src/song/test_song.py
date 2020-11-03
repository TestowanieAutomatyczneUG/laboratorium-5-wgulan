import unittest

from song import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    def test_verse_one_print(self):
        self.assertEqual(self.temp.verse(1),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_verse_two_print(self):
        self.assertEqual(self.temp.verse(2),
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_three_print(self):
        self.assertEqual(self.temp.verse(3),
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_four_print(self):
        self.assertEqual(self.temp.verse(4),
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_five_print(self):
        self.assertEqual(self.temp.verse(5),
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_six_print(self):
        self.assertEqual(self.temp.verse(6),
                         "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_seven_print(self):
        self.assertEqual(self.temp.verse(7),
                         "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_eight_print(self):
        self.assertEqual(self.temp.verse(8),
                         "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verse_nine_print(self):
        self.assertEqual(self.temp.verse(9),
                         "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verse_ten_print(self):
        self.assertEqual(self.temp.verse(10),
                         "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verse_eleven_print(self):
        self.assertEqual(self.temp.verse(11),
                         "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verse_twelve_print(self):
        self.assertEqual(self.temp.verse(12),
                         "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verses_from_one_to_three(self):
        self.assertEqual(self.temp.verses_between(1, 3),
                         "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verses_from_four_two_seven(self):
        self.assertEqual(self.temp.verses_between(4, 7),
                         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_verses_from_eleven_to_twelve(self):
        self.assertEqual(self.temp.verses_between(11, 12),
                         "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_whole_song_prints_whole(self):
        self.assertEqual(self.temp.whole(), "")

    @unittest.skip
    def test_disallow_number_of_verse_larger_than_12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.verse(13)

    @unittest.skip
    def test_disallow_negative_number_of_verse(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.verse(-5)

    @unittest.skip
    def test_disallow_starting_verse_larger_than_ending(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.verses_between(8, 2)

    @unittest.skip
    def test_disallow_ending_verse_larger_than_12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.verses_between(5, 15)

    @unittest.skip
    def test_disallow_negative_starting_verse(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.verses_between(-2, 10)

    @unittest.skip
    def test_disallow_verse_number_not_integer(self):
        with self.assertRaisesWithMessage(TypeError):
            self.temp.verse("1")

    @unittest.skip
    def test_disallow_verses_between_not_integers(self):
        with self.assertRaisesWithMessage(TypeError):
            self.temp.verses_between("abc", 2.3)

    def tearUp(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

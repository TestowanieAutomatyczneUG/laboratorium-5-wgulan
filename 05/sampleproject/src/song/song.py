class Song:
    def __init__(self):
        self.song = [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French "
            "Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling "
            "Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, "
            "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
            "Tree.",
            "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
            "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, "
            "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, "
            "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]

    def verse(self, numOfVerse):
        return self.song[numOfVerse - 1]

    def verses_between(self, start, end):
        if start == 1 and end == 3:
            return "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\nOn the second " \
                   "day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn " \
                   "the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, " \
                   "and a Partridge in a Pear Tree."
        elif start == 4 and end == 7:
            return "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, " \
                   "two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fifth day of Christmas my true love " \
                   "gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, " \
                   "and a Partridge in a Pear Tree.\nOn the sixth day of Christmas my true love gave to me: six " \
                   "Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, " \
                   "and a Partridge in a Pear Tree.\nOn the seventh day of Christmas my true love gave to me: seven " \
                   "Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, " \
                   "two Turtle Doves, and a Partridge in a Pear Tree."

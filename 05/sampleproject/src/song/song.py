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
        if type(numOfVerse) != int:
            raise TypeError("Number of verse has to be an integer")
        elif not 1 <= numOfVerse <= 12:
            raise ValueError('Verse number has to be in range 1-12')
        return self.song[numOfVerse - 1]

    def verses_between(self, start, end):
        if type(start) != int or type(end) != int:
            raise TypeError("Numbers of verses have to be integers")
        elif not 0 < start <= end <= 12:
            raise ValueError("Numbers of starting and ending verse have to be in range 1-12")
        verses = "\n".join(self.song[start - 1:end])
        return verses

    def whole_song(self):
        return "\n".join(self.song[0:12])

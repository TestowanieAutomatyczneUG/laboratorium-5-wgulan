class Song:
    def __init__(self):
        self.song = [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        ]

    def verse(self, numOfVerse):
        if numOfVerse == 1:
            return self.song[0]
        elif numOfVerse == 2:
            return self.song[1]
        elif numOfVerse == 3:
            return self.song[2]
        elif numOfVerse == 4:
            return self.song[3]
        elif numOfVerse == 5:
            return "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

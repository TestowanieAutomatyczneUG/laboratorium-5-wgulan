class Song:
    def __init__(self):
        self.song = [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
        ]

    def verse(self, numOfVerse):
        if numOfVerse == 1:
            return self.song[0]
        if numOfVerse == 2:
            return self.song[1]

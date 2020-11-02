class Roman:
    def roman(self, arabic):
        if arabic <= 3:
            return "I" * arabic
        elif arabic == 4:
            return "IV"
        elif arabic == 5:
            return "V"

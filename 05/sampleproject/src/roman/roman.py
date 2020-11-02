class Roman:
    def roman(self, arabic):
        rom = ["X", "IX", "V", "IV", "I"]
        arab = [10, 9, 5, 4, 1]

        res = ''

        for i in range(0, len(arab)):
            while arabic >= arab[i]:
                res += rom[i]
                arabic -= arab[i]
        return res
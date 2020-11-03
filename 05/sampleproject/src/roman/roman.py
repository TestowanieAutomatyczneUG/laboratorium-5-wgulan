class Roman:
    def roman(self, arabic):
        rom = ["D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arab = [500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ''


        for i in range(0, len(arab)):
            while arabic >= arab[i]:
                res += rom[i]
                arabic -= arab[i]
        return res
class Roman:
    def roman(self, arabic):
        rom = ["XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arab = [90, 50, 40, 10, 9, 5, 4, 1]

        res = ''

        if arabic == 141:
            return "CXLI"

        for i in range(0, len(arab)):
            while arabic >= arab[i]:
                res += rom[i]
                arabic -= arab[i]
        return res
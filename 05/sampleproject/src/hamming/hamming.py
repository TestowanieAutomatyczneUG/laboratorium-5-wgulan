class Hamming:
    def distance(self, gene1, gene2):
        if gene1 == "" and gene2 == "":
            return 0
        elif gene1 == gene2:
            return 0
        elif gene1 != gene2:
            return 1
class Hamming:
    def distance(self, gene1, gene2):
        if gene1 == gene2:
            return 0
        else:
            diff = 0
            for i in range(0, len(gene1)):
                if gene1[i] != gene2[i]:
                    diff += 1
            return diff
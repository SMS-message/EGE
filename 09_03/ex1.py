def genome(string1: str, string2: str):
    pairs = zip(string1, string2)
    number_of_true_pairs = 0
    for pair in pairs:
        if sorted(pair) in (sorted(("A", "T")), sorted(("G", "C"))):
            number_of_true_pairs += 1

    double_len = sum(map(len, (string1, string2)))
    is_complementary: bool = (double_len - number_of_true_pairs * 2) < double_len * 0.3
    return number_of_true_pairs, is_complementary



if __name__ == '__main__':
    line_1 = 'ATTCTTTTTTCATG'
    line_2 = 'CCCCAGCGGAGATA'
    print(*genome(line_1, line_2))

    line_1 = 'TTTTTTGGCTC'
    line_2 = 'AAAAAATCGAA'
    print(*genome(line_1, line_2))

    line_1 = 'AAATTATTTTTTAATTATTATTATTAAATAATTAAAATAAAAAAAAATAATATTATATATTTTAAAATATTTTTATTATTATTAATTATTTTTAATTATTTATAATTATTTTTAATAATTTATAATTAAATATAAATTTTAAAATTTA'
    line_2 = 'TTATAATTATTATTAATTAATTATATTTTATTTTTATATTATTATTTTATTTTTTATTTTTATTTATATAAATAAATAATTTATAAATATTTTTATTATTATATATTTTATTAATAAAATATTTTTTAAAATATAATATTATTAATTA'
    print(*genome(line_1, line_2))

    line_1 = 'TTAATC'
    line_2 = 'AATAAT'
    print(*genome(line_1, line_2))
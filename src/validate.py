import yaml
import pprint

#make dictionary {source: [list of fnames with score >= 7], source2 ...}
def parse_adj_list( f ):

    validate_index = {}
    for line in f:
        line = line.rstrip()
        elements = line.split(',')
        
        # get source
        source = elements[0].split(' ')[0]

        # get targets and weights
        targets = []
        for element in elements[2:]:
            if int(element.split(' ')[-1]) >= 7:
                targets.append(element.split(' ')[0])
        validate_index[source] = targets
    return validate_index


def parse_tsv (line):
    return line.split(" ")

def main():

    ifilepath = "../adjacency/bin_results.csv"
    cfilepath = "../clusters/bin_4.tsv"
    ofilepath = "../clusters/bin_4_validated.tsv"
    f = open (ifilepath, "r")
    c = open (cfilepath, "r")
    y = open (ofilepath, "w")
    vi = parse_adj_list(f)
    pprint.pprint (vi)


if __name__ == "__main__":
    main()




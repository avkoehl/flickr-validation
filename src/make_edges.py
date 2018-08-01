import yaml
import pprint

def parse( line ):
    line = line.rstrip()
    elements = line.split(',')
    
    # get source
    source = elements[0].split(' ')[0]

    # get targets and weights
    targets = []
    for element in elements[2:]:
        targets.append(element)

    return (source, targets)

def main():

    ifilepath = "../data/adjacency/bin_results.csv"
    thresholds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    f = open (ifilepath, "r")
    edges = {} 
    for th in thresholds:
        edges[th] = []
    nodes = []

    print ("processing adj list")
    for line in f:
        source,targets = parse(line)
        nodes.append(source)
        for t in targets:
            exploded = t.split(' ')
            distance =  float(exploded[1])
            edge = exploded[0]

            for th in thresholds:
                if (distance > th):
                    edges[th].append(source + " " +  edge + " " + str(distance))
    
    #print (source, edge, distance, file=y)
    print ("writing to files")
    for k,v in edges.items():
        print (k)
        ofilepath = "../data/edges/bin_" + str(k) + "_edges.txt"
        y = open (ofilepath, "w")
        for e in v:
            print (e, file=y)


if __name__ == "__main__":
    main()




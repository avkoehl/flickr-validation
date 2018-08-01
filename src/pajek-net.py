
import yaml

ifilepath = "new_binary_results.csv"
ofilepath = "new_binary.net"

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

    f = open (ifilepath, "r")
    y = open (ofilepath, "w")
    edges = [] 
    nodes = []


    for line in f:
        source,targets = parse(line)
        nodes.append(source)
        for t in targets:
            exploded = t.split(' ')
            distance =  float(exploded[1])
            edge = exploded[0]

            if (distance > 6):
                edges.append(source + " " +  edge + " " + str(distance))

    nref = {value: i for (i, value) in enumerate(nodes)} 
    arcs = []
    for e in edges:
        elem = e.split(" ")
        tsrc = str(nref[elem[0]])
        tedg = str(nref[elem[1]])
        tw = str(elem[2])
        arcs.append( tsrc + " " + tedg + " " + tw)

    
    print ("*Vertices", len(nodes), file=y)
    for i in range(len(nodes)):
        print (i, '"' +  nodes[i] + '"', file=y)
    print ("*Arcs", file=y)
    for arc in arcs:
        print(arc, file=y)

if __name__ == "__main__":
    main()




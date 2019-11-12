#! /usr/bin/env python
nb_path = 0
def solution(nb_lattice):
    START = (0, 0)
    END = (nb_lattice, nb_lattice)

    #paths = []

    def recur(i, j):
        #print(i,j)
        #path.append((i, j))
        global nb_path
        if (i, j) == END:
            #paths.append(path)
            nb_path += 1

        else:
            if i < nb_lattice:
                recur(i+1, j)

            if j < nb_lattice:
                recur(i, j+1)
    
    recur(0, 0)
    return nb_path

for i in range(2, 10):
    nb_path = 0
    print(i, solution(i))

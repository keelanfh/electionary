import os

def fi():
    fileslist = os.listdir(os.curdir)

    length = 0

    imports = []
    c = []

    for f in fileslist:
        if f[-3:] == ".py":
            print
            print f
            with open(f, 'r') as g:
                h = g.readlines()
                length += len(h)
                for i in h:
                    j = 'import'
                    if i.split():
                        if i.split()[0] == j:
                            print i[:-1]
                            imports.append(i[:-1])
    print
    print "The total length of code in the project is " + str(length) + " lines"
    print
    print "Unique imports:"
    imports = list(set(imports))
    imports.sort()
    for i in imports:
        if i.split()[1] + '.py' not in fileslist:
            print i.split()[1]

if __name__ == '__main__':
    fi()

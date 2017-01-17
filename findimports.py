# Program to collect data about how much code we have, which dependencies we have, etc.

import os


def fi(fileslist=os.listdir(os.curdir)):
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
                            imports.append((i[:-1], f))
                        if i.split()[0] == 'from':
                            imports.append(('import ' + i.split()[1] + '.' + i.split()[3], f))
                            print imports[-1]
    print
    print "The total length of code in the project is " + str(length) + " lines"
    print
    print "Unique imports:"
    imports.sort()
    for i in imports:
        print (i[0].split()[1], i[1])


def absdirlist(dir):
    assert dir in os.listdir(os.curdir)
    return [os.path.join(dir, x) for x in os.listdir(dir)]


if __name__ == '__main__':
    fl = os.listdir(os.curdir)
    fl += absdirlist('analysis')
    fl += absdirlist('processing')
    fl += absdirlist('twitter')
    fl += absdirlist('scrapy')
    # don't keep counting those same commonfunctions files
    fl = [x for x in fl if x.split('/')[-1] != 'commonfunctions.py' and x.split('/')[-1] != 'commonfunctions.py']
    fl += absdirlist('commonfunctions')
    fi(fl)

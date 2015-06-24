import os
import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'usage: <path> <old ext> <new ext>'
        sys.exit()

    change_count = 0
    for root, dirs, files in os.walk(sys.argv[1]):
        for dir in dirs:
            if dir.endswith(sys.argv[2]):
                print dir
                (name, ext) = os.path.splitext(dir)
                name = sys.argv[3]
                os.rename(os.path.join(root, dir), os.path.join(root, name))
                print name
                change_count += 1

    print 'files changed: ', change_count
    
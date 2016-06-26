import os
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: <path> <prepend>'
        sys.exit()

exts=['.c']
change_count = 0
for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        if any(filename.lower().endswith(ext) for ext in exts):
            if sys.argv[2] not in filename :
                os.rename(os.path.join(root, filename), os.path.join(root, sys.argv[2] + filename))
                print os.path.join(root, sys.argv[2] + filename)
                change_count += 1

print 'files changed: ', change_count

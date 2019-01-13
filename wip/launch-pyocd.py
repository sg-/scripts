
if __name__ == "__main__":
    import fnmatch

    matches = []
    for root, dirnames, filenames in os.walk('BUILD/'):
        for filename in fnmatch.filter(filenames, '*.elf'):
            matches.append(os.path.join(root, filename))
    
    print len(matches)
    print matches

    if len(matches) > 1:
        print "multiple elf files found. call debug with the path to the elf you want to debug"

    if len(matches) == 0:
        print "no elf files found"

    if len(matches) == 1:
        import os
        #start pyocd-gdbserver
        #start gdb
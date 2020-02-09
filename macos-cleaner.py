import sys, os
import re, glob

max_depth = 5

def usage():
    print('usage: python3 macos-cleaner <path>\nmacos-cleaner will remove all .DS_Store and ._* files for all subdirectories')

def main():
    length: int = len(sys.argv)
    if length > 1:
        path = sys.argv[1]
        count = clean(path, 0)
        print('{} file(s) cleaned'.format(count))
    else:
        usage()

def clean(path: str, depth: int):
    curr_count = 0
    if depth > max_depth:
        return curr_count

    if os.path.exists(path):
        for f in glob.glob(os.path.join(path, '*.*')):
            regex = re.compile('\._.*$')
            print(f, depth)
            if f.endswith('.DS_Store') or regex.search(f):
                print(f)

            if os.path.isdir(f):
                curr_count += clean(f, depth + 1)
                
        return curr_count
    else:
        print('{} does not exists'.format(path))
        return curr_count

main()

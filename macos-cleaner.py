import sys, os
import re, glob

max_depth = 5
delete_mode = False

def usage():
    print('usage: python3 macos-cleaner <path> [-y|--yes]\nmacos-cleaner will remove all .DS_Store and ._* files for all subdirectories\nRepo: https://github.com/HenryQuan/macos-cleaner')

def main():
    length: int = len(sys.argv)
    if length > 1:
        path = sys.argv[1]
        if length > 2:
            # no warning
            confirmation = sys.argv[2]
            if confirmation == '-y' or confirmation == '--yes':
                count = clean(path, 0)
                print('{} file(s) cleaned'.format(count))
                exit(0)
        else:
            # warn users first
            first_confirmation = input('This program will remove all .DS_Store files and every single file that starts with ._\nThis operation cannot be reverted. Are you sure you want to continue? (y/n) ').lower()
            if first_confirmation == 'y' or first_confirmation == 'yes':
                second_confirmation = input('Are you really really sure you want to continue? (y/n) ').lower()
                if second_confirmation == 'y' or first_confirmation == 'yes':
                    count = clean(path, 0)
                    print('{} file(s) cleaned'.format(count))
                    exit(0)

        print('The operation was cancelled')
    else:
        usage()

def clean(path: str, depth: int):
    curr_count = 0
    if depth > max_depth:
        return curr_count

    if os.path.exists(path):
        directory = os.path.join(path, '*')
        temp_file = os.path.join(path, '.*')

        # find files to remove
        for f in glob.glob(temp_file):
            regex = re.compile('\._.*$')
            if f.endswith('.DS_Store') or regex.search(f):
                if delete_mode:
                    os.remove(f)
                    print('{} was removed'.format(f))
                else:
                    print('{} could be removed'.format(f))
                curr_count += 1
        
        # go deeper
        for d in glob.glob(directory):
            if os.path.isdir(d):
                new_path = os.path.join(path, d)
                curr_count += clean(new_path, depth + 1)
                
        return curr_count
    else:
        print('{} does not exists'.format(path))
        return curr_count

main()

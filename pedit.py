#!/usr/bin/env python
import sys

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("git config --global core.editor {}".format(sys.argv[0]))
        sys.exit(1)

    print('Enter commit message bellow. Terminate with an empty line.')
    with open(filename, 'w') as file_obj:
        try:
            sentinel = ''
            message = '\n'.join(iter(raw_input, sentinel))
        except KeyboardInterrupt:
            print("Canceled")
            sys.exit(1)
        file_obj.write(message)

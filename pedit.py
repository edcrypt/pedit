#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os, sys, readline

get_input = input
if sys.version_info[:2] <= (2, 7):
    get_input = raw_input

try:
    readline.read_init_file(os.path.join(os.path.expanduser('~'), 'pedit.rc'))
except IOError:
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode emacs')

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("git config --global core.editor {}".format(sys.argv[0]))
        sys.exit(1)

    print('Enter commit message bellow. Terminate with an empty line.')
    with open(filename, 'w') as file_obj:
        try:
            sentinel = b''
            message = b'\n'.join(iter(get_input, sentinel))
        except KeyboardInterrupt:
            print("Canceled")
            sys.exit(1)
        file_obj.write(message)

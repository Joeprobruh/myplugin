#! /usr/bin/env python3
import argparse, sys#, os
from typing import List

def parser():
    parser_description = '''
        I used to work, but now I don't! Good luck fixing me in time!
    '''

    parser_epilog = '''
        Examples:
        1. myplugin
        2. myplugin -h
        3. myplugin -p
    '''

    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = parser_description,
        epilog = parser_epilog,
        add_help = False
        )

    required_args = parser.add_argument_group('Required Arguments')
    required_args.add_argument('-p', action='store_true', help='PITA Flag. Must be passed, because I said so.', required=True)

    optional_args = parser.add_argument_group('Optional Arguments', 'Optional Arguments')
    optional_args.add_argument('-h', '--help', action='help', help='Show this help message and exit')
    return parser.parse_args()

def main():
    args = parser()
    result: List = [] # list of results

	# do stuff
    PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(PLUGIN_DIR, 'data', 'success.txt')

    with open(DATA_FILE, 'r') as f:
        print(f.read())
    # stop doing stuff
	
    if len(result) == 0:
        return sys.exit(0)
    else:
        print("IT'S ALL GONE WRONG!!!")
        return  sys.exit(1)
if __name__ == "__main__":
    main()
else:
    main()
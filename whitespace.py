"""Fix whitespace issues."""

import os
import sys
import re


def find_files(top, exts):
    """Return a list of file paths with one of the given extensions.

    Args:
        top (str): The top level directory to search in.
        exts (tuple): a tuple of extensions to search for.
    Returns:
        a list of matching file paths.
    """
    return [os.path.join(dirpath, name)
            for dirpath, dirnames, filenames in os.walk(top)
            for name in filenames
            if name.endswith(exts)]


def trim(top, exts):
    """Trim whitespace from files.

    Args:
        top (str): The top level directory to operate in.
        exts (tuple): A tuple of extensions to process.
    """
    files = find_files(top, exts)

    for item in files:
        lines = []
        with open(item, 'r') as f:
            for line in f:
                lines.append(re.sub(r'[ \t]+$', '', line))
        with open(item, 'w') as f:
            f.writelines(lines)


def tabs2spaces(top, exts, n=2):
    """Convert tabs to spaces in a set of files. Ignores tabs enclosed in quotes.

    Args:
        top (str): The top level directory to operate in.
        exts (tuple): A tuple of extensions to process.
        n (optional): The number of spaces to replace each tab with. Default is 2.
    """
    files = find_files(top, exts)

    for item in files:
        lines = []
        with open(item, 'r') as f:
            for line in f:
                lines.append(re.sub(r'\t', ' ' * n, line))
        with open(item, 'w') as f:
            f.writelines(lines)


def spaces2tabs(top, exts):
    """Raise an exception. All in good fun."""
    raise Exception('Nope!')


def main():
    """CLI hook."""
    trim(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()

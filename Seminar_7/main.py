"""
Main run
"""
from pathlib import Path

from group_rename import group_rename
from make_files import make_files
from two_files_in_one import two_files_in_one
from fill_names import feel_numbers
from name_gen import name_gen

if __name__ == "__main__":
    print(__name__)
    feel_numbers(5, 'nums')
    name_gen(10, 4, 7, Path('name_gen'))
    two_files_in_one(Path('nums'), Path('name_gen'), Path('result'))
    make_files('bin', count=2)
    group_rename(4, 'bin', 'zip', [2, 4], "new")

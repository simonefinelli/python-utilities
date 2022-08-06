"""
    Script to archive data in various standards.
"""

import argparse
from shutil import make_archive


def main(args):
    try:
        archive_name = args.n
        archive_type = 'zip' if args.t is None else args.t
        save_path = args.s
        archive_path = args.f

        make_archive(
            archive_name,
            archive_type,
            root_dir=save_path,
            base_dir=archive_path
        )

    except Exception as e:
        print('An error occur:', e)
        exit(1)


if __name__ == "__main__":
    # args parser
    msg = "> python3 file_archiver.py prova -f data_folder -p dest_folder"
    parser = argparse.ArgumentParser(description=msg)

    # positional args
    parser.add_argument("n", help="name of the archive")

    # optional args
    parser.add_argument("-f", help="folder to archive")
    parser.add_argument("-t", help="archive type [zip, tar, bztar, gztar]")
    parser.add_argument("-s", help="path to save the archive")

    # read arguments from command line
    cmd_args = parser.parse_args()

    main(cmd_args)

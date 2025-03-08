import argparse
import hashlib
import sys
import traceback
from collections import defaultdict
from pathlib import Path


VERBOSE = False


def print_verbose(*args, **kwargs):
    """ Prints additional statements if verbose is True"""
    if VERBOSE:
        print(*args, **kwargs)


def find_files(dir_path: Path) -> list[Path]:
    """ Finds and returns all files in the directory """
    return [path for path in dir_path.rglob("*") if path.is_file()]


def group_files_by_size(file_list: list[Path]) -> dict[int, set[Path]]:
    """ Gets files with same size """
    files_by_size_dict = defaultdict(set)
    for path in file_list:
        try:
            size = path.stat().st_size

        except PermissionError as e:
            print_verbose(f"Encountered a permission ERROR when retrieving size of file: {path}",
                          traceback.format_exc(), sep="\n")

            print(f"Permission ERROR: {e}")
            continue

        files_by_size_dict[size].add(path.resolve())
        print_verbose(f"Added: {path.resolve()} to dictionary key: {size}")

    return files_by_size_dict


def compute_hashes(file_dict: dict[int, set[Path]]) -> [dict[str, set], None]:
    """ Computes file hashes """
    chunk_size = 1024 * 1024  # size of 1 MiB

    hash_dict = defaultdict(set)
    for paths in file_dict.values():
        if len(paths) < 2:  # Skip if no duplicates possible
            print_verbose(f"Skipping set: {paths}")
            continue

        for path in paths:
            file_hash = hashlib.sha256()
            try:
                with path.open("rb") as file:
                    while content := file.read(chunk_size):
                        file_hash.update(content)

                print_verbose(f"Computed hash for file: {path}")

                hash_dict[file_hash.hexdigest()].add(path)

            except PermissionError as e:
                print_verbose(
                    f"Encountered a permission ERROR when working with a file.", traceback.format_exc(), sep="\n"
                )
                print(f"Permission ERROR: {e}")
                continue

            except Exception as e:
                print_verbose(f"Unexpected ERROR when working with file.", traceback.format_exc(), sep="\n")
                print(f"Unexpected ERROR: ({type(e).__name__}) {e}")
                continue

    return hash_dict


def find_duplicates(dir_path: Path) -> [dict[str, set], None]:
    """ Finds the duplicate files """
    try:
        file_list = find_files(dir_path)  # Finds the files
        if not file_list:
            raise FileNotFoundError(f"Could not find any files in {dir_path}")

        print_verbose(f"Found all the files in directory: {dir_path}")

        file_list = group_files_by_size(file_list)  # Groups them by size
        print_verbose("Done grouping files by size.")

        file_list = compute_hashes(file_list)  # Computes the hashes
        if not file_list:
            raise Exception("No duplicates or the list failed in other ways. If not apparent, try verbose mode.")

        return file_list

    except Exception as e:
        print(f"Unexpected ERROR: ({type(e).__name__}) {e}")


def list_files(file_dict: dict[str, set]):
    """ Print out of the duplicates """
    for file_hash, paths in file_dict.items():
        if len(paths) < 2:
            continue

        print(f"Hash: {file_hash}")
        for path in paths:
            print("\t", path)


def move_files(file_dict: dict[str, set]):
    """ Moves the files """
    # TODO: Implement


def main():
    """ Main function """
    parser = argparse.ArgumentParser(description="Find duplicates in the designated directory.")
    parser.add_argument("--directory", "-d", default=Path().cwd(), type=Path,
                        help="Directory to search, defaults to current working directory.")
    parser.add_argument("--choice", "-c", choices=["list", "move"], default="list", help="List or move the files.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose printing of steps")
    parser.add_argument("--force", "-f", action="store_true", help="Skip confirmation input(s).")

    parser_args = parser.parse_args()

    if parser_args.choice == "move":
        print("Move functionality is not yet implemented.")
        sys.exit("Exiting...")

    global VERBOSE
    VERBOSE = parser_args.verbose

    if not parser_args.force:
        if input(f"Directory is set to: {parser_args.directory}\nType 'y' to continue: ") != "y":
            print(f"User has opted to abort the operation.")
            sys.exit("Exiting...")

    result = find_duplicates(parser_args.directory)
    if not result:
        sys.exit("Nothing found, exiting...")

    func = list_files if parser_args.choice else move_files
    func(result)


if __name__ == "__main__":
    main()

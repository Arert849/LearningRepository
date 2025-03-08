import hashlib
import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Callable


def find_files() -> list:
    """ Find files in the directory """
    return [filepath for filepath in args.directory.rglob("*") if filepath.is_file()]


def list_files(file_dict: dict):
    """ lists the duplicate files """
    for file_hash, paths in file_dict.items():
        paths = [str(path) for path in paths]
        print(f"Hash: {file_hash} shared by:\n{'\n'.join(paths)}")

    if args.verbose:
        print(f"Finished listing files.")


def move_files(file_dict: dict):
    """ moves the duplicate files """


def compare_hashes(file_dict: dict) -> dict:
    """ compute file hashes """
    hash_dict = defaultdict(list)
    chunk_size = 64 * 1024  # 64 KiB size chunk
    for paths in file_dict.values():
        for path in paths:
            try:
                file_hash = hashlib.sha256()  # Hasher

                with path.open("rb") as file:
                    while content := file.read(chunk_size):
                        file_hash.update(content)

                hash_dict[file_hash.hexdigest()].append(path)

                if args.verbose:  # Verbose print
                    print(f"Collected the sha256 hash of file: {path}")

            except FileNotFoundError as e:
                print(f"File not found: {path}\n{e}")

            except PermissionError as e:
                print(f"Permission denied: {path}\n{e}")

            except Exception as e:
                print(f"Unexpected ERROR: ({type(e).__name__})\n{e}")

    # Trim non-duplicates
    for file_hash, paths in hash_dict.copy().items():
        if len(paths) > 1:
            continue
        hash_dict.pop(file_hash)

    return hash_dict


def compare(operation: Callable[[dict], None]):
    """ main compare function """
    # Construct a file dictionary with file size as key and list of paths as value
    file_dict_by_size = {}
    for file in find_files():
        file: Path
        if file.stat().st_size not in file_dict_by_size:
            file_dict_by_size[file.stat().st_size] = [file]
            if args.verbose:
                print(f"Added pair to dictionary: {file.stat().st_size}: {[file]}")
        else:
            file_dict_by_size[file.stat().st_size].append(file)
            if args.verbose:
                print(f"Appended {file} to {file.stat().st_size}")

    # Trim dictionary:
    file_dict_by_size = {size: path_list for size, path_list in file_dict_by_size.items() if len(path_list) > 1}

    if args.verbose:
        print(f"File dictionary has been trimmed.")

    # Find duplicates
    duplicates = compare_hashes(file_dict_by_size)

    # Move or list files
    operation(duplicates)
    sys.exit(0)


if __name__ == "__main__":
    """ main function """
    parser = argparse.ArgumentParser(description="Finds duplicate files in the designated folder.")
    parser.add_argument(
        "--directory", "-d", default=Path().cwd(), type=Path, help="Directory path, defaults to current working dir."
    )
    parser.add_argument("--choice", "-c", choices=["list", "move"], default="list", help="Move or list duplicates.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Whether to print out progress")

    args = parser.parse_args()

    if input(f"Directory is set to: {args.directory}\nType 'y' to continue: ") != "y":
        sys.exit("User aborted the operation.")

    func = list_files if args.choice == "list" else move_files

    compare(func)

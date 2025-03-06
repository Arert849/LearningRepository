import mimetypes
import argparse
import shutil
import sys
from collections import defaultdict
from typing import Callable
from pathlib import Path
from logger.logger import get_logger


logger = get_logger(__name__)


def find_folder(path: Path) -> Path:
    """ This function should find the designated folder """
    paths = list(Path.cwd().rglob(str(path)))
    if not paths:
        print(f"No folder {path} found\nExiting...")
        logger.warning(f"Folder {path} not found in {Path.cwd().relative_to(Path().cwd().parent)}")
        sys.exit(1)

    print(f"\nPlease confirm folder selection:")
    for i, path in enumerate(paths, 1):
        print(f"\t{i}: {path}")
    print(f"\t0: To abort the operation.")

    logger.debug("Waiting on user input.")
    choice = int(input("\nPlease select a folder by number: "))

    if choice > len(paths) or choice < 0:
        logger.debug(f"User has selected an out of range index.")
        print(f"Index does not exist. Please try again.")
        find_folder(path)
    elif choice == 0:
        logger.debug("User has elected to abort")
        print("Exiting...")
        sys.exit(0)

    return paths[choice-1]


def find_files(path: Path) -> list | None:
    """ Find files in the folder and subfolders """
    file_list = []
    unknown_list = []
    files = list(path.rglob("**/*"))

    if not files:
        print(f"No files found at: {path.relative_to(path.parent.parent)}\nExiting...")
        logger.warning(f"Nothing found at {path.relative_to(path.parent.parent)}")
        sys.exit(1)

    mtypes = mime_types()
    for file in files:
        file: Path

        if not file.is_file():
            continue

        if file.parent in ("audio", "video", "text", "unknown"):
            continue

        suffix_type = mtypes.get(file.suffix, "unknown")

        if suffix_type == "ignore":
            logger.debug(f"On ignore list: {file.relative_to(path)}")
            continue

        if suffix_type == "unknown" and args.unknown != "copy":
            logger.debug(f"Ignore unknown ext: {file.relative_to(path.parent)}")
            continue

        if suffix_type == "unknown":
            mtypes[file.suffix] = "unknown"
            logger.debug(f"Adding ext: {file.suffix} to unknown mimetypes.")

            unknown_list.append(file)
            logger.debug(f"Appended to unknown_list: {file.relative_to(path.parent)}")
            continue

        file_list.append(file)

    files = defaultdict(list[Path])
    for file in file_list:
        files[file.name.lower()].append(file)
        logger.debug(f"Appended {file} to {file.name.lower()} dictionary key.")

    unknown = defaultdict(list[Path])
    for file in unknown_list:
        unknown[file.name.lower()].append(file)

    return [files, unknown, mtypes]


def mime_types() -> dict:
    """ Construct a list of applicable mimetypes """
    files: dict = {}
    for ext, mtype in mimetypes.types_map.items():
        if "application" in mtype or ext.startswith(".py"):
            files[ext] = "ignore"
            logger.debug(f"Assigned - {ext}: {mtype} to ignore list.")
            continue
        else:
            files[ext] = mtype.split("/")[0]
            logger.debug(f"Assigned - {ext}: {mtype} to {mtype.split('/')[0]}")
    logger.info("Done construction of mimetype dict.")
    return files


def move_file(destination: Path, file: Path):
    """ Move the file to the new location """
    try:
        if not destination.parent.exists():
            destination.parent.mkdir()
            logger.info(f"Created directory: {destination.parent.stem}")
        file.rename(destination)

    except PermissionError as err:
        # Maybe there's a way to figure out which folder caused the exception
        print("Lacking permissions to progress.")
        logger.error(f"Permission denied: {err}")


def copy_file(destination: Path, file: Path):
    """ Copy the file to the new location"""
    try:
        if not destination.parent.exists():
            destination.parent.mkdir()
            logger.info(f"Created directory: {destination.parent.stem}")
        shutil.copy2(file, destination)

    except PermissionError as err:
        print("Lacking permissions to progress.")
        logger.error(f"Permission denied: {err}")


def sort_file(path: Path, func: Callable[[Path, Path], None]):
    """ The main sorting function """
    files_dict, unknown, mtypes = find_files(path)   # Returns a dict in format: file_name: [path_list]
    for name, files in files_dict.items():
        width = len(str(len(files)))    # Width for zero filling

        for i, file in enumerate(files):
            file: Path
            name = f"{file.stem}_{i:0{width}d}{file.suffix}"
            folder = mtypes[file.suffix]
            destination = path / folder / name if args.flatten else file.parent / folder / name
            func(destination, file)  # Move or copy function
            logger.info(f"Used {func.__name__} on: {file.relative_to(path.parent)}")

    if unknown:
        for name, files in unknown.items():
            width = len(str(len(files)))

            for i, file in enumerate(files):
                file: Path
                name = f"{file.stem}_{i:0{width}d}{file.suffix}"
                folder = mtypes[file.suffix]
                destination = path / folder / name if args.flatten else file.parent / folder / name
                copy_file(destination, file)
                logger.debug(f"Copied unknown file: {file}")

    print("Finished operation\nExiting...")
    logger.info("Finished the operation")
    sys.exit(0)


if __name__ == "__main__":
    """ main function """
    # Parsers
    parser = argparse.ArgumentParser(description="File Organizer: defaults to CWD, --folder --copy, --flatten")
    parser.add_argument("--path", "-p", default=Path().cwd(), help="Folder to sort. Defaults to current working dir.")
    parser.add_argument("--copy", "-c", action="store_true", help="Whether to copy the files instead")
    parser.add_argument("--flatten", "-f", action="store_true", help="Flatten to main path or sort subfolders?")

    parser.add_argument(
        "--unknown", "-u", choices=["ignore", "copy"], default="ignore", help="Handling of unknown files."
    )

    args = parser.parse_args()

    if not Path(args.path).is_absolute():
        args.path = find_folder(args.path)

    action = copy_file if args.copy else move_file

    sort_file(Path(args.path), action)

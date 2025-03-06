import argparse
import csv
import difflib
import sys
import zipfile
from datetime import datetime
from pathlib import Path
# TODO
#    DirSnap v1.0.1
# STRIKE    Tool to take a snapshot of a directory
#           Save report.txt and compare with current directory structure
#           Save metadata along with snapshot
#           make a compressed backup
#           restore from backup
#           change to csv reader
# TODO      Store metadata like snapshot time inside manifest.json
#           Change to a rolling backup of 5 files
#           change restore to offer choice between available backups
#           add a verbose flag for detailed logging


def save_snap(dirpath: Path):
    """ Save snapshot of directory structure to report.txt """
    try:
        if not dirpath.exists() or not dirpath.is_dir():
            raise FileNotFoundError(f"Path does not exist or is not a directory: {dirpath}")

        file = Path("report.txt")
        with file.open("w", encoding="utf-8") as file:
            for path in dirpath.rglob("*"):
                file.write(f"{path},{path.stat().st_size},{datetime.fromtimestamp(path.stat().st_mtime)}\n")

    except FileNotFoundError as e:
        print(e)

    except PermissionError as e:
        print(f"Permission denied: {e}")


def compare(dirpath: Path, file: Path):
    """ Compare snapshot file with current directory structure """
    try:
        if not dirpath.exists() or not dirpath.is_dir():
            raise FileNotFoundError(f"Path does not exist or is not a directory: {dirpath}")
        if not file.exists():
            raise FileNotFoundError("Snapshot file does not exist.")

        lines = []
        with file.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                path, size, mtime = row
                lines.append(f"{path},{size},{mtime}")

        dirstruct = []
        for path in (dirpath.rglob("*")):   # Makes a list of current structure of target directory
            path: Path
            line = f"{path},{path.stat().st_size},{datetime.fromtimestamp(path.stat().st_mtime)}"
            dirstruct.append(line)

        if dirstruct == lines:
            sys.exit("No changes since snapshot.\nExiting...")
        else:
            for line in difflib.context_diff(lines, dirstruct):
                print(line)
    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: ({type(e).__name__}) {e}")


def backup(dirpath: Path):
    """ Backs up the directory as a zip """
    try:
        if not dirpath.exists() or not dirpath.is_dir():
            raise FileNotFoundError(f"Path does not exist or is not a directory: {dirpath}")

        backupdir = dirpath.parent / "backup"
        backupdir.mkdir(exist_ok=True)

        name = f"{dirpath.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"

        with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for path in dirpath.rglob("*"):
                zip_file.write(path, arcname=path.relative_to(dirpath.parent))
            zip_file.close()

        backupdir = backupdir / name
        Path(name).rename(backupdir)

    except FileNotFoundError as e:
        print(e)

    except PermissionError as e:
        print(f"Permission denied: {e}")

    except Exception as e:
        print(f"Unexpected error: ({type(e).__name__}) {e}")


def restore(dirpath: Path):
    """ Restore file from backup"""
    try:
        backupdir = dirpath.parent / "backup"
        if not backupdir.exists():
            raise FileNotFoundError(f"There is no backup directory in. {dirpath.parent}")
        path = next(backupdir.iterdir(), None)
        if not path:
            raise FileNotFoundError(f"There are no backups in {dirpath.parent / 'backup'}")

        with zipfile.ZipFile(path, "r") as zip_file:
            zip_file.extractall(dirpath)

    except FileNotFoundError as e:
        print(e)

    except PermissionError as e:
        print(f"Permission denied: {e}")

    except Exception as e:
        print(f"Unexpected error: ({type(e).__name__}) {e}")


def main():
    """ Main function """
    parser = argparse.ArgumentParser(description="DirSnap tool - Snapshot the directory or compare with saved snapshot")
    parser.add_argument("directory", type=Path, help="Directory location")

    subparsers = parser.add_subparsers(dest="command", help="Available operations: save, compare, backup, restore.")
    subparsers.add_parser("save", help="Saves a snapshot of the directory")
    subparsers.add_parser("compare", help="Compares the snapshot to the directory.")
    subparsers.add_parser("backup", help="Makes a compressed zipfile backup in the backup folder.")
    subparsers.add_parser("restore", help="Restores the folder from backup")

    args = parser.parse_args()

    args.directory = Path(args.directory)

    match args.command:
        case "save":
            save_snap(args.directory)

        case "compare":
            compare(args.directory, Path("report.txt"))

        case "backup":
            backup(args.directory)

        case "restore":
            restore(args.directory)

        case _:
            sys.exit("Please type python DirSnap.py -help")


if __name__ == "__main__":
    main()

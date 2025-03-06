import argparse
import os
import re
from collections import Counter
from pathlib import Path

# TODO: Functionality and Feature improvement
# ---   Numerical processing functionality
#           Sum the numbers
#           Add a line by line option
#           Choose between integers, floats, or both
#
# ---   Logging system for debugging
#
# ---   Enhanced search functionality
#           Wild card searches
#
# ---   Batch File Processing
#           Handle results per file


class FileProcessingError(Exception):
    """ Custom exception for file errors """
    pass


def find_path(file_path: str) -> Path:
    """ Find the file path """
    path = Path(file_path)

    if path.exists():
        return path

    parent_dir = Path(__file__).resolve().parent
    matches = list(parent_dir.rglob(path.name))

    if not matches:
        raise FileProcessingError(f"File not found: {path}")

    elif len(matches) > 1:
        print("Multiple files found:")
        for i, match in enumerate(matches, 1):
            print(f"{i}: {match}")
        try:
            choice = int(input("Select file by number: ")) - 1
            path = matches[choice]

        except (ValueError, IndexError):
            raise FileProcessingError("Invalid selection.")
    else:
        path = matches[0]

    return path


def read_file(file_path: Path) -> list:
    """ Read from file and split into list of lines """
    lines = file_path.read_text(encoding="utf-8").splitlines()
    return lines


def write_file(file_path: Path, lines: list, line_break=os.linesep):
    """ Write a list of lines to the file """
    with file_path.open("wb") as file:
        file.write(bytes(line_break.join(lines), "utf-8"))
    print(f"Saved to {file_path}")


def count_file(file_path: Path) -> list:
    """ Count the lines, words, and characters in the file """
    lines = read_file(file_path)
    words = sum(len(re.findall(r"\b\w+\b", line)) for line in lines)
    chars = sum(len(line) for line in lines)

    return [("Lines", len(lines)), ("Words", words), ("Chars", chars)]


def search_file(file_path: Path, query: str, case_sensitive=True) -> list:
    """ Search the file for a string and return the occurrence count and lines """
    lines = read_file(file_path)
    flag = 0 if case_sensitive else re.IGNORECASE
    regex = re.compile(rf"\b{re.escape(query)}\b", flag)

    return [(i + 1, line) for i, line in enumerate(lines) if regex.search(line)]


def find_replace(file_path: Path, query: str, repl="", case_sensitive=True, overwrite=True):
    """ Find the query in the file and replace it with the repl string """
    lines = read_file(file_path)
    flag = 0 if case_sensitive else re.IGNORECASE
    regex = re.compile(rf"\b{re.escape(query)}\b", flag)

    new_lines = [regex.sub(repl, line) for line in lines]
    out_path = file_path if overwrite else (Path(__file__).resolve().parent / "modified_sample_files" / file_path.name)
    write_file(out_path, new_lines)


def remove_duplicates(file_path: Path, case_sensitive=True, list_only=True, remove_all=True, overwrite=True):
    """ Find the duplicate strings and deal with them accordingly """
    lines = read_file(file_path)
    counts = Counter([line if case_sensitive else line.lower() for line in lines])
    if list_only:
        return [(line, count) for line, count in counts.items() if count > 1]

    new_lines = [line for line in lines if (counts[line if case_sensitive else line.lower()] == 1 or not remove_all)]
    out_path = file_path if overwrite else (Path(__file__).resolve().parent / "modified_sample_files" / file_path.name)
    write_file(out_path, new_lines)


def file_clean(file_path: Path, line_break: str, remove_indent=False, keep_spaces=False, remove_empty=True,
               overwrite=True):
    """ Clean the file according to flags """
    lines = read_file(file_path)
    new_lines = []
    for line in lines:
        new_line = line.rstrip()  # Strip the line from the right.

        if remove_empty and not new_line:
            continue  # Remove the empty line by starting next iteration

        match_obj = re.search(r"\S", line)  # Finds first non whitespace character.
        pos = 0 if remove_indent or not match_obj else match_obj.start()

        if not keep_spaces:
            new_line = line[:pos] + " ".join(line[pos:].split())  # Force singular space between words.

        new_lines.append(new_line)

    out_path = file_path if overwrite else (Path(__file__).resolve().parent / "modified_sample_files" / file_path.name)
    write_file(out_path, new_lines, line_break)


def extract_numbers(file_path: Path) -> list:
    lines = read_file(file_path)
    result = []

    for i, line in enumerate(lines):
        nums = []
        if not re.search(r"\d", line):
            continue
        parts = re.split(r"[,\s]", line)
        for part in parts:
            if re.fullmatch(r"\d+(?:\.\d+)?", part):
                nums.append(part)
        result.append((i+1, nums))
    return result


def main():
    """ Main function, where the parsers are <3 """
    # Main parser
    parser = argparse.ArgumentParser(description="File Processing Tool")
    parser.add_argument("file", help="Name of the file.")

    # Sub Parsers
    subparsers = parser.add_subparsers(dest="command", help="Available operations.")

    # Count function parser
    subparsers.add_parser("count", help="Count the lines, words, and characters.")

    # Search function parser
    search_parser = subparsers.add_parser("search", help="Find the query and it's lines.")
    search_parser.add_argument("query", help="The string to search for.")
    search_parser.add_argument("--case_sensitive", "-cs", action="store_true", help="Case sensitive search.")

    # Find and replace parser
    replace_parser = subparsers.add_parser("replace", help="Find and replace string.")
    replace_parser.add_argument("query", help="The string to search for.")
    replace_parser.add_argument("--repl", "-r", default="", help="The replacement string.")
    replace_parser.add_argument("--case_sensitive", "-cs", action="store_true", help="Case sensitive search.")
    replace_parser.add_argument("--overwrite", "-o", action="store_true", help="Overwrite the file?")

    # Remove duplicates parser
    duplicates_parser = subparsers.add_parser("duplicates", help="Deal with duplicates in the file.")
    duplicates_parser.add_argument("--case_sensitive", "-cs", action="store_true", help="Case sensitive search.")
    duplicates_parser.add_argument(
        "--list_only", "-l", action="store_true", help="List the duplicates, don't remove."
    )
    duplicates_parser.add_argument("--remove_all", "-r", action="store_true", help="Remove all instances.")
    duplicates_parser.add_argument("--overwrite", "-o", action="store_true", help="Overwrite the file?")

    # File cleaner parser
    file_clean_parser = subparsers.add_parser("clean", help="Clean the file.")
    file_clean_parser.add_argument("--line_break", "-nl", default=os.linesep, help=r"Linebreak to use \n, \r or \r\n")
    file_clean_parser.add_argument("--remove_indent", "-r", action="store_true", help="Remove leading indentation?")
    file_clean_parser.add_argument("--keep_spaces", "-s", action="store_true", help="Ignore excessive whitespace.")
    file_clean_parser.add_argument("--remove_empty", "-e", action="store_false", help="Remove empty/whitespace lines")
    file_clean_parser.add_argument("--overwrite", "-o", action="store_true", help="Overwrite the file?")

    # Valid number extractor:
    subparsers.add_parser("number", help="Returns only valid numbers from the file.")

    args = parser.parse_args()

    file_path = find_path(args.file)

    try:
        results = None

        match args.command:
            case "count":
                results = count_file(file_path)

            case "search":
                results = search_file(file_path, args.query, args.case_sensitive)

            case "replace":
                find_replace(file_path, args.query, args.repl, args.case_sensitive, args.overwrite)
                return

            case "duplicates":
                if args.list_only:
                    results = remove_duplicates(file_path, args.case_sensitive, args.list_only, args.remove_all,
                                                args.overwrite)
                else:
                    remove_duplicates(file_path, args.case_sensitive, args.list_only, args.remove_all, args.overwrite)

            case "clean":
                file_clean(file_path, args.line_break, args.remove_indent, args.keep_spaces, args.remove_empty,
                           args.overwrite)
                return

            case "number":
                results = extract_numbers(file_path)

            case _:
                parser.print_help()

        if results:
            for key, val in results:
                print(f"{key}: {val}")

    except FileProcessingError as err:
        print(f'Error: {err}')

    except Exception as err:
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()

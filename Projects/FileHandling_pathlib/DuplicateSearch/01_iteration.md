The initial attempt was successful, but it felt poorly done.
My personal observation was:
- The lack of the main function, I enjoyed the ability to directly use parsed args, but probably bad idea.
- Could be more segmented
- I also thought I was redundantly iterating over the dict.
- verbose printing was stupidly implemented

# ChatGPT review:

Here's a detailed, code-free review of your duplicate-file-finder script, highlighting strengths, weaknesses, areas for improvement, and best practices you could adopt:

## What works well:

1. **Clear modularity:**
   - You've started breaking down the script into clearly defined functions (find_files, list_files, compare_hashes, compare). This significantly enhances readability and makes future adjustments easier.
<br><br>
2. **Chunk-based hashing:**
   - Reading files in chunks (64 KiB) for hashing is efficient memory-wise, especially beneficial when dealing with large files.
<br><br>
3. **Error Handling:**
   - Explicit handling of specific exceptions (FileNotFoundError, PermissionError) and generic exceptions shows good practice for robustness and debugging.
<br><br>
4. **Command-line interface (CLI):**
   - The use of argparse provides clear and straightforward command-line interactions. Allowing the user to confirm the operation before execution helps avoid accidental actions.
<br><br>
5. **Verbose mode:**
   - Optional verbose output (--verbose) is valuable for debugging and user transparency.

## What can be improved:

### Code Structure and Organization:
- **Main Function Encapsulation:**
  - As you've noted, encapsulating your CLI parsing logic and execution in a dedicated main() function is ideal. It increases clarity and simplifies testability.
<br><br>
- **Separation of Concerns:**
  - Currently, find_files directly accesses args.directory, coupling it closely with the global argument state. Consider passing directory paths explicitly to functions. This allows more flexible testing and reuse.

### Redundant Operations:
- **Multiple Iterations:**
    - You're iterating over files multiple times: once in find_files, once for grouping by size, and again for hashing. Grouping files by size first is a great optimization, but currently, the way dictionaries are trimmed and managed might cause slight redundancies. A single well-defined pipeline could minimize unnecessary iterations.

### Function Responsibilities:
 - **File Grouping:**
    - Consider moving the logic to group files by size into its own function rather than embedding it within the compare function. This would make your pipeline clearer:
    find_files() -> group_files_by_size() -> compute_hashes() -> find_duplicates()
<br><br>
- **Dictionary Management:**
    - Rather than trimming dictionaries by copying them (hash_dict.copy().items()), consider filtering or constructing new dictionaries directly, reducing memory overhead and improving clarity.

### User Interaction:
- **Input Prompt:** 
    - Using an input() confirmation is practical, but it limits script automation or batch processing. Offering an optional --force flag for skipping confirmation would make the script suitable for automated workflows.
<br><br>
- **Exiting Script:**
    - Exiting via sys.exit() inside your main logic is common practice, but it's typically cleaner if the script naturally finishes execution without forcing an exit, unless explicitly necessary for error states.

### Verbosity and Logging:
- **Logging instead of Print:**
    - While verbosity (print) is helpful, adopting Python's logging library would be better practice. It gives granular control over logging levels (DEBUG, INFO, ERROR, etc.) and can be easily toggled or redirected.

### Future-proofing and Extensibility:
- **Move File Placeholder:**
    - Your move_files() function is currently empty. Even as a placeholder, consider at least adding descriptive comments on intended functionality to clarify future implementation.
<br><br>
- **Testing and Testability:**
    - The current script is a bit challenging to unit test due to reliance on global arguments. Passing parameters explicitly and returning values clearly would greatly facilitate testing.

## Alternative Methods or Libraries:
- **Pathlib Enhancements:**
    - You're correctly using pathlib. To enhance further, consider leveraging built-in methods (Path.stat(), Path.read_bytes(), or Path.resolve()) more explicitly to handle edge-cases or symbolic links.
<br><br>
- **File Hashing Performance:**
    - Your chunk-based hashing is good. Alternatively, libraries like xxhash or hashlib.blake2 offer faster hashing algorithms with similar collision resistance.
<br><br>
- **File Comparison Efficiency:**
<br><br>
    - If performance becomes critical, consider using file modification timestamps (st_mtime) or other metadata for initial filtering to further reduce hashing operations.

### Overall Suggestions (summary):
- Encapsulate CLI logic in main().
- Explicitly pass arguments to functions instead of relying on global state.
- Refine function structure (group by size, hash, find duplicates).
- Reduce redundant iterations.
- Adopt Python’s logging library for verbosity.
- Add --force or similar CLI flags to facilitate automation.
- Clearly document placeholders (move_files) and intended future behaviors. 
 
Your approach is solid and clean, and with these refinements, you can achieve even clearer, more efficient, and testable code.
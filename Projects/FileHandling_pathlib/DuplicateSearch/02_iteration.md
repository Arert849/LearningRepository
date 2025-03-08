I ended up just writing from scratch rather than rewriting the stuf. 
Proved to be more efficient than constantly going back and forth on decisions.
Who would have thought?

I ended up importing the traceback module since I felt it'd fit the verbose flag...

I like this more apart from the try except blocks.
I find they make things more difficult to read. I might end up wrapping the entire for loop with it.

It's mainly the return in compute hashes function, it looks... wrong below the except blocks.

# ChatGPT review:

Here's a high-level review of the updated script, focusing on design, readability, and best practices—without showing any code:

## Strengths
1. **Centralized Verbose Printing**
    - Your print_verbose function now keeps the verbosity checks out of the main logic, resulting in cleaner, more readable functions.
<br><br>
2. Dedicated Main Function
   - You’ve nicely wrapped argument parsing and workflow control in main(), which is more modular and easier to maintain/test.
<br><br>
3. **Clear Workflow Pipeline**
    - find_duplicates manages each step in turn:
      - Gather files
      - Group by size
      - Compute hashes
    <br><br>
    - This “pipeline” style is easy to read and straightforward to follow.
<br><br>
4. **Separation of Concerns**
    - list_files and move_files are now separate functions, ready for future expansion (e.g., actual move logic).

    - Error handling is mostly contained in the relevant steps, so each function stays focused on its main job.
<br><br>
5. **Use of a Global Verbose Flag**
    - While not everyone loves globals, it keeps the function signatures clean for a script of this scope. This is acceptable for smaller utilities where a dedicated logging system might be overkill.
<br><br>
6. **Better Chunk Size**
    - 1 MiB chunks are a sensible balance for hashing large files.

## Potential Enhancements

1. **Move Implementation**

    - Currently, move_files is a placeholder. When you do implement it, make sure to handle edge cases (e.g., conflicts with existing files, directory creation if needed).
<br><br>
2. **try-except Granularity**
    - You have broad exception handling for each step, which is good for preventing crashes. However, you might eventually want to refine these blocks so that each exception provides more specific messages or retries.
    - In particular, if you catch an unexpected exception (like Exception), logging it alongside a stack trace is helpful for debugging.
<br><br>
3. **Returning Early Instead of Raising**
    - In find_duplicates, if no duplicates are found, you raise a generic exception. For clarity, you might prefer just returning an empty dict or None with a clear debug message. The rest of the code can then decide what to do if it receives None or an empty dict.
<br><br>
4. **Dictionary vs. More Structured Objects**
    - Storing paths grouped by hash in a dictionary is perfectly fine. As the project grows, you might consider a class or namedtuple if you need more structured data with additional fields. For now, though, a dictionary of sets is a neat approach.
<br><br>
5. **Reconsider the Global Variable**
    - While the global VERBOSE is fine for a small script, you might eventually prefer passing a verbose parameter around or using Python’s built-in logging to control verbosity at different log levels. It’s a minor point, but worth considering if your script grows larger.
<br><br>
6. **Testability**
    - Because you now have a proper main() function, it should be fairly simple to write unit tests for find_files, group_files_by_size, etc. You might add docstrings or comments that specify expected edge-case behavior, which will guide future testing.

## Overall Verdict
Your improvements have made the script more maintainable, readable, and robust. The flow of data—finding files, grouping by size, computing hashes, and listing or moving—feels more intuitive now. With just a bit more refinement in handling exceptions and the future move functionality, you’ll have a versatile and polished tool.

These are a bit of a pain to format.
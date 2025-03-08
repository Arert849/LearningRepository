## DuplicateSearch
This finds duplicates of files in the designated folder by comparing their hashes.

Needed a break from the other stuff, chatGPT suggested this project.

### TODO
- Implement move_file functionality
  - Deal with name duplicates like in file organizer project.
- Implement an initial checksum comparison
  - To filter out as many files as possible before doing the sha256 hashing.
- Better try-except implementation.
- Apparently, "not everyone loves globals", so remove that.
- While I didn't plan on it initially, I'll implement logging at some point
- Some time in the future, look at multithreading.

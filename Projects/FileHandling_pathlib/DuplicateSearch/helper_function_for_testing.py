import random
from pathlib import Path

parent_path = Path("test_folder")

if not parent_path.exists():
    parent_path.mkdir()

content = [
    "test", "file", "content", "for", "hash", "duplicate", "very", "stupid", "method", "guaranteed"
]

for i in range(30):
    path = parent_path / f"file_{i}.txt"
    with path.open("w") as f:
        if i < 3:
            f.write(content.pop())
        else:
            f.write(content[random.randint(0, len(content)-1)])


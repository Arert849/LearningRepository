import random
from pathlib import Path

path = Path().cwd() / "test_folder"

words = [
    "apple", "banana", "chocolate", "dragon", "elephant", "forest", "galaxy", "horizon", "island", "jigsaw",
    "kangaroo", "labyrinth", "meteor", "nebula", "octopus", "puzzle", "quantum", "rocket", "symphony", "tornado",
    "avalanche", "blueprint", "cascade", "dandelion", "emerald", "fossil", "glacier", "harmony", "illusion", "jubilee",
    "kaleidoscope", "lighthouse", "mirage", "nocturnal", "oasis", "pendulum", "quasar", "riddle", "serendipity",
    "treasure", "utopia", "voyager", "whirlpool", "xylophone", "yonder", "zephyr", "alchemist", "basilisk", "crimson",
    "destiny", "evergreen", "firefly", "gondola", "hologram", "incognito", "javelin", "knapsack", "lantern",
    "moonlight", "nucleus", "orchestra", "paradox", "quicksilver", "resonance", "silhouette", "twilight", "undertow",
    "vortex", "wanderlust", "xenon", "yearning", "zenith", "astronaut", "blizzard", "cataclysm", "dystopia", "eclipse",
    "fable", "gargoyle", "helios", "infinity", "jackpot", "keystone", "labyrinthine", "monolith", "nebulous",
    "obsidian", "phantom", "quintessence", "runestone", "spectrum", "tesseract", "unicorn", "volcano", "whisper",
    "xenophile", "yellowtail", "zodiac", "artifact", "borealis"
]

folders = [
    "Test", "Module", "Maybe"
]
ext = [
    ".mp3", ".mpeg", ".png", ".bmp", ".jpeg", ".poiasdj", ".txt", ".py", ".test", ".info", ".md", ".app",
    ".exe", ".no", ".unknown"
]

paths = []

for folder in folders:
    for name in words:
        test = path / folder / f"{name}{ext[random.randrange(len(ext)]}"
        paths.append(test)

for path in paths:
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text("")

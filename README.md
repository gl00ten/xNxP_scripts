# xNxP_scripts

Consolidated collection of personal scripts, experiments, notes, and one-offs.

Originally split across `messy_area/` and `scripts/`. Now organized into a single directory tree with sensible names, categories, fixes, and documentation.

## Directory Layout

- **scripts/** — Polished, (somewhat) reusable tools. Add to PATH or call directly.
- **experiments/** — Toys, visualizations, simulations, curiosities.
- **legacy/** — Old heavy one-shot installers (historical).
- **notes/** — Text notes and old manifests.
- **configs/** — Config snippets (PulseAudio etc.).
- **archive/** — The "perfectly dumb" and low-value items (with explanations).

## Perfectly Dumb / Archived Items

These were moved to `archive/` with headers explaining the problems:

| Original location                  | New name                              | Why dumb / archived |
|------------------------------------|---------------------------------------|---------------------|
| scripts/clickABunchOfTimes.bash    | click_spam_mouse.sh                   | Hardcoded coords, 3000 click spam loop. No args, no value. |
| scripts/piratebay_parser.py        | piratebay_magnet_scraper.py           | Brittle The Pirate Bay scraper + auto torrent client launcher. Legally risky + will break constantly. |
| messy_area/compressDecompressFileLineByLine.py | line_by_line_zlib_demo.py | Per-line zlib on text with hardcoded files. Doesn't do useful compression. |
| messy_area/auto_ssh                | auto_ssh_one_liner.txt                | Single personal reverse-tunnel command line. Belongs in ssh config. |
| messy_area/moveFilesWithAutoRename.py | move_jpegs_with_rename.py          | Hardcoded paths + buggy collision rename logic (produced `name-.ext`). |
| scripts/findPairsOfSimilarNamesInList.py | find_similar_filenames_hardcoded.py | O(n²) on hardcoded dir only. Inefficient and inflexible. |
| messy_area/generateRandomWords.py  | generate_random_words_broken.py       | Trivial generator + `buildWordStartedWith(letter)` completely ignores the letter param. |

Other borderline cases kept in `experiments/` or `legacy/` for nostalgia/reference:
- `number_cheat_simulation.py` (confusingly named experiment)
- The old install scripts (very era-specific)

## Current Scripts (scripts/)

| Script                              | Description |
|-------------------------------------|-------------|
| `clear_free_space.sh`               | Zero-fill free space on a filesystem (classic `cat /dev/zero` trick). Run in target dir. |
| `correct_image_dates.sh DIR...`     | Walk images, if missing CreateDate or it looks newer than mtime, set EXIF CreateDate from mtime and restore file mtime. Requires `exiftool`. |
| `download_qbittorrent_search_plugins.py` | Scrape the qbittorrent unofficial plugins wiki for `.py` links. Pipe to `xargs wget`. |
| `remove_duplicates_from_lists.py file1 file2` | Set operations between two newline lists. Shows only-in-A, only-in-B, intersection. |
| `reverse_video_segments.sh [GLOB]`  | Split videos (default `*.MTS`) into 30s segments, reverse the segments, concat in reverse order to produce time-reversed effect. Produces `reversed/joined.mp4`. Needs `ffmpeg`. |
| `reverse_video_from_dir_list.sh [listfile]` | Run the above in each directory listed in a text file. |
| `scramble_text.py "phrase..."`      | "Human readable" scrambler: keeps first+last letters of each word, shuffles middles. Also reads stdin. Surprisingly readable. |
| `scramble_text.html`                | Same scrambler as a self-contained browser toy (no Python needed). |

## Experiments

- `round_robin_tournament.py Team1 Team2 ...` — Generates shuffled round-robin rounds/pairs. Supports `--teams-file` and `--seed`.
- `sieve_of_eratosthenes_gui.py` — Step-by-step interactive PyQt5 visualization of the Sieve of Eratosthenes. Fun educational toy. `pip install PyQt5`.
- `number_cheat_simulation.py` — Monte Carlo of two weird "higher number" strategies.

## Usage Tips

Make `scripts/` available:

```bash
export PATH="$HOME/workspace/xNxP_scripts/scripts:$PATH"
```

Or symlink the ones you like into `~/bin`.

Many of the original scripts had **hardcoded paths** and no argument handling. Most have been updated to accept arguments or at least document the old behavior.

## License / History

Individual pieces carried either Unlicense or GPLv3. These are tiny personal tools; treat them as public domain / CC0 unless a specific file states otherwise.

The two original git repos were small and have been flattened into this layout (sub-.gits removed).

## What Was Done

- Reviewed every file.
- Consolidated from two directories into one logical tree.
- Renamed for clarity (fixed "pesudoRandomize", descriptive names, extensions standardized).
- Added shebangs, usage, argument handling, and bug fixes to the keepers.
- Clearly labeled the dumb ones in `archive/`.
- Updated READMEs and added this master index.

Enjoy the less messy collection.
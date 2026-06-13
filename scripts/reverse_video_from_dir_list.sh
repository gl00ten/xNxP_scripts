#!/bin/bash
#
# reverse_video_from_dir_list.sh
# Run the segment-reverse process in each directory listed in a file.
#
# Usage: ./reverse_video_from_dir_list.sh [dir_list.txt]
# Default list file: dir_list.txt (one absolute or relative dir per line)

set -euo pipefail

LIST_FILE="${1:-dir_list.txt}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKER="$SCRIPT_DIR/reverse_video_segments.sh"

if [ ! -f "$LIST_FILE" ]; then
  echo "error: list file not found: $LIST_FILE" >&2
  exit 1
fi
if [ ! -x "$WORKER" ]; then
  echo "error: worker script not found or not executable: $WORKER" >&2
  exit 1
fi

while IFS= read -r d || [ -n "$d" ]; do
  [ -z "$d" ] && continue
  if [ ! -d "$d" ]; then
    echo "warning: skipping non-directory: $d" >&2
    continue
  fi
  echo ">>> Processing $d"
  ( cd "$d" && "$WORKER" )
done < "$LIST_FILE"

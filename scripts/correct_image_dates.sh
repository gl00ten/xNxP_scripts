#!/bin/bash
#
# correct_image_dates.sh
# For images missing a CreateDate (or with future CreateDate), set EXIF CreateDate
# from the file's mtime. Restores mtime afterwards.
#
# Usage: ./correct_image_dates.sh /path/to/photos [another/dir ...]
# Requires: exiftool
#
# WARNING: This modifies files in place (-overwrite_original).

set -euo pipefail

if ! command -v exiftool >/dev/null 2>&1; then
  echo "error: exiftool is required" >&2
  exit 1
fi

if [ $# -eq 0 ]; then
  echo "Usage: $0 DIR [DIR...]" >&2
  exit 1
fi

for folder_path in "$@"; do
  if [ ! -d "$folder_path" ]; then
    echo "warning: not a directory: $folder_path" >&2
    continue
  fi

  find "$folder_path" -type f \( \
      -iname '*.jpg' -o -iname '*.jpeg' -o \
      -iname '*.png' -o -iname '*.gif' -o \
      -iname '*.heic' -o -iname '*.tiff' -o -iname '*.tif' \
    \) -print0 | while IFS= read -r -d '' file; do

    mtime=$(stat -c %Y "$file")   # epoch for reliability
    mtime_human=$(date -d "@$mtime" '+%Y:%m:%d %H:%M:%S')

    # Current CreateDate (if any)
    create_date=$(exiftool -s3 -CreateDate "$file" 2>/dev/null || true)

    needs_fix=0
    if [ -z "$create_date" ]; then
      needs_fix=1
    else
      # Parse exif date to epoch if possible; fall back to lexical
      create_epoch=$(date -d "${create_date//:/-}" '+%s' 2>/dev/null || echo 0)
      if [ "$create_epoch" -gt "$mtime" ] 2>/dev/null || [ "$create_epoch" = 0 ]; then
        needs_fix=1
      fi
    fi

    if [ "$needs_fix" = 1 ]; then
      echo "fixing: $file  (mtime -> CreateDate: $mtime_human)"
      exiftool -overwrite_original -CreateDate="$mtime_human" "$file" >/dev/null
      touch -c -d "@$mtime" "$file"
    fi
  done
done

#!/bin/bash
#
# reverse_video_segments.sh
# For each video in current dir (default *.MTS), split into ~30s segments,
# reverse each segment, concat the reversed segments (in reverse segment order),
# then concat those per-original reversed clips into one final "joined.mp4".
#
# This produces a "time-reversed" effect across the whole recording.
#
# Usage:
#   cd /path/with/videos && /path/to/reverse_video_segments.sh [GLOB]
#   Example: reverse_video_segments.sh '*.mp4'
#
# Requirements: ffmpeg
#
# Output: reversed/joined.mp4  (plus intermediate per-file clips)

set -euo pipefail

GLOB="${1:-*.MTS}"

shopt -s nullglob nocaseglob
videos=( $GLOB )
shopt -u nullglob nocaseglob

if [ ${#videos[@]} -eq 0 ]; then
  echo "No files matched: $GLOB" >&2
  exit 1
fi

mkdir -p reversed/before_join

for src in "${videos[@]}"; do
  base=$(basename "$src")
  echo ">>> Reversing segments of $src"

  workdir="split.$$"
  mkdir -p "$workdir/reverse"

  # 1. segment the original (copy streams)
  ffmpeg -hide_banner -loglevel warning -i "$src" -c copy -map 0 -segment_time 00:00:30 -f segment \
    -reset_timestamps 1 "$workdir/output%03d.mp4"

  # 2. reverse each segment
  for seg in "$workdir"/output*.mp4; do
    [ -e "$seg" ] || continue
    ffmpeg -hide_banner -loglevel warning -i "$seg" -crf 20 -vf reverse "$workdir/reverse/$(basename "$seg")"
  done

  # 3. concat the reversed segments BACKWARDS (to get overall reverse)
  concat_list="$workdir/to_concat.txt"
  for seg in $(ls "$workdir/reverse"/output*.mp4 2>/dev/null | sort -r); do
    echo "file '$seg'" >> "$concat_list"
  done

  if [ -s "$concat_list" ]; then
    ffmpeg -hide_banner -loglevel warning -f concat -safe 0 -i "$concat_list" -c copy \
      "reversed/before_join/${base}.mp4"
  fi

  rm -rf "$workdir"
done

# 4. concat all the per-original reversed clips, again in reverse filename order
#    (so the overall sequence is reversed)
final_concat="reversed/to_concat_final.txt"
> "$final_concat"
for f in $(ls reversed/before_join/*.mp4 2>/dev/null | sort -r); do
  echo "file '$f'" >> "$final_concat"
done

if [ -s "$final_concat" ]; then
  ffmpeg -hide_banner -loglevel warning -f concat -safe 0 -i "$final_concat" -c copy reversed/joined.mp4
  echo "Created: reversed/joined.mp4"
fi

rm -f "$final_concat"
rm -rf reversed/before_join

echo "Done."

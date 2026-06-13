#!/bin/sh
#
# clear_free_space.sh
# Classic "fill free space with zeros then delete" to allow better compression
# or to overwrite deleted data on HDDs (not reliable on SSDs/flash).
#
# Run in the filesystem you want to "clear". Creates a huge temporary file.
# Use with care: will consume all free space temporarily.

set -e
echo "Writing zeros to ./file.zero until disk is full..."
cat /dev/zero > ./file.zero || true
sync
rm -f ./file.zero
echo "Done. Free space should now be zeroed."

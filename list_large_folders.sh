#!/bin/bash

# This script lists the largest folders in the specified directory
# Usage: ./list_large_folders.sh /path/to/directory

DIR=${1:-.}

du -ah $DIR | sort -rh | head -n 20

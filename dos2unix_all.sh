#!/usr/bin/env bash
# find all files in folder (recursively) and convert them to "unix" format
find /home/$USER/files_to_convert -type f -print0 | xargs -0 dos2unix

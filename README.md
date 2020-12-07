# smashdupes-007
A tool that removes duplicate files based on its checksum.

# Installation
```
pip3 install termcolor
git clone https://github.com/killeroo7/smashdupes-007
cd smashdupes-007 && chmod +x smashDupes-007.py
ln -s $(pwd)/smashDupes-007.py /usr/local/bin/smashDupes-007
```

# USAGE

▶ Remove Duplicates in the current directory

> smashDupes-007

▶ Remove Dupes in a specified directory

> smashDupes-007 -d /path/to/remove/dupefiles


# FLAGS
```
  -v, --verbose         Print filenames that are removed
  -d DIRECTORY, --dir DIRECTORY
                        Directory to Delete Files
  -s, --silent          Don't Ask fir confirmation
```

# Universal Shortcut file

This Python script creates a "universal shortcut" file which hybrid Bash-Batch script that can be used in Linux and Windows to open a file or execute a program. Specifically, it might be useful for launchers in removable media, if the filesystem supports file permissions (FAT32 does not) and files in cloud-storage services such as Dropbox.

While Linux and Windows support symbolic links, when the target file is an executable, certain scripts and programs present problems when executed through a symbolic link, as the working directory is expected to be the directory containing the executable  and not the directory with the symbolic link.

This universal shortcut consist in text file with bash code and bat code commented in such a way that the code for a different OS is ignored.

## Usage
The shortcut can be created either from Linux or Windows.

1. From the Directory where you want to create the shortcut:
2. Execute `python3 mk_unishortcut.py <targetpath>`
3. A file called `targetpath.cmd` will be created in the current Directory

The **targetpath** is the path to the target, and the target can be either a file or a directory.

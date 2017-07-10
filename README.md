# Universal Shortcut file

I wrote this to create a shortcut file that can be used in Linux and Windows, a universal shortcut. Specifically, it might be useful for launchers in removable media, and files in cloud-storage services such as Dropbox.

While Windows supports Symbolic Links these are not always useful as the working directory is the one where the symbolic link is and not where the target is located.

This universal shortcut consist in text file with bash code and bat code commented in such a way that the code for a different OS is ignored.

Some of the properties are:
It stores the relative path from the shortcut to the target, then, if any of this files is moved the shortcut is broken

## Usage
The shortcut can be created either from Linux or Windows.

1. From the Directory where you want to create the shortcut:
2. Execute `python3 mk_unishortcut.py <targetpath>`
3. A file called `targetpath.cmd` will be created in the current Directory

A previous unishortcut if existent, will be replaced.  
The **target** can be either a file or a directory.

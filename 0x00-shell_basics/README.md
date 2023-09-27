#!/bin/bash
### 1. `generate_magic.sh`

- **Purpose**: Generates a magic file (`school.mgc`) for detecting School data files that contain the string "SCHOOL" at offset 0.
- **Usage**: Execute `./generate_magic.sh` in the terminal to create the `school.mgc` file.

### 2. `0-current_working_directory`

- **Purpose**: Prints the absolute path name of the current working directory.
- **Usage**: Execute `./0-current_working_directory` in the terminal to display the current working directory.

### 3. `1-listit`

- **Purpose**: Displays the contents list of the current directory.
- **Usage**: Execute `./1-listit` in the terminal to list the contents of the current directory.

### 4. `2-bring_me_home`

- **Purpose**: Changes the working directory to the user's home directory without using any shell variables.
- **Usage**: Execute `./2-bring_me_home` in the terminal to switch to the home directory.

### 5. `3-listfiles`

- **Purpose**: Shows the contents of the current directory in long format, displaying user and group IDs numerically.
- **Usage**: Execute `./3-listfiles` in the terminal to list contents in long format.

### 6. `4-listmorefiles`

- **Purpose**: Lists the current directory's contents, including hidden files, in long format with user and group IDs displayed numerically.
- **Usage**: Execute `./4-listmorefiles` in the terminal to list all contents, including hidden files.

### 7. `5-listfilesdigitonly`

- **Purpose**: Lists the current directory's contents in long format with user and group IDs displayed numerically, including hidden files.
- **Usage**: Execute `./5-listfilesdigitonly` in the terminal to display contents with hidden files.

### 8. `6-firstdirectory`

- **Purpose**: Creates a directory named `my_first_directory` in the `/tmp/` directory.
- **Usage**: Execute `./6-firstdirectory` in the terminal to create the `my_first_directory` folder.

### 9. `7-movethatfile`

- **Purpose**: Moves the file named `betty` from `/tmp/` to `/tmp/my_first_directory/`.
- **Usage**: Execute `./7-movethatfile` in the terminal to move the `betty` file.

### 10. `8-firstdelete`

- **Purpose**: Deletes the file named `betty` from `/tmp/my_first_directory/`.
- **Usage**: Execute `./8-firstdelete` in the terminal to delete the `betty` file.

### 11. `9-firstdirdeletion`

- **Purpose**: Deletes the directory named `my_first_directory` from the `/tmp/` directory.
- **Usage**: Execute `./9-firstdirdeletion` in the terminal to delete the `my_first_directory` folder.

### 12. `10-back`

- **Purpose**: Changes the working directory to the previous one.
- **Usage**: Execute `./10-back` in the terminal to navigate to the previous working directory.

### 13. `11-listmagic`

- **Purpose**: Lists all files and directories in the current directory, the parent of the working directory, and the `/boot` directory in long format.
- **Usage**: Execute `./11-listmagic` in the terminal to display files and directories as specified.

### 14. `12-file_type`

- **Purpose**: Prints the type of the file named `iamafile` in the `/tmp` directory.
- **Usage**: Execute `./12-file_type` in the terminal to determine the file type of `iamafile`.

### 15. `13-symbolic_link`

- **Purpose**: Creates a symbolic link named `__ls__` to `/bin/ls` in the current working directory.
- **Usage**: Execute `./13-symbolic_link` in the terminal to create the symbolic link.

### 16. `14-copy_html_files`

- **Purpose**: Copies HTML files from the current working directory to the parent directory, ensuring that files don't exist in the parent directory or are newer.
- **Usage**: Execute `./14-copy_html_files` in the terminal to copy HTML files with the specified conditions.

### 17. `15-move_uppercase_files`

- **Purpose**: Moves files that begin with an uppercase letter to the directory `/tmp/u`.
- **Usage**: Execute `./15-move_uppercase_files` in the terminal to move files as specified.

### 18. `16-clean_emacs`

- **Purpose**: Deletes files in the current working directory ending with the character `~` (tilde), commonly associated with Emacs backup files.
- **Usage**: Execute `./16-clean_emacs` in the terminal to remove such files.

### 19. `17-tree`

- **Purpose**: Creates directories `welcome/`, `welcome/to/`, and `welcome/to/s


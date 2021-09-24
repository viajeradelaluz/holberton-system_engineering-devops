# 0x01. Shell, permissions

This project is focused on learning what the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do, and Linux file permissions in general.

## Tasks Names — Files — Description

- **0. My name is Betty** — ``0-iam_betty `` — Create a script that switches the current user to the user `betty`.

- **1. Who am I** — ``1-who_am_i `` — Write a script that prints the effective username of the current user.

- **2. Groups** — ``2-groups `` — Write a script that prints all the groups the current user is part of.

- **3. New owner** — ``3-new-owner`` — Write a script that changes the owner of the file `hello` to the user `betty`.

- **4. Empty!** — ``4-empty`` — Write a script that creates an empty file called `hello`.

- **5. Execute** — ``5-execute`` — Write a script that adds execute permission to the owner of the file `hello`.

- **6. Multiple permissions** — ``6-multiple_permissions`` — Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

- **7. Everybody!** — ``7-everybody`` — Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`

- **8. James Bond** — ``8-James_Bond`` — Write a script that sets the permission to the file `hello` as follows:

  - Owner: no permission at all
  - Group: no permission at all
  - Other users: all the permissions

- **9. John Doe** — ``9-John_Doe`` — Write a script that sets the mode of the file `hello` to this:

  ```html
  -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
  ```

- **10. Look in the mirror** — ``10-mirror_permissions`` — Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.

- **11. Directories** — ``11-directories_permissions`` — Create a script that adds execute permission to all subdirectories of  the current directory for  the owner, the group owner and all other  users. Regular files should not be changed.

- **12. More directories** — ``112-directory_permissions`` — Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

- **13. Change group** — ``13-change_group`` — Write a script that changes the group owner to `school` for the file `hello
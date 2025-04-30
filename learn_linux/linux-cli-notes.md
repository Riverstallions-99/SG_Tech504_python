# Linux CLI Notes

Contents:
- [Commands](#commands)
    - [History Command](#history-command)
    - [List Directory Command](#list-directory-command)

---

## Commands
### history command
`history` gives a list of previously used commands
`!16` allows you to run a previous command from the history, using the index listed
`history -c` clears your history 


### list directory command
`ls -l` or `ll` gives a verbose list of files and directories

### curl command
`curl <url>` to fetch a website, if the end point/url is a .jpg, you can save the file using: `curl <url/<filename>.jpg> --output <filename.jpg>` or `curl <url/<filename>.jpg> > <filename.jpg>`

`cp <filename>` copy file
`rm <filename>` remove file
`mkdir <directory>` make directory
`rmdir <directory>` remove directory
`rm -r <directory>` remove directory recursively

`cd ..` change into parent directory
`cd ~` change into home directory
`cd /` change into root directory

`touch <file>` makes empty file if not exists
`head -<number> <file>` gives the top number of lines of a file
`tail -<number> <file>` gives the bottom number of lines of a file

`nl <filename>` number lines

`sudo apt update` fetches new versions of stuff on system
`sudo apt upgrade` installs the new versions of stuff on system

`sudo systemctl status <process>` gives the status of a process
`sudo systemctl restart <process>` restarts a process
`sudo systemctl is-enabled <process>` checks if a service is enabled (runs on start up)



# colove
a container of love

## usage
### prep
First, build the container:
`py colove.py -b`

Then, run the container and attach:
`py colove.py -r`

### in the container
1. `. /colove/setup/setup.sh`
2. pass in your gpg key
3. add ssh keys to your ssh-agent (TODO: fucking do this automatically)
   - `ssh-add ~/path/to/file`
4. run any deploys you want


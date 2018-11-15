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

#### deployments

1. Mojobot
   - cd to the deploy folder
   - `ansible-playbook -i hosts.yml mojo.yml --ask-vault-pass`
   - this will deploy it automatically to docker hosts. eventually i'll need to update targets
2. arke
   - cd to deploy folder
   - `ansible-playbook -i hosts arke.yml`
   - has to be deployed on same docker host as mojo. they share the `towervol` docker volume to share data
3. znc
   - cd to deploy folder
   - `ansible-playbook -i hosts.yml znc.yml`
   - currently deploys to dockerhosts datagroup. 

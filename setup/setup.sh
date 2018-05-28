#!/bin/bash
# prompt for decrypt and extract secrets
gpg --output ~/.ssh.tar --decrypt /colove/setup/secrets/ssh-secrets.tar.gpg
mkdir .ssh
7z x ~/.ssh.tar

# change default umask so that I can actually use my ssh keys
umask 077
# start up the ssh agent.
eval `ssh-agent`
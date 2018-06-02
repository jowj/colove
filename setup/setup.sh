#!/bin/bash
# change default umask so that I can actually use my ssh keys
umask 077
# prompt for decrypt and extract secrets
gpg --output ~/.ssh.tar --decrypt /colove/setup/secrets/ssh-secrets.tar.gpg
7z x ~/.ssh.tar

# start up the ssh agent.
eval `ssh-agent`

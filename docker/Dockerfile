FROM alpine:3.7
LABEL maintainer "me@jowj.net"

# make container livable
RUN apk update \
    && apk add \
        bash bash-doc \
        emacs-nox emacs-doc \
        git git-doc \
        gnupg gnupg-doc \
        groff groff-doc \
        iputils \
        man man-pages \
        openssh-client openssh-doc \
        openssl openssl-doc \
        python3 python3-doc \
        sudo sudo-doc \
        tmux tmux-doc \
    && python3 -m pip install \
        awscli \
    && apk add \
        gcc \
        linux-headers \
        make \
        musl-dev \
        python2-dev \
        python3-dev \
        libffi-dev \
        openssl-dev

# install more specific applications
RUN apk add \
        nmap nmap-doc \
        ansible ansible-doc \
    && python3 -m ensurepip \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install \
        ansible
    
CMD /bin/bash -i
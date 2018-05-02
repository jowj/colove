FROM alpine:3.7
LABEL maintainer "me@jowj.net"

ARG username=colove
ARG homedir=/home/$username

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

# configure a user
RUN addgroup -S "$username" \
    && adduser -S -G "$username" -s /bin/bash "$username" \
    
# ARG enablesudo="true"
# RUN if test "$enablesudo"; then true \
#         && echo "ENABLING PASSWORDLESS SUDO" >&2 \
#         && echo "sudo should only be enabled in development, since root privs in your container can probably be leveraged to root privs on your host" >&2 \
#         && echo "$username ALL=(ALL) NOPASSWD: ALL" > "/etc/sudoers.d/$username" \
#         && chmod 0440 "/etc/sudoers.d/$username" \
# ; fi


USER $username
WORKDIR $homedir
CMD /bin/bash -i
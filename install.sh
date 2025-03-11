#!/bin/bash

git clone https://github.com/linuxfanboy4/bash-config.git
cd bash-config

if ! command -v bash &> /dev/null; then
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        if [[ "$ID" == "ubuntu" || "$ID" == "debian" ]]; then
            apt update && sudo apt install -y bash
        elif [[ "$ID" == "centos" || "$ID" == "rhel" ]]; then
            yum install -y bash
        elif [[ "$ID" == "fedora" ]]; then
            dnf install -y bash
        elif [[ "$ID" == "arch" || "$ID" == "manjaro" ]]; then
            pacman -S --noconfirm bash
        fi
    elif [ -f /system/build.prop ] || [ -f /data/data/com.termux/files/usr/bin/bash ]; then
        pkg install bash
    fi
fi

if [ "$SHELL" != "$(which bash)" ]; then
    chsh -s "$(which bash)"
fi

cd src

echo "Bash Configuration Manager is Installed! Type \"python3 main.py\" to use it"

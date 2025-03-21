plugins = {
    "fast_aliases": "echo 'alias ll=\"ls -lah\"' >> ~/.bashrc && echo 'alias gs=\"git status\"' >> ~/.bashrc",
    "power_prompt": "echo 'export PS1=\"\\\e[32m\\\u@\\h:\\w\\$ \\\e[0m\\"' >> ~/.bashrc",
    "sys_monitor": "echo 'alias cpu=\"top\"' >> ~/.bashrc && echo 'alias mem=\"free -h\"' >> ~/.bashrc",
    "net_tools": "echo 'alias myip=\"curl ifconfig.me\"' >> ~/.bashrc && echo 'alias ports=\"netstat -tulnp\"' >> ~/.bashrc",
    "dev_shortcuts": "echo 'alias python=python3' >> ~/.bashrc && echo 'alias grep=\"grep --color=auto\"' >> ~/.bashrc",
    "custom_ls": "echo 'alias ls=\"ls --color=auto\"' >> ~/.bashrc && echo 'alias la=\"ls -A\"' >> ~/.bashrc",
    "docker_helper": "echo 'alias dps=\"docker ps\"' >> ~/.bashrc && echo 'alias dlogs=\"docker logs\"' >> ~/.bashrc",
    "git_boost": "echo 'alias gcl=\"git clone\"' >> ~/.bashrc && echo 'alias gp=\"git push\"' >> ~/.bashrc",
    "extract_tool": "echo 'extract() { case $1 in *.tar.gz) tar -xzf $1 ;; *.zip) unzip $1 ;; *) echo \"Unknown format\" ;; esac }' >> ~/.bashrc",
    "colorizer": "echo 'alias cat=\"bat\"' >> ~/.bashrc",
    "disk_tools": "echo 'alias df=\"df -h\"' >> ~/.bashrc && echo 'alias du=\"du -sh *\"' >> ~/.bashrc",
    "battery_status": "echo 'alias battery=\"upower -i $(upower -e | grep BAT)\"' >> ~/.bashrc",
    "clipboard": "echo 'alias copy=\"xclip -sel clip\"' >> ~/.bashrc && echo 'alias paste=\"xclip -o\"' >> ~/.bashrc",
    "screenshot": "echo 'alias ss=\"scrot ~/screenshot.png\"' >> ~/.bashrc",
    "uptime_monitor": "echo 'alias uptime=\"uptime -p\"' >> ~/.bashrc",
    "temp_checker": "echo 'alias temp=\"sensors\"' >> ~/.bashrc",
    "log_cleaner": "echo 'alias clean_logs=\"sudo journalctl --vacuum-time=7d\"' >> ~/.bashrc",
    "wifi_tools": "echo 'alias wifi=\"nmcli dev wifi\"' >> ~/.bashrc",
    "random_motd": "echo 'echo \"Welcome, hacker!\" | lolcat' >> ~/.bashrc",
    "auto_update": "echo 'alias update=\"sudo apt update && sudo apt upgrade\"' >> ~/.bashrc",
    "tldr": "echo 'alias tldr=\"tldr -u\"' >> ~/.bashrc",
    "timezone": "echo 'alias tz=\"timedatectl set-timezone\"' >> ~/.bashrc",
    "browser_cleaner": "echo 'alias clean_browser=\"rm -rf ~/.cache/google-chrome/*\"' >> ~/.bashrc",
    "python_venv": "echo 'alias venv=\"python3 -m venv\"' >> ~/.bashrc",
    "docker_compose": "echo 'alias dcup=\"docker-compose up\"' >> ~/.bashrc",
    "file_search": "echo 'alias findfile=\"find . -type f -name\"' >> ~/.bashrc",
    "dns_lookup": "echo 'alias dnslookup=\"dig\"' >> ~/.bashrc",
    "http_server": "echo 'alias server=\"python3 -m http.server\"' >> ~/.bashrc",
    "rsync_sync": "echo 'alias sync=\"rsync -avz\"' >> ~/.bashrc",
    "file_compress": "echo 'alias compress=\"tar -czf\"' >> ~/.bashrc",
    "file_decompress": "echo 'alias decompress=\"tar -xzf\"' >> ~/.bashrc",
    "git_alias": "echo 'alias gstatus=\"git status\"' >> ~/.bashrc && echo 'alias gpush=\"git push\"' >> ~/.bashrc",
    "ip_lookup": "echo 'alias iplookup=\"curl ipinfo.io\"' >> ~/.bashrc",
    "speedtest": "echo 'alias speed=\"speedtest-cli\"' >> ~/.bashrc",
    "cleanup": "echo 'alias clean=\"rm -rf ~/.cache/*\"' >> ~/.bashrc",
    "clipboard_manager": "echo 'alias clip=\"xclip -selection clipboard\"' >> ~/.bashrc"
}

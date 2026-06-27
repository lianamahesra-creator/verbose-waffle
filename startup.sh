#!/bin/bash

export DISPLAY=:1

Xvfb :1 -screen 0 1920x1080x24 &

vncserver :1 -geometry 1920x1080 -depth 24

websockify --web=/usr/share/novnc 6080 localhost:5901 &

startxfce4 &

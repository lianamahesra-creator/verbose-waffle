FROM FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    xfce4 \
    xfce4-terminal \
    firefox \
    tigervnc-standalone-server \
    novnc \
    websockify \
    xvfb \
    supervisor \
    wget \
    curl \
    git \
    unzip \
    python3 \
    python3-pip \
    && apt-get clean

RUN mkdir -p /root/.vnc
RUN echo "password" | vncpasswd -f > /root/.vnc/passwd
RUN chmod 600 /root/.vnc/passwd

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]

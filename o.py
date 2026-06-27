import time
import subprocess
import modal

app = modal.App("ubuntu-desktop")

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.4.1-runtime-ubuntu22.04",
        add_python="3.11",
    )
    .env(
        {
            "DEBIAN_FRONTEND": "noninteractive",
            "TZ": "Etc/UTC",
        }
    )
    .apt_install(
        "tzdata",
        "xfce4",
        "xfce4-terminal",
        "tigervnc-standalone-server",
        "novnc",
        "websockify",
        "xvfb",
        "supervisor",
        "firefox",
        "wget",
        "curl",
        "git",
        "unzip",
    )
    .add_local_file(
        "startup.sh",
        remote_path="/startup.sh",
        copy=True,
    )
    .run_commands(
        "chmod +x /startup.sh"
    )
)

@app.function(
    image=image,
    gpu="T4",
    timeout=60 * 60 * 24,
)
@modal.web_server(port=6080)
def desktop():
    subprocess.Popen(
        ["bash", "/startup.sh"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )

    while True:
        time.sleep(60)

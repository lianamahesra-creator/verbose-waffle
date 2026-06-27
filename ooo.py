import modal
import subprocess

app = modal.App("ubuntu-desktop")

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.4.1-runtime-ubuntu22.04",
        add_python="3.11",
    )
    .env({
        "DEBIAN_FRONTEND": "noninteractive",
        "TZ": "Etc/UTC",
    })
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
    )
    .add_local_file("startup.sh", "/startup.sh")
    .run_commands("chmod +x /startup.sh")
)

@app.function(image=image, gpu="T4", timeout=86400)
@modal.web_server(port=6080)
def desktop():
    subprocess.Popen(["bash", "/startup.sh"])

    import time
    while True:
        time.sleep(60)

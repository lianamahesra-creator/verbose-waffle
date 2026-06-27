import modal
import subprocess

app = modal.App("ubuntu-desktop")

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.4.1-runtime-ubuntu22.04",
        add_python="3.11",
    )
    .apt_install(
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
)

@app.function(image=image, gpu="T4", timeout=86400)
def desktop():
    subprocess.run(["/startup.sh"], check=True)

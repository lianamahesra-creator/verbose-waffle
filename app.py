import subprocess
import modal

app = modal.App("ubuntu-desktop")

image = modal.Image.from_dockerfile("Dockerfile")

@app.function(
    image=image,
    gpu="T4",
    timeout=86400,
)
def desktop():
    subprocess.run(["/startup.sh"], check=True)

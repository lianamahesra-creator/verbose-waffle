import modal

image = (
    modal.Image.from_dockerfile(".")
)

app = modal.App("ubuntu-desktop")

@app.function(
    image=image,
    gpu="T4",
    timeout=86400,
)
@modal.web_server(port=6080)
def desktop():
    pass

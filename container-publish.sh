
podman build . -t ngmaibulat/demo-python

podman login docker.io

podman push ngmaibulat/demo-python

podman run -it ngmaibulat/demo-python

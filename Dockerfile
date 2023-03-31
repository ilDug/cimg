# FROM python:3.11
# WORKDIR /app
# COPY ./requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# COPY ./compress-image.py ./compress-image.py
# ENTRYPOINT [ "python", "-u",  "./compress-image.py" ]
# CMD []
# la -u è per mostrare i print nel log (UNBUFFERED=1)


# docker build -t compress-image .
# docker run --rm -v $(PE) compress-image  -s <size=768> -q <quality=70> < inputimage.png > output.png

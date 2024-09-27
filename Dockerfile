FROM rendyprojects/python:latest

RUN apt -qq update && \
    apt -qq install -y --no-install-recommends \
    ffmpeg \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-dev \
    python3-pip \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \
    libavutil-dev \
    libswscale-dev \
    libswresample-dev \
    neofetch && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/

WORKDIR /usr/src/app

COPY . .
RUN pip3 install --upgrade pip setuptools==59.6.0
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN chown -R 1000:0 .
RUN chmod 777 .
RUN chown -R 1000:0 /usr
RUN chmod 777 /usr

EXPOSE 7860

CMD ["bash", "-c", "python3 server.py & python3 bot.py"]
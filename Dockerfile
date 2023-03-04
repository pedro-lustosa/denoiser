FROM python:3.7
RUN pip install --upgrade pip
RUN pip install hydra_core==0.11.3
RUN pip install hydra_colorlog==0.1.4
RUN pip install numpy
RUN pip install pystoi==0.3.3
RUN pip install git+https://github.com/ludlows/python-pesq#egg=pesq
RUN pip install six
RUN pip install sounddevice==0.4.0
RUN pip install torch
RUN pip install torchaudio
RUN pip install numba
RUN pip install julius
COPY . /app
WORKDIR /app
CMD sh make_debug.sh
CMD python train.py

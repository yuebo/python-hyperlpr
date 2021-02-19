FROM python
ADD sources.list /etc/apt/sources.list
RUN apt update
RUN apt install -y libgl1-mesa-glx
ADD requirements.txt requirements.txt
RUN python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
ADD main.py main.py
EXPOSE 8080
ENTRYPOINT python3 main.py

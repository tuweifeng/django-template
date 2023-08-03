FROM python:latest

# Django 基础框架以及组件
RUN yes | pip3 install Django==4.0.6 django-cors-headers==4.1.0 djangorestframework==3.14.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

# Python 开源第三方库
RUN yes | pip3 install pymysql==1.1.0 gunicorn==21.2.0 gevent==23.7.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

# Python 开源第三方库（不常用）
RUN yes | pip3 install yt-dlp==2023.7.6 -i https://pypi.tuna.tsinghua.edu.cn/simple

# Python 闭源私人库
COPY packages /root/packages
RUN yes | pip3 install /root/packages/sometools-0.1.0-py3-none-any.whl /root/packages/someapi-0.1.0-py3-none-any.whl


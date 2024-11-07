# 使用官方 Python 镜像作为基础镜像
FROM python:3.12-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到容器中
COPY requirements.txt .

# 设置 MYSQLCLIENT_CFLAGS 和 MYSQLCLIENT_LDFLAGS 环境变量
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/mysql -lmysqlclient"

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-deps

# 复制项目文件到容器中，包括 H5 文件夹 `web`
COPY . .

# 设置环境变量，避免 Python 在容器中生成 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HTTP_PROXY="http://host.docker.internal:10809"
ENV HTTPS_PROXY="http://host.docker.internal:10809"

# 配置静态文件收集
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# 开放8000端口用于 HTTP 和 WebSocket 服务
EXPOSE 8000

# 运行 Django HTTP 服务和 WebSocket 服务
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "casher.asgi:application"]

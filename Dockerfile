# 使用 Python 3.12.3 作为基础镜像
FROM python:3.12.3 AS builder

# 设置工作目录
WORKDIR /usr/src/app

# 将当前目录的内容复制到容器中
COPY . .

# 安装依赖并清理缓存
RUN pip install --no-cache-dir -r requirements.txt

# 使用 Python 3.12.3 作为基础镜像
FROM python:3.12.3-slim

# 安装 libpq 并清理缓存
RUN apt-get update && apt-get install -y libpq5 && rm -rf /var/lib/apt/lists/*

# 复制从 builder 阶段构建的 Python 依赖
COPY --from=builder /usr/local /usr/local

# 设置工作目录
WORKDIR /usr/src/app

# 将当前目录的内容复制到容器中
COPY . .

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 运行命令
CMD ["gunicorn", "admin_panel.wsgi:application", "--bind", "0.0.0.0:8000"]
## Paddle模型部署手册

### 一、环境准备

#### 1. Python 3.x（略）

#### 2. Paddle 1.5.x

安装指令：

```shell
pip3 install  --user paddlepaddle==1.5.0 --index-url https://pypi.tuna.tsinghua.edu.cn/simple/  --trusted-host https://pypi.tuna.tsinghua.edu.cn --timeout 600
```

#### 3. Django 2.2.x

安装指令：

```shell
pip3 install  --user Django==2.2.12 --index-url https://pypi.tuna.tsinghua.edu.cn/simple/  --trusted-host https://pypi.tuna.tsinghua.edu.cn --timeout 600
```

### 二、部署服务

#### 1. 文件目录说明

tile_server.zip解压后，目录及说明如下：

```python
# tile_server: 项目主目录
# infer: infer APP(预测)文件目录(按照Django规范创建)
# model_freeze: 预测模型存放目录
# request_infer_imgs: 待预测图像存放目录
# templates: 静态文件目录
# test_sample: 临时测试目录
# tile_server: django主APP目录(按照Django规范创建)
```

#### 2. 启动服务

进入tile_server主目录，执行如下命令启动：

```shell
python3 manage.py runserver 0.0.0.0:8000
```

如果打印出以下信息则表明启动成功：

```
Django version 2.2.12, using settings 'tile_server.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

#### 3. 进行预测

- 在浏览器中打开以下地址：

```
http://127.0.0.1:8000/static/infer_index.html
```

- 选择图像，并上传
- 跳转页面如果显示预测结果，则表明预测成功


# ali_oss
类似阿里云oss，实现图片旋转，加水印
## 开发环境
* python3.6
* windows10
* Pycharm
* tornado做服务
## From PyPi directly
pip install tornado

## Example
#### 请求访问：
* 旋转：http://127.0.0.1:6080/get_img/5.jpg?img_type=rotate&angle=102
* 打水印：http://127.0.0.1:6080/get_img/5.jpg?img_type=watermark&text=oss

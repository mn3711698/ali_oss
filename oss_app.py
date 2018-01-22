#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'

from tornado import web,ioloop,httpserver

from tornado.options import define, options
from functions import img_rotate,add_text_to_image

#define("port", default=8000, help="run on the given port", type=int)

#部门 逻辑处理模块
class IndexHandler(web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Welcome To GuangZhou11115555')
        # self.write(greeting + ', tornado!')
        self.render('index.html')#返回页面

# 上传图片的模块
class UploadHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        try:
            files = self.request.files.get('file')
            file = files[0]
            # print(file)
            # 保存文件
            with open(file['filename'],'wb') as f:
                f.write(file['body'])
            self.render('success.html')
        except Exception as e:
            print(e)
            self.write('上传失败')

# 展示图片
class GetImgHandler(web.RequestHandler):
    def get(self, filename, **kwargs):
        # 需要判断是什么服务
        # 旋转，加水印，get参数img_type
        img_type = self.get_argument('img_type',None)
        if img_type:
            if img_type=='rotate':
                # 旋转
                angle = self.get_argument('angle')
                img = img_rotate(filename,int(angle))

            elif img_type == 'watermark':
                # 加水印
                text = self.get_argument('text')
                img = add_text_to_image(filename,text)
        else:
            img = img_rotate(filename,0)
        self.write(img.getvalue())
        self.set_header('Content-Type','image/jpeg')
        print(filename)

# 分机号 路出
application = web.Application([
        (r'/index',IndexHandler),
        (r'/upload',UploadHandler),
        (r'/get_img/(?P<filename>.*)',GetImgHandler),
    ])


# 前台 socket服务
if __name__ == "__main__":
    # application.run(host='0.0.0.0', port=50000, debug=True)
    options.parse_command_line()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(6080)
    ioloop.IOLoop.instance().start()

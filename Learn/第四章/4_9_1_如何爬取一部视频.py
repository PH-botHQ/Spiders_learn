# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/23 17:42
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

# <video src='视频.mp4'></video>
# 一般的视频网站是怎么做的？：
# 用户上传视频 -> 转码(把视频处理出不同分辨率的, 2k, 1080, 标清) -> 切片处理(把单个视频文件拆分)
# 用户在进行拉动进度条时：
# ==============================

# 需要一个文件记录 1.视频播放顺序 2.视频存放路径
# M3U8（M3U文件，编码格式utf-8） txt json => 文本

# 想要抓取一个视频：
# 1.找到m3u8文件（各种手段）
# 2.通过m3u8下载到ts文件
# 3.通过各种手段(不仅是编程手段) 把ts文件合并为一个mp4文件


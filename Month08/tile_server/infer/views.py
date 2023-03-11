from django.shortcuts import render
from django.http import HttpResponse  # wdb
import csv
from .core_infer import *
import base64
import json
import os
import cv2

core_load_freeze_models()  # 加载模型
name_dict = {"MT_Blowhole": 0,
             "MT_Break": 1,
             "MT_Crack": 2,
             "MT_Fray": 3,
             "MT_Free": 4,
             "MT_Uneven": 5}


# 保存待预测图像，并返回归一化的图像数据
def write_to_tmp_file(img_data, request_sn):
    img_path = os.path.join("request_infer_imgs/" + request_sn)
    with open(img_path, "wb") as f:
        f.write(img_data)

    ret_img_data = core_load_image(img_path)  # 读取、裁剪、归一化
    return ret_img_data


def do_infer(request):
    print("do_infer()")

    # 获取预测参数
    if request.method == "POST":
        print("Method:Post")
        req_data = request.body.decode("utf-8")
        print("type of request:", type(req_data))
        print("\n\n", req_data, "\n\n")

        # 解码
        received_json_data = json.loads(req_data)
        img_data_base64 = received_json_data["img_data"]  # 获取图像数据

        tmp_base64_header = "data:image/jpeg;base64,"
        if img_data_base64.startswith(tmp_base64_header):
            img_data_base64 = img_data_base64[len(tmp_base64_header):]  # 截掉头部
            print("截取base编码头部:", tmp_base64_header)

        request_sn = received_json_data["req_sn"]  # 请求流水号
        img_data = base64.b64decode(img_data_base64)  # Base64解码
        img_data = write_to_tmp_file(img_data, request_sn)  # 将图像数据写入临时文件
    else:
        print("Method:Get")
        return HttpResponse("The method not was supported.")

    ret = ""  # 返回字符串

    result = core_do_infer(img_data)  # 预测
    print(result)
    max_index = np.argmax(result) # 获取概率最高的预测结果
    # 转换为名称
    for k, v in name_dict.items():
        if max_index == v:
            ret = k
            break

    return HttpResponse(json.dumps(ret), status=200)

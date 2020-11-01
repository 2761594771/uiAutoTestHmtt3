
import  yaml
import  os
from config import BASE_PATH
# def read_yaml():
#     # 定义空列表 组装测试数据
#     arr = []
#     with open("../data/mp_login.yaml","r",encoding="utf-8") as f:
#         # 遍历
#         for datas in yaml.safe_load(f).values():
#             # tuple(datas.values())转换为列表嵌套元组
#             arr.append(tuple(datas.values()))
#     # 返回 结果
#     return  arr


# 修改  动态解决路径问题  路径参数化 新建config.py 文件
def read_yaml(filename):
    # 定义空列表 组装测试数据
    arr = []
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file_path, "r", encoding="utf-8") as f:
        # 遍历
        for datas in yaml.safe_load(f).values():
            # tuple(datas.values())转换为列表嵌套元组
            arr.append(tuple(datas.values()))
    # 返回 结果
    return arr
#
# if __name__ == '__main__':
#     print(read_yaml("mp_login.yaml"))

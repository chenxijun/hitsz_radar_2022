"""
配置类
config.py
从外部文件读取配置
created by 李龙 2021/12
最终修改 by 李龙 2021/1/15
"""
import os
import numpy as np

enemy_color = 0
USEABLE = {
    "cam_left": True,
    "cam_right": True,
    "cam_far": False,
    "serial": False,
    "Lidar": True,
    "using_d": False,
}
DEBUG = True
BO = 0
cam_config = {
    "cam_left": {
        "id": "J37877236",
        "size": (3072, 2048),
        "video_path": "/home/hoshino/CLionProjects/LCR_sjtu/demo_resource/two_cam/1.mp4",
        "K_0": np.mat([[2505.2629026927225, 0.0, 1529.4286325395244],
                       [0.0, 2505.5722700649067, 1026.1378217662113],
                       [0.0, 0.0, 1.0]]),
        "C_0": np.mat([-0.06856710471358254, 0.1269396451339073,
                       -0.0003599605406165552, -0.0004173270419984247,
                       -0.141056084229664]),
        "exposure": 8000,
        "gain": 22,
        "rvec": np.mat([[1.69750257], [0.69091169], [-0.54474128]]),
        "tvec": np.mat([[-11381.85466339], [-584.01247871], [9359.30328641]]),
        "E_0": np.mat([
            [0.00462803, -0.999749, 0.0219115, 0.154876],
            [0.0931124, -0.0213857, -0.995426, -0.0506296],
            [0.995645, 0.0066471, 0.0929901, -0.137197],
            [0, 0, 0, 1]
        ])},

    "cam_right": {
        "id": "00J59583857",
        "size": (3072, 2048),
        "video_path": "/home/hoshino/CLionProjects/LCR_sjtu/demo_resource/two_cam/2.mp4",
        "K_0": np.mat([[2551.020329744114, 0.0, 1495.9469657967131],
                       [0.0, 2552.472255441562, 1062.7407379282765],
                       [0.0, 0.0, 1.0]]),
        "C_0": np.mat([-0.2555614504491957, 0.43900628627040805,
                       0.0013833604737366841, -0.00014651975584703355,
                       -0.527086991520376]),
        "exposure": 6000,
        "gain": 17,
        "rvec": np.mat([[1.69750257], [0.69091169], [-0.54474128]]),
        "tvec": np.mat([[-11381.85466339], [-479.01247871], [9449.30328641]]),
        "E_0": np.mat([
            [0.0242436, -0.999658, -0.00981226, -0.0455338],
            [0.0396638, 0.0107692, -0.999155, -0.0193313],
            [0.998919, 0.0238339, 0.0399114, -0.0972796],
            [0, 0, 0, 1]
        ])},

    "cam_far": {
        "id": "RS0037001020",
        "size": (640, 480),
        "video_path": "/home/hoshino/CLionProjects/LCR_sjtu/demo_resource/two_cam/2.mp4",
        "K_0": np.mat([[1273.6729986357857, 0.0, 598.3779780737999],
                       [0.0, 1274.0066230685838, 531.2012102435624],
                       [0.0, 0.0, 1.0]]),
        "C_0": np.mat([[-0.22753846151806761], [0.2209031621277345], [-0.0006069352871209068], [-0.0006361387371312384],
                       [0.02412961227405689]]),
        "exposure": 5000,
        "gain": 25,
        "rvec": np.mat([[1.59668528], [0.58626031], [-0.53932911]]),
        "tvec": np.mat([[-8625.00028137], [771.3457855], [6926.60950051]]),
        "E_0": np.mat([
            [0.0474247, -0.998873, -0.0019402, -0.00701503],
            [0.12093, 0.00766964, -0.992631, -0.0844397],
            [0.991528, 0.0468406, 0.121157, 0.0749353],
            [0, 0, 0, 1]
        ])}

}

net1_onnx = os.path.dirname(os.path.abspath(__file__)) + "/net_onnx/best.onnx"
net1_engine = os.path.dirname(os.path.abspath(__file__)) + "/net_onnx/net1.engine"

net2_onnx = os.path.dirname(os.path.abspath(__file__)) + "/net_onnx/net2.onnx"
net2_engine = os.path.dirname(os.path.abspath(__file__)) + "/net_onnx/net2.engine"

net1_cls = ['car', 'watcher', 'base']
net2_cls_names = ["0", "1", "2", "3", "4",
                  "5", "O", "Bs", "Bb"]
net2_col_names = ["B", "R", "N", "P"]

color2enemy = {"red": 0, "blue": 1}
enemy2color = ['red', 'blue']
num2cam = ['左', '右']
enemy_case = ["前哨站", "环形高地"]  # 这些区域在预警时只考虑敌方的该区域
our_case = ["missle_launch1", "missle_lauch2", "danger"]


armor_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'B1', 'B2', 'B3', 'B4', 'B5']  # 雷达站实际考虑的各个装甲板类
unit_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'RG', 'RO', 'RB', 'B1', 'B2', 'B3', 'B4', 'B5', 'BG', 'BO',
             'BB']  # 赛场上各个目标，主要用于HP显示

# 小地图图片路径
MAP_PATH = os.path.dirname(os.path.abspath(__file__)) + "/map.jpg"
BAG_FIRE = ""

# 小地图设定大小
map_size = (716, 384)
real_size = (28., 15.)
# UI中主视频源初始图像路径

INIT_FRAME_PATH = os.path.dirname(os.path.abspath(__file__)) + "/beijing.png"

region = \
    {
        'a_fp_red_环形高地_a': [8.90, 6.69, 8.90, 9.36, 10.37, 9.00, 10.37, 7.00, 0.60],
        'a_r_red_打符_a': [8.22, 2.50, 7.02, 1.30, 0.85, 0.85],
        'a_r_red_公路_a': [13.78, 14.94, 8.28, 13.92, 0.20, 0.20],
        'a_r_red_飞坡_d': [11.49, 0.94, 10.37, 0.20, 0.54, 0.20],

        'a_fp_blue_环形高地_a': [8.90, 6.69, 8.90, 9.36, 10.37, 9.00, 10.37, 7.00, 0.60],
        'a_r_blue_打符_a': [18.90, 13.70, 17.70, 12.50, 0.85, 0.85],
        'a_r_blue_公路_a': [17.70, 1.08, 12.20, 0.12, 0.20, 0.20],
        'a_r_blue_飞坡_d': [15.60, 14.80, 14.48, 14.06, 0.20, 0.54]
}

test_region = \
    {
        'a_fp_red_环形高地_a': [8.90, 6.69, 8.90, 9.36, 10.37, 9.00, 10.37, 7.00, 0.60],
        'a_fp_blue_环形高地_a': [8.90, 6.69, 8.90, 9.36, 10.37, 9.00, 10.37, 7.00, 0.60],
    }

PC_STORE_DIR = ""
LIDAR_TOPIC_NAME = "/livox/lidar"

# 0为正式场上使用的points 1为debug用
objNames = [
    {
        "cam_left": ['飞坡点(右)', '风车狙击点角(右)', '敌方烧饼轨道(左)', '环形高低银矿处角（敌方）',
                     '我方矿架基座左上角位', 'R0左上角'],
        "cam_right": ['4高地到盲道的通道右角', '敌方烧饼轨道(左)', 'R3B3右上直角',
                      '我方矿架基座左上角位', '我方飞坡点(右)']
    },
    {
        "cam_left": ['风车狙击点角', '烧饼轨道左', '烧饼轨道右', '环形高低银矿处角',
                     '环形高低坡下角(右)', '环形高地坡右下角(左)', "   "],
        "cam_right": ['风车狙击点角', '烧饼轨道左', '烧饼轨道右', '环形高低银矿处角',
                      '环形高低坡下角(右)', '环形高地坡右下角(左)', "   "]
    }
]

# 0为正式场上使用的points 1为debug用
objPoints = [
    {
        "cam_left": np.array([[9.56, 2.72, .90],  # 风车狙击点角
                              [5.59, 5.13, 1.376],  # 烧饼轨道左
                              [5.59, 8.74, 1.376],  # 烧饼轨道右
                              [9.09, 6.25, .600],  # 环形高低银矿处角
                              [11.18, 5.52, 0.],  # 环形高低坡下角(右)
                              [10.15, 4.90, 0.],
                              [9.09, 9.36, .600]], dtype=np.float32),  # 环形高地坡右下角(左)
        "cam_right": np.array([[9.56, 2.72, .90],  # 风车狙击点角
                               [5.59, 5.13, 1.376],  # 烧饼轨道左
                               [5.59, 8.74, 1.376],  # 烧饼轨道右
                               [9.09, 6.25, .600],  # 环形高低银矿处角
                               [11.18, 5.52, 0.],  # 环形高低坡下角(右)
                               [10.15, 4.90, 0.]], dtype=np.float32),  # 环形高地坡右下角(左)
    },
    {
        "cam_left": np.array([[9.56, 2.91, .90],  # 风车狙击点角
                              [5.59, 5.50, 1.376],  # 烧饼轨道左
                              [5.59, 9.36, 1.376],  # 烧饼轨道右
                              [9.09, 6.69, .600],  # 环形高低银矿处角
                              [11.18, 5.91, 0.],  # 环形高低坡下角(右)
                              [10.15, 5.26, 0.],  # 环形高地坡右下角(左)
                              [9.09, 9.36, .600]], dtype=np.float32),
        "cam_right": np.array([[9.56, 2.91, .90],  # 风车狙击点角
                              [5.59, 5.50, 1.376],  # 烧饼轨道左
                              [5.59, 9.36, 1.376],  # 烧饼轨道右
                              [9.09, 6.69, .600],  # 环形高低银矿处角
                              [11.18, 5.91, 0.],  # 环形高低坡下角(右)
                              [10.15, 5.26, 0.],  # 环形高地坡右下角(左)
                              [9.09, 9.36, .600]], dtype=np.float32),
    }
]

# 0为正式场上使用的points 1为debug用
Delaunary_points = [
    [
        {
            "cam_left": [
                (),
                [
                    # (world_points)
                ]

            ],
            "cam_right": [
                (),
                [
                    # (world_points)
                ]
            ]
        }
    ],
    [
        {
            "cam_left": [
                (),
                [
                    # (world_points)
                ]

            ],
            "cam_right": [
                (),
                [
                    # (world_points)
                ]
            ]
        }
    ]
]

"""
多线程管理类
mul_manager.py
用于多进程间的信息发布与接收
created by 李龙 in 2022/1
最终修改 by 李龙 in 2022/1/15
"""
from multiprocessing import Queue, Process, Event
import cv2 as cv
import time
import sys
from pyrdr.client import ImageAndArmorClient
from radar_detect.common import res_decode


def thread_detect(event, que, name):
    """
    debug 使用
    """
    from net.network_pro import Predictor
    import cv2
    import time
    # 多线程接收写法
    predictor1 = Predictor(name)
    count = 0
    t1 = time.time()
    t3 = time.time()
    print("副线程开始")
    print(id(event))
    while True:
        if t1 - t3 > 20:
            break
        frame = sub(event, que)
        if frame is not None:
            im1 = frame.copy()
            predictor1.detect_cars(frame)
            count += 1
            t2 = time.time()
            if t2 - t1 > 1:
                fps = float(count) / (t2 - t1)
                print(f'fps: {fps}')
                t1 = time.time()
                count = 0
    predictor1.stop()


def pub(event, que, data):
    """
    pub 函数
    :param event 多进程事件
    :param que 传输队列
    :param data 待传输数据
    """
    if event.is_set():
        return
    if que.full():
        try:
            que.get()
        except:
            pass
    que.put(data)
    event.set()


def sub(event, que):
    """
    sub 函数
    :param event 多进程事件
    :param que 传输队列
    """
    _wait = event.wait(timeout=0.1)
    if _wait:
        try:
            re_data = que.get_nowait()
        except:
            print("[ERROR] sub process can't get data!")
            re_data = False, None
        event.clear()
        return re_data
    else:
        return False, None


def process_detect(main_event, que, name, event_list):
    # 多线程接收写法
    from camera.cam_hk_v3 import Camera_HK
    from net.network_pro import Predictor
    from config import using_video
    print(f"子线程开始: {name}")
    predictor = Predictor(name)
    cam = Camera_HK(name, using_video, event_list)
    count = 0
    count_error = 0
    t1 = 0
    try:
        while not event_list['close'].is_set():
            if event_list['record'].is_set():
                predictor.record_on_clicked()
                event_list['record'].clear()
            result, frame = cam.get_img()
            if result and frame is not None:
                t3 = time.time()
                res = predictor.detect_cars(frame)
                pub(main_event, que, res)
                # time.sleep(0.04)
                t1 = t1 + time.time() - t3
                count += 1
                if count == 100:
                    fps = float(count) / t1
                    print(f'{name} count:{count} fps: {int(fps)} with queue size: {que.qsize()}')
                    count = 0
                    t1 = 0
            else:
                count_error += 1
                pub(main_event, que, [result, frame])
                if count_error == 10:
                    cam.destroy()
                    del cam
                    cam = Camera_HK(name, using_video)
                    count_error = 0
        predictor.stop()
        cam.destroy()
        print(f"相机网络子进程:{name} 退出")
    except Exception as e:
        print(f"相机网络子进程:{name} 寄了\n {e}")
        raise e
    # sys.exit()


def process_detect_rs(event, que, event_close, record, name):
    # 多线程接收写法
    print(f"子进程开始: {name}")
    receiver = ImageAndArmorClient('tcp://127.0.0.1:5555')
    count = 0
    t1 = 0
    try:
        while not event_close.is_set():
            t3 = time.time()
            frame, result = receiver.recv()
            frame = cv.resize(frame, (3072, 2048))
            frame[1848:, :, :] = 0
            if frame is not None:
                pub(event, que, [res_decode(result), frame])
                t1 = t1 + time.time() - t3
                count += 1
                if count == 100:
                    fps = float(count) / t1
                    print(f'{name} count:{count} fps: {int(fps)}')
                    count = 0
                    t1 = 0
    except Exception as e:
        print(f"相机网络子进程:{name} 寄了\n {e}")
    sys.exit()

# 멀티프로세싱

import multiprocessing as mp
import time

# if __name__ == "__main__":
#     proc = mp.current_process() #currnet_process() 실행되는 프로세스에 대한 정보를 담고있는 객체를 얻음
#     print(proc.name) #객체의 name 속성을 출력
#     print(proc.pid) #객체의 pid 속성 을 출력


def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")

if __name__ == '__main__':
    #main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    #process spawning
    p = mp.Process(name="SubProcess", target=worker)
    p.start()

    print("MainProcess End")
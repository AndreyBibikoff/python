import time


class TrafficLight:
    __color = {1: 'red', 2: 'yellow', 3: 'green'}

    def running(self):
        while True:
            print("\033[31m {}".format(self.__color[1]))
            time.sleep(7)
            print("\033[33m {}".format(self.__color[2]))
            time.sleep(2)
            print("\033[32m {}".format(self.__color[3]))
            time.sleep(7)


t_l = TrafficLight()
t_l.running()

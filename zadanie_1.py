import time
class TrafficLight:
    __colour = ['red', 'yellow', 'green']
    def running(self):
        while True:
            print(self.__colour[0])
            time.sleep(7)
            print(self.__colour[1])
            time.sleep(2)
            print(self.__colour[2])
            time.sleep(5)

svet = TrafficLight()
svet.running()
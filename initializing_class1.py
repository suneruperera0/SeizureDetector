# initializing the class

class basal:
    
    def __init__(self, sensor_1 = [] , sensor_2 = [], sensor_3 = [], sensor_4 = []):
        self.sensor_1 = sensor_1
        self.sensor_2 = sensor_2
        self.sensor_3 = sensor_3
        self.sensor_4 = sensor_4
        self.history = sum(sensor_1, sensor_2, sensor_3, sensor_4) / 4
        #self.history should be within a while loop and time.sleep should be for sensors 
        # self.history = sum(sensor_1) / len(sensor_1) + sum(sensor_2) / len(sensor_2)
        #safety mechanism to make sure that values for standard are as accurate as possible since different sensors = different results
        #add more sensors into the calculations depending on how many we are allowed to use

    def get_1(self):
        return self.sensor_1
    def get_2(self):
        return self.sensor_2
    #add for the number of sensors you want to have 

    def move(self, sensor_1, sensor_2):
        sensor_1 = sensor_1.append()
        sensor_2 = sensor_2.append()
        self.__sensor_1 = self.history.append






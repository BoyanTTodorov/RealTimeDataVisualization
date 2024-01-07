import numpy as np

# DataGenerator will generate numbers that will be sent to the database

class DataGenerator:
    def __init__(self, num, len, min, max):
        self.num = num
        self.data_len = len
        self.min = min
        self.max = max
    
    def generate(self):
        '''
            Generates an array of random numbers based on the object instance
        '''
        data = [np.random.randint(self.min, self.max) for _ in range(self.data_len)]
        return data

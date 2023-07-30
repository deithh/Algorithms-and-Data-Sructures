import random
import numpy as np



class Data: #min max included || size of an array

    def noise(_min, _max, size):
        array = np.linspace(_min,_max,size)
        np.random.shuffle(array)
        return array
       
    @classmethod
    def A(cls, _min, _max, size):
        temp = cls.noise(_min, _max, size)
        a, b = temp[:size//2], temp[size//2:]
        a.sort()
        b.sort()
        array = np.concatenate((a,np.flip(b)))
        return array
        
    def up(_min, _max, size):
        array= np.linspace(_min,_max, size)
        return array

    def down(_min, _max, size):
        array =  np.flip(np.linspace(_min,_max, size))
        return array
        
    def const(_min, _max, size):
        array = np.asarray([random.uniform(_min, _max)]*size)
        return array
        

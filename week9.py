'''
一、生成器函数
'''
import numpy as np
def random_walk(mu,x_0,sigma,N):
    '''
    随机游走生成器函数
    '''
    x=x_0
    for i in range(N):
        yield x+np.random.normal(0,sigma)
        w=np.random.normal(0,sigma)
        x=mu+x+w
    return 'NaN'
'''
def main():
    r1=random_walk(1,0,1,10)
    r2=random_walk(1,0,0.5,10)
    r3=random_walk(1,0,4,10)
    z=zip(r1,r2,r3)
    for each in z:
        print(each)
'''
'''
二、迭代器
'''
from PIL import Image
import numpy as np
import os

class FaceDataset:
    def __init__(self,path):
        self.path=path
        self.n=len(os.listdir(path))
        self.i=0
        self.image_list=os.listdir(path)
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<self.n:
            img=Image.open(self.path+'/'+self.image_list[self.i])
            img=np.array(img)
            self.i+=1
            return img
        else:
            raise StopIteration()
def main():
    path='D:/Project/Python/week9Iterator/originalPics/2003/06/07/big'
    image_list=FaceDataset(path)
    for image in image_list:
        print(image)
if __name__=='__main__':main()
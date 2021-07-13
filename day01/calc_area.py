import math

if __name__ == '__main__':
    print("pi:", 3.14)
    print("pi:", math.pi)
    print("1.計算圓面積")
    r=35
    area=r**2* math.pi
    print("半徑:%d 圓面積: %.2f" % (r, area))
    print("pi:", 3.14)
    print("pi:", math.pi)
    print("計算球面積")
    r=35
    area=4/3*math.pi*r*r*r
    print("半徑:%d 球體積: %.2f" % (r, area))



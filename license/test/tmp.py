class Vector2D(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

if __name__ == "__main__":
    v = Vector2D(3, 4)
    print(v.x, v.y)
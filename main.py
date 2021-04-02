from random import random, randint


class rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 > x2:
            t = x1
            x1 = x2
            x2 = t
        if y1 > y2:
            t = y1
            y1 = y2
            y2 = t
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)

    def info(self):
        return self.p1, self.p2


def rect_generator(n):
    while n > 0:
        yield rectangle(randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10))
        n -= 1


def decorator_log(func):
    def wrapper(args):
        print('Ищу неперекрытые прямоугольники')
        return func(args)

    return wrapper


def compare_rects(rect1, rect2):
    c1 = rect1.p1[1] >= rect2.p2[1]
    c4 = rect1.p1[0] >= rect2.p2[0]
    c2 = rect1.p2[1] <= rect2.p1[1]
    c3 = rect1.p2[0] <= rect2.p1[0]
    return c1 or c2 or c3 or c4


@decorator_log
def find_uncrossed(rects):
    print("ищу...")
    unx = rects
    needs_removing = False
    for r in rects:
        for r1 in rects:
            if r1 != r:
                if not compare_rects(r, r1):
                    needs_removing = True
                    try:
                        unx.remove(r1)
                    except:
                        continue
        if needs_removing:
            unx.remove(r)
            needs_removing = False
    print()
    print('нашёл!')
    for r in unx:
        print(r.info())

    return unx


def read_rects(file):
    with open(file) as f:
        lines = f.readlines()
    rectangles = list()
    for l in lines:
        points = l.split(" ")
        r = rectangle(int(points[0]), int(points[1]), int(points[2]), int(points[3]))
        print(r.info())
        rectangles.append(r)
    return rectangles


if __name__ == '__main__':
    rects = read_rects('test1.txt')
    for r in rect_generator(10):
        rects.append(r)
        print(r.info())
    uncrossed = find_uncrossed(rects)

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
        print(self.p1, ' ', self.p2)


def compare_rects(rect1, rect2):
    c1 = rect1.p1[1] <= rect2.p2[1]
    c2 = rect1.p2[1] >= rect2.p1[1]
    c3 = rect1.p2[0] <= rect2.p1[0]
    c4 = rect1.p1[0] >= rect2.p2[0]
    return c1 or c2 or c3 or c4


def find_uncrossed(rects):
    uncrossed = rects
    for r in rects:
        for r1 in rects:
            if compare_rects(r, r1):
                try:
                    uncrossed.remove(r)
                    uncrossed.remove(r1)
                except:
                    continue

    return uncrossed


def read_rects(file):
    with open(file) as f:
        lines = f.readlines()
    rectangles = list()
    for l in lines:
        points = l.split(" ")
        r = rectangle(points[0], points[1], points[2], points[3])
        r.info()
        rectangles.append(r)
    return rectangles


if __name__ == '__main__':
    rects = read_rects('test1.txt')
    uncrossed = find_uncrossed(rects)
    print("---------")
    print(uncrossed[0].info())

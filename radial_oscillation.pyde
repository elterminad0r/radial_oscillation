PHI = 0.5 * (1 + sqrt(5))

POINT_SIZE = 20
TIME_DILATION = 0.02
COLOUR_DILATION = TWO_PI * TIME_DILATION * 2
MAX_LENGTH = 300

FRAMES_PER_GEN = int(TWO_PI / TIME_DILATION)

REPRO_THRESHOLD = 5

FRAME_DOUBLEUP = 4

MAKING_VIDEO = False

def draw():
    global num, stop_adding
    translate(width / 2, height / 2)

    if not stop_adding and (frameCount) % FRAMES_PER_GEN == 0:
        num *= 2
        if num > 100 and MAX_LENGTH * sin(3 * TWO_PI / num) < REPRO_THRESHOLD:
            stop_adding = True
            print("finished")
        print("reproducing - {} {} {}".format(MAX_LENGTH * sin(3 * TWO_PI / num), num, 3 * TWO_PI / num))

    for _ in xrange(FRAME_DOUBLEUP):
    
        for i in range(num):
            th = 3 * TWO_PI * i / num
            l = sin(frameCount * TIME_DILATION + th / 3.0) * MAX_LENGTH
            fill(255 * (sin(frameCount * COLOUR_DILATION + th * 2 + PHI) + 1) * 0.5, 255, 255)
            ellipse(l * cos(th), l * sin(th), POINT_SIZE, POINT_SIZE)

    if MAKING_VIDEO:
        saveFrame("data/rainbow-######.png")

def setup():
    global num, stop_adding
    size(1280, 720)
    num = 6
    stop_adding = False
    background(0)
    noStroke()
    colorMode(HSB, 255, 255, 255)

def keyPressed():
    global num
    if key == ' ':
        num *= 2
    elif key == 'r':
        setup()
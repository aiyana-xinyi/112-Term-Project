# Updated Animation Starter Code

from tkinter import *
import sys
from aubio import onset, source
from numpy import hstack, zeros

####################################
# customize these functions
####################################

def init(data):
    data.timerDelay = 1000
    data.timeCount = 0
    data.x = 0
    data.allOnsets = []
    onSet(data)

def onSet(data):
    win_s = 512                 # fft size
    hop_s = win_s // 2          # hop size

    if len("ahah.wav") < 2:
        print("Usage: %s <filename> [samplerate]" % sys.argv[0])
        sys.exit(1)

    filename = "ahah.wav"

    samplerate = 0
    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    o = onset("default", win_s, hop_s, samplerate)

    # list of onsets, in samples
    onsets = []

    # storage for plotted data
    desc = []
    tdesc = []
    allsamples_max = zeros(0,)
    downsample = 2  # to plot n samples / hop_s

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        if o(samples):
            #print("%f" % (o.get_last_s()))
            data.allOnsets.append(o.get_last_s())
            onsets.append(o.get_last())
        # keep some data to plot it later
        new_maxes = (abs(samples.reshape(hop_s//downsample, downsample))).max(axis=0)
        allsamples_max = hstack([allsamples_max, new_maxes])
        desc.append(o.get_descriptor())
        tdesc.append(o.get_thresholded_descriptor())
        total_frames += read
        if read < hop_s: break
    # if 1:
    #     # do plotting
    #     import matplotlib.pyplot as plt
    #     allsamples_max = (allsamples_max > 0) * allsamples_max
    #     allsamples_max_times = [ float(t) * hop_s / downsample / samplerate for t in range(len(allsamples_max)) ]
    #     plt1 = plt.axes([0.1, 0.75, 0.8, 0.19])
    #     plt2 = plt.axes([0.1, 0.1, 0.8, 0.65], sharex = plt1)
    #     plt.rc('lines',linewidth='.8')
    #     plt1.plot(allsamples_max_times,  allsamples_max, '-b')
    #     plt1.plot(allsamples_max_times, -allsamples_max, '-b')
    #     for stamp in onsets:
    #         stamp /= float(samplerate)
    #         plt1.plot([stamp, stamp], [-1., 1.], '-r')
    #     plt1.axis(xmin = 0., xmax = max(allsamples_max_times) )
    #     plt1.xaxis.set_visible(False)
    #     plt1.yaxis.set_visible(False)
    #     desc_times = [ float(t) * hop_s / samplerate for t in range(len(desc)) ]
    #     desc_max = max(desc) if max(desc) != 0 else 1.
    #     desc_plot = [d / desc_max for d in desc]
    #     plt2.plot(desc_times, desc_plot, '-g')
    #     tdesc_plot = [d / desc_max for d in tdesc]
    #     for stamp in onsets:
    #         stamp /= float(samplerate)
    #         plt2.plot([stamp, stamp], [min(tdesc_plot), max(desc_plot)], '-r')
    #     plt2.plot(desc_times, tdesc_plot, '-y')
    #     plt2.axis(ymin = min(tdesc_plot), ymax = max(desc_plot))
    #     plt.xlabel('time (s)')
    #     #plt.savefig('/tmp/t.png', dpi=200)
    #     plt.show()

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.timeCount += 1
    for time in data.allOnsets:
        if data.timeCount == int(time):
            print(time,"i am reached")

def redrawAll(canvas, data):
    # draw in canvas
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
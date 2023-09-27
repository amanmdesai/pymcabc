import json
import matplotlib.pyplot as plt
from feynman import Diagram


class FeynmanDiagram:
    """
    class for drawing feynman diagrams
    using feynman package
    """

    def __init__(self):
        with open("library.json", "r") as f:
            library = json.load(f)

        process = library["process"]
        mediator = library["mediator"][0]
        channel = library["channel"][0]

        decay_process = library["decay_process"]
        if decay_process !="NaN":
            decay_process = decay_process[0].replace(">","")
            self.decay_process = decay_process.split()
            self.decay()

        process = process[0].replace(">", mediator)
        self.process = process.split()

        if channel == "none":
            for p in library["process_type"][0]:
                if p == "s":
                    self.s_chan()
                elif p == "t":
                    self.t_chan()
                elif p == "u":
                    self.u_chan()
                else:
                    return 0
        elif channel =="s":
            self.s_chan()
        elif channel == "t":
            self.t_chan()
        elif channel == "u":
            self.u_chan()
        else:
            print("Possible channels: s, t, and u")
            return 0

    def s_chan(self):
        fig = plt.figure(figsize=(5.0, 5.0))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)
        in1 = diagram.vertex(xy=(0.1, 0.75), marker="")
        in2 = diagram.vertex(xy=(0.1, 0.25), marker="")
        v1 = diagram.vertex(xy=(0.35, 0.5))
        v2 = diagram.vertex(xy=(0.65, 0.5))
        out1 = diagram.vertex(xy=(0.9, 0.75), marker="")
        out2 = diagram.vertex(xy=(0.9, 0.25), marker="")

        a = diagram.line(in1, v1, arrow=False)
        b = diagram.line(in2, v1, arrow=False)
        c = diagram.line(v1, v2, arrow=False)
        d = diagram.line(v2, out1, arrow=False)
        e = diagram.line(v2, out2, arrow=False)

        a.text(self.process[0], fontsize=20, t=0.1, y=0.1)
        b.text(self.process[1], fontsize=20, t=0.1, y=-0.1)
        c.text(self.process[2], fontsize=20)  # ,y=.1)
        d.text(self.process[3], fontsize=20, t=-0.01, y=0.1)
        e.text(self.process[4], fontsize=20, t=-0.1, y=-0.1)

        diagram.plot()
        plt.savefig("schan.pdf")

    def t_chan(self):
        fig = plt.figure(figsize=(5.0, 5.0))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)
        in1 = diagram.vertex(xy=(0.1, 0.75), marker="")
        in2 = diagram.vertex(xy=(0.1, 0.25), marker="")
        v1 = diagram.vertex(xy=(0.5, 0.65))
        v2 = diagram.vertex(xy=(0.5, 0.35))
        out1 = diagram.vertex(xy=(0.9, 0.75), marker="")
        out2 = diagram.vertex(xy=(0.9, 0.25), marker="")

        a = diagram.line(in1, v1, arrow=False)
        b = diagram.line(in2, v2, arrow=False)
        c = diagram.line(v1, v2, arrow=False)
        d = diagram.line(v1, out1, arrow=False)
        e = diagram.line(v2, out2, arrow=False)

        a.text(self.process[0], fontsize=20, t=0.1, y=0.1)
        b.text(self.process[1], fontsize=20, t=0.1, y=-0.1)
        c.text(self.process[2], fontsize=20)  # ,y=.1)
        d.text(self.process[3], fontsize=20, t=-0.1, y=+0.1)
        e.text(self.process[4], fontsize=20, t=-0.1, y=-0.1)

        diagram.plot()
        plt.savefig("tchan.pdf")

    def u_chan(self):
        fig = plt.figure(figsize=(5.0, 5.0))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)
        in1 = diagram.vertex(xy=(0.1, 0.75), marker="")
        in2 = diagram.vertex(xy=(0.1, 0.25), marker="")
        v1 = diagram.vertex(xy=(0.5, 0.65))
        v2 = diagram.vertex(xy=(0.5, 0.35))
        out1 = diagram.vertex(xy=(0.9, 0.75), marker="")
        out2 = diagram.vertex(xy=(0.9, 0.25), marker="")

        a = diagram.line(in1, v1, arrow=False)
        b = diagram.line(in2, v2, arrow=False)
        c = diagram.line(v1, v2, arrow=False)
        d = diagram.line(v1, out2, arrow=False)
        e = diagram.line(v2, out1, arrow=False)

        a.text(self.process[0], fontsize=20, t=0.1, y=0.1)
        b.text(self.process[1], fontsize=20, t=0.1, y=-0.1)
        c.text(self.process[2], fontsize=20)  # ,y=.1)
        d.text(self.process[3], fontsize=20, t=-0.1, y=-0.1)
        e.text(self.process[4], fontsize=20, t=-0.1, y=0.1)

        diagram.plot()
        plt.savefig("uchan.pdf")

    def decay(self):
        fig = plt.figure(figsize=(5.,5.))
        ax = fig.add_axes([0,0,1,1], frameon=False)

        diagram = Diagram(ax)
        in1 = diagram.vertex(xy=(.1,.5), marker='')
        v1  = diagram.vertex(xy=(.5,.5))
        out1 = diagram.vertex(xy=(.9,.75),marker='')
        out2 = diagram.vertex(xy=(.9,.25),marker='')

        a = diagram.line(in1,v1,arrow=False)
        b = diagram.line(v1,out1,arrow=False)
        c = diagram.line(v1,out2,arrow=False)
        a.text(self.decay_process[0],fontsize=30,t=.1,y=.1)
        b.text(self.decay_process[1],fontsize=30,t=-.01,y=.1)
        c.text(self.decay_process[2],fontsize=30,t=-.1, y=-.1)

        diagram.plot()
        plt.savefig('decay.pdf')

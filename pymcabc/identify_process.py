import json
import math
import pymcabc.constants


def build_json():
    library = {
        "mA": [],
        "mB": [],
        "mC": [],
        "m1": [],
        "m2": [],
        "m3": [],
        "m4": [],
        "mx": [],
        "outgoing_p": [],
        "bw": [],
        "massive": [],
        "massive_mass": [],
        "decay_process": [],
        "decay1_mass": [],
        "decay2_mass": [],
        "mediator": [],
        "pi": [],
        "Ecm": [],
        "process": [],
        "process_type": [],
        "channel": [],
        "w_max": [],
        "w_sum": [],
        "w_square": [],
    }
    jsonString = json.dumps(library, indent=2)

    with open("library.json", "w") as f:
        json.dump(library, f)


class DefineProcess:
    """
    This is class to define the process, masses of particles and center of mass energy
    Parameters:
        input_string (str): Physics process. Example > 'A A > B B'
        mA (float): mass of particle A
        mB (float): mass of particle B
        mC (float): mass of particle C
        E1 (float): center of mass energy for beam 1
        E2 (float): center of mass energy for beam 2
        channel (str): optional, use to study effect a particular channel
    """

    def __init__(
        self,
        input_string: str,
        mA: float,
        mB: float,
        mC: float,
        pi: float,
        #E1: float,
        #E2: float,
        channel: str = "none",
    ):

        build_json()
        with open("library.json", "r") as f:
            self.library = json.load(f)
        self.input_string = input_string
        self.mA = mA
        self.mB = mB
        self.mC = mC
        self.p_i = pi
        #self.E1 = E1
        #self.E2 = E2
        if self.mA < 0 or self.mB < 0 or self.mC < 0:
            raise Exception("Negative masses not accepted")
        #if self.E1 < 0:
        #    raise Exception("Negative Energy not accepted")
        if self.p_i <= 0:
            raise Exception("Negative or Zero absolute momentum not accepted")
        self.library["mA"].append(mA)
        self.library["mB"].append(mB)
        self.library["mC"].append(mC)
        self.library["pi"].append(pi)
        #self.library["E2"].append(self.E2)
        self.library["channel"].append(channel)
        self.process()
        self.channel()
        self.masses()
        self.identify_mediator()
        self.identify_decay()
        self._ECM()
        self.final_momenta()
        self.bw()

    def process(self):
        """identify the physics process"""
        self.library["process"].append(self.input_string)
        string = self.input_string.replace(" > ", " ")
        string = string.split(" ")
        initial_1 = string[0]
        initial_2 = string[1]
        output_3 = string[2]
        output_4 = string[3]
        if output_3 == output_4:
            process_type = "tu"
        elif output_3 != output_4:
            process_type = "st"
        else:  # modify logic here; identify valid string at the start
            raise Exception("unable to identify process, please try again")
        self.library["process_type"].append(process_type)
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return None

    def channel(self):
        process_type = self.library["process_type"][0]
        channel = self.library["channel"][0]
        if channel != "none":
            if channel not in process_type:
                raise Exception(
                    "Channel "
                    + channel
                    + " not available for process type "
                    + process_type
                )
        return None

    def masses(self):
        """assign masses to m1, m2, m3, m4 and mediator"""
        string = self.input_string.replace(" > ", " ")
        string = string.split(" ")
        pmass = [0, 0, 0, 0]
        for i in range(4):
            if string[i] == "A":
                pmass[i] = self.mA
            elif string[i] == "B":
                pmass[i] = self.mB
            elif string[i] == "C":
                pmass[i] = self.mC
            else:
                raise Exception("Enter valid string")
        self.library["m1"].append(pmass[0])
        self.library["m2"].append(pmass[1])
        self.library["m3"].append(pmass[2])
        self.library["m4"].append(pmass[3])
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return None
    
    def _ECM(self):
        #center of mass energy
        with open("library.json", "r") as f:
            library = json.load(f)
        m1 = library["m1"][0]
        m2 = library["m2"][0]
        E1 = math.sqrt(m1**2 + self.p_i**2)
        E2 = math.sqrt(m2**2 + self.p_i**2)
        Ecm = E1 + E2
        self.library["Ecm"].append(Ecm)
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return E1, E2, Ecm
    
    def ECM(self):
        with open("library.json", "r") as f:
            library = json.load(f)
        m1 = library["m1"][0]
        m2 = library["m2"][0]
        E1 = math.sqrt(m1**2 + self.p_i**2)
        E2 = math.sqrt(m2**2 + self.p_i**2)
        Ecm = E1 + E2
        print(
              "\n",
            "Energy Beam 1 : ", E1,
              "\n",
            "Energy Beam 2 : ", E2,
              "\n",
            "Energy CM : ", Ecm,
              )
        return E1, E2, Ecm



    def identify_mediator(self):
        """identify the mediator of the process"""
        process = self.library["process"][0]
        process = process.replace(" > ", " ")
        if (
            process == "A A B B"
            or process == "A B A B"
            or process == "B A B A"
            or process == "B B A A"
        ):
            self.library["mx"].append(self.mC)
            self.library["mediator"].append("C")
        elif (
            process == "A A C C"
            or process == "A C A C"
            or process == "C A C A"
            or process == "C C A A"
        ):
            self.library["mx"].append(self.mB)
            self.library["mediator"].append("B")
        elif (
            process == "B B C C"
            or process == "B C B C"
            or process == "C B C B"
            or process == "C C B B"
        ):
            self.library["mx"].append(self.mA)
            self.library["mediator"].append("A")
        else:
            return None
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return None
    
    def final_momenta(self):
        p_f = pymcabc.constants.outgoing_p(self.library["Ecm"][0], self.library["m3"][0], self.library["m4"][0])
        self.library["outgoing_p"].append(p_f)
        with open("library.json", "w") as f:
            json.dump(self.library, f)

    def bw(self):
        if self.library["mx"][0] > 0:
            deno  = 8*math.pi*(self.library["mx"][0])**2
            _bw = (pymcabc.constants.g**2*self.library["outgoing_p"][0])/deno
        else:
            _bw = 0.0
        self.library["bw"].append(_bw)
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return _bw

    def identify_decay(self):
        """identify the decay chain associated with the process"""
        mA = self.library["mA"][0]
        mB = self.library["mB"][0]
        mC = self.library["mC"][0]
        if mA > mB + mC:
            self.library["massive"].append("A")
            self.library["massive_mass"].append(mA)
            self.library["decay1_mass"].append(mB)
            self.library["decay2_mass"].append(mC)
            self.library["decay_process"].append("A > B C")

        elif mB > mA + mC:
            self.library["massive"].append("B")
            self.library["massive_mass"].append(mB)
            self.library["decay1_mass"].append(mA)
            self.library["decay2_mass"].append(mC)
            self.library["decay_process"].append("B > A C")

        elif mC > mA + mB:
            self.library["massive"].append("C")
            self.library["massive_mass"].append(mC)
            self.library["decay1_mass"].append(mA)
            self.library["decay2_mass"].append(mB)
            self.library["decay_process"].append("C > A B")

        else:
            self.library["massive"].append("NaN")
            self.library["massive_mass"].append("NaN")
            self.library["decay1_mass"].append("NaN")
            self.library["decay2_mass"].append("NaN")
            self.library["decay_process"].append("NaN")
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return None

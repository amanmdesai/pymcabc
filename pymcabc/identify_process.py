import json


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
        "massive": [],
        "massive_mass": [],
        "decay_process": [],
        "decay1_mass": [],
        "decay2_mass": [],
        "mediator": [],
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
        Ecm (float): center of mass energy
        channel (str): optional, use to study effect a particular channel


    """

    def __init__(
        self,
        input_string: str,
        mA: float,
        mB: float,
        mC: float,
        Ecm: float,
        channel: str = "none",
    ):
        """
        Defines the process, masses of particles and center of mass energy
        Parameters:
            input_string (str): Physics process. Example > 'A A > B B'
            mA (float): mass of particle A
            mB (float): mass of particle B
            mC (float): mass of particle C
            Ecm (float): center of mass energy
            channel (str): optional, use to study effect a particular channel


        """

        build_json()
        with open("library.json", "r") as f:
            self.library = json.load(f)
        self.input_string = input_string
        self.mA = mA
        self.mB = mB
        self.mC = mC
        self.Ecm = Ecm
        self.library["mA"].append(mA)
        self.library["mB"].append(mB)
        self.library["mC"].append(mC)
        self.library["channel"].append(channel)
        self.process()
        self.masses()
        self.ECM()
        self.identify_mediator()
        self.identify_decay()

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

    def ECM(self):
        """center of mass energy"""
        self.library["Ecm"].append(self.Ecm)
        with open("library.json", "w") as f:
            json.dump(self.library, f)
        return None

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

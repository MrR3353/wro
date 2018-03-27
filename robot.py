import rpyc
import copy
import json

class Robot():
    # Link to another robot
    another_robot = None

    # Link to module move 
    move = None

    # Robot name
    name = None

    # Robot field
    field = {}
    # Robot coord
    coord = (0,0)
    # Robot direction
    alpha = 0

    # Is the robot localized?
    localized = False

    def __init__(self, ip = None, name = None):
        #robot = rpyc.classic.connect(ip)
        #self.move = robot.modules["move"]
        self.name = name 

    def dumpAll(self):
        '''
        dumpAll - dump all information about the robot on the server
        '''

        field = copy.deepcopy(self.field)
        field_dump = {}
        keys = sorted(field.keys())
        r = []
        if keys[0][0] < 0:
            r.append(keys[0][0])
        else:
            r.append(0)
        if keys[0][1] < 0:
            r.append(keys[0][1])
        else:
            r.append(0)
        if r != [0,0]:
            r = keys[0]
            field_ret = {}
            for coord, cell in field.items():
                field_ret[coord[0] - r[0], coord[1] - r[1]] = cell
            field = field_ret

        for coord, cell in field.items():
            cell_dump = ""
            for i in range(len(cell)):
                if cell[i] == 1:
                    if i == 0:
                        cell_dump += "r"
                    elif i == 1:
                        cell_dump += "b"
                    elif i == 2:
                        cell_dump += "l"
                    elif i == 3:
                        cell_dump += "t"
            field_dump[str(coord[0]) + str(coord[1]+ 1)] = cell_dump

        filename = r"graphic\app\data\field_" + str(self.name) + ".json"
        json.dump(field_dump, open(filename, "w"))

        fielname = r"graphic\app\data\\" + str(self.name) + ".json" 
        json.dump([str(self.coord[0] - r[0]) + str(self.coord[1] + 1 - r[1]), self.alpha], open(fielname, "w"))


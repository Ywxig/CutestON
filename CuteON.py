type_str_action = ("str", "url", "file")
type_int_action = ("int")
type_list_action = ("list", "rgb", "rgba", "diolog", "matrix")
type_float_action = ("float")

import math

class Color():

    def toIntVec(list_):
        try:
            list_ = list_.split(",")
        except:
            pass
        arr = []
        for i in list_:
            arr.append(int(i))
        return arr

    def subtraction(Color_vector1 : list, Color_vector2 : list) -> list:
        Color_vector = []
        for color in range(3):
            rezalt_color = Color_vector1[color] - Color_vector2[color]
            if rezalt_color < 0:
                Color_vector.append(0)
            if rezalt_color > 255:
                Color_vector.append(255)
            else:
                Color_vector.append(rezalt_color)
        return Color_vector   
    
    def addition(Color_vector1 : list, Color_vector2 : list) -> list:
        Color_vector = []
        for color in range(3):
            rezalt_color = Color_vector1[color] + Color_vector2[color]
            if rezalt_color < 0:
                Color_vector.append(0)
            if rezalt_color > 255:
                Color_vector.append(255)
            else:
                Color_vector.append(rezalt_color)
        return Color_vector

class Get_:

    def getAll(file):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")

        arr = []

        for i in content_l:
            text = i.split("::")
            if text[0] == "public":
                arr.append(text[2])
            if content_l == "":
                pass
            else:
                pass
        return arr

    def getLine(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[1] == str(nameString):
                return text[2]
            else:
                pass

    def getObj(file : str, nameObj : str) -> dict:
        """
        getObj read obj in file and serialize this
        pbject. And return dict values for this
        opject
        """
        file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("object::"+nameObj+"::{")
        fin = content_l[1].split("}")
        content = fin[0]
        values = {}
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::") 
            values[text[1]] = text[2]
        return values

class Read_:
    def Read(file):
        file = open(file, "r", encoding="utf-8").read()
        if file != "":
            return file
        else:
            return file
        
        

    def readLine(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[1] == str(nameString):
                if text[0] in type_list_action:
                    return text[2].split(",")
                if text[0] in type_str_action:
                    return str(text[2])
                if text[0] in type_int_action:
                    return int(text[2])
                if text[0] in type_float_action:
                    return float(text[2])

class Write_:
    def add(file, text):
        file = open(file, "a")
        if text.split()[0] == "public" or text.split()[0] == "private":
            file.write(text)

    def WriteLine(file : str, Line : str):
        nameLine = Line.split("::")[1]
        file_ = open(file, "r", encoding="utf-8").read()
        content = file_.split("\n")
        for i in content:
            if i.split("::")[1] == nameLine:
                cutLine = i
        fileParts = file_.split(cutLine)
        open(file, "w", encoding="utf-8").write(str(fileParts[0]) + str(Line) + str(fileParts[1]))

class CuteScript:

    def parser(file : str) -> list:
        vars_ = {}
        STEK_COMMAND = []

        FILE = Read_.Read(file) #Получаем данные из файла
        HEEP = FILE.split("\n") #Делаем кучу из фала по которой будем ходить

        for line in HEEP:
            if line == "":
                pass
            else:
                items = line.split()
                """Читаем кучу по линиям и делаем очередь из комманд"""

                if items[0] == "line":
                    try:
                        vars_[items[1]] = items[0] + "::" + items[1] + "::" + items[2]
                    except:
                        vars_[items[1]] = items[0] + "::" + items[1] + "::0"

                if items[0] == "int":
                    try:
                        vars_[items[1]] = items[2]
                    except:
                        vars_[items[1]] = "0"
                if items[0] == "str":
                    vars_[items[1]] = items[2]

                if items[0] == "rgb":
                    vars_[items[1]] = items[2].split(",")

                if items[0] == "@":
                    vars_[items[1]] = items[2]

                if items[0] == "/subtractionRGB":
                    Vec1 = Color.toIntVec(vars_[items[1]])
                    Vec2 = Color.toIntVec(vars_[items[2]])
                    vars_["VecRes"] = Color.subtraction(Vec1, Vec2)

                if items[0] == "/additionRGB":
                    Vec1 = Color.toIntVec(vars_[items[1]])
                    Vec2 = Color.toIntVec(vars_[items[2]])
                    vars_["VecRes"] = Color.addition(Vec1, Vec2)

                if items[0] == "/toCss":
                    res = Color.toIntVec(vars_[items[1]])
                    vars_["css"] = "rgb(" + str(res[0]), "," + str(res[1]) + "," + str(res[2]) + ")" 

                if items[0] == "/write":
                    if items[2] in vars_ and items[1] in vars_:
                        Write_.WriteLine(vars_[items[1]], str(vars_[items[2]]))
                    else:
                        Write_.WriteLine(items[1], items[2])

                if items[0] == "/getLine":
                    if items[2] in vars_ and items[1] in vars_:
                        vars_[items[2]] = Get_.getLine(vars_[items[1]], (str(vars_[items[2]])).split("::")[1])
                    else:
                         vars_[items[2]] = Get_.getLine(vars_[items[1]], items[2])                    

                if items[0] in vars_ and items[1] == "=" and items[2] in vars_:
                    vars_[items[0]] = vars_[items[2]]

                if items[0] == "/print":
                    print(vars_[items[1]])

                if items[0] == "/toLine":
                    if str(items[1]) == "rgb":
                        normalize = []
                        for i in range(3):
                            normalize.append(str(vars_[items[3]][i]))
                        rgb_l = ",".join(normalize)
                    vars_[items[2]] = str(items[1]) + "::" + str(items[2]) + "::" + rgb_l    
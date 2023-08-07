type_str_action = ("str", "url", "file")
type_int_action = ("int")
type_list_action = ("list", "rgb", "rgba", "diolog", "matrix")
type_float_action = ("float")
WebFile = ('html', 'css', 'js')

import time
import math

class Types:
    def toIntVec(list_):
        try:
            list_ = list_.split(",")
        except:
            pass
        arr = []
        for i in range(2):
            arr.append(int(i))
        return arr

class Color:
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

    def getType(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[1] == str(nameString):
                return text[0]
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
        File = open(file, "r", encoding="utf-8").read()
        if File != "":
            return File
        else:
            return "None"
        
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

    def write(file, text):
        file = open(file, "w", encoding="utf-8")
        file.write(text)
        file.close()

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

class Builder:

    class CSS:

        def New(tupe_ : str, name : str):
            if tupe_ == "id":
                return "#" + name + "{"
            if tupe_ == "class":
                return "." + name + "{"
            else:
                print("[Sorry what is `" + tupe_ + "`? I dont know what is type of style!]")      

    class HTML:

        def Tag(tag : str, ctx : str, class_:str):
            if class_ != "":
                return '<' + tag + ' class="' + class_ + '">' + ctx + '</' + tag + '>'
            else:
                return '<' + tag + '>' + ctx + '</' + tag + '>'


        def build(file : str, content : list):
            arr = []
            for i in content:
                if i == "#insert":
                    FILE = content[content.index(i)].split()[1]
                    arr.append(Read_.Read(FILE))
                if i == "#include":
                    FILE = content[content.index(i)].split()[1]
                    name_file = FILE.split(".")
                    if name_file[1] == "css":
                        arr.append("<style>\n" + open("template/" + Read_.Read(FILE), "r").read() + "\n" + "</style>\n")

                    if name_file[1] == "js":
                        arr.append("<script>\n" + open("template/" + Read_.Read(FILE), "r").read() + "\n" + "</script>\n")
                
                else:
                    arr.append(i)

            Write_.write(file, "\n".join(arr))

                    

class CuteScript:

    FLAG = "main"

    def command(line, vars_ = {}):
        for i in line.split():
            Word = i.split(".")

            if Word[0] == "HTML":
                if Word[1] == "tag":
                    return Builder.HTML.Tag(Word[2], str(line.split("HTML.tag." + Word[2])[1]), class_="")
                
                if Word[1] == "add":
                    return str(line.split("HTML.add")[1])
                if Word[1] == "element":
                    file_type = str(line.split("HTML.element ")[1]).split(".")[1]
                    if file_type in WebFile:
                        return Read_.Read(str(line.split("HTML.element ")[1]))
                    else:
                        print("[Element is not for web. I can't use this element]")
    
            if Word[0] == "CSS":

                if Word[1] == "start":
                    return "<style>"

                if Word[1] == "new":
                    return Builder.CSS.New("id", str(line.split("CSS.new ")[1]))

                if Word[1] == "element":
                    file_type = str(line.split("CSS.element ")[1]).split(".")[1]
                    if file_type == "css":
                        return Read_.Read(str(line.split("CSS.element ")[1]))
                    else:
                        print("[Element is not `css`. I can't use this element]")

                if Word[1] == "end":
                    try:
                        if str(line.split("CSS.end ")[1]) == "element":
                            return "}"
                        else:
                            return "</style>"
                    except:
                        return "</style>"
       
            if Word[0] == "doc":
                if Word[1] == "start":
                    return '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Document</title>\n</head>\n<body>\n\n'
                if "end":
                    return '</body>\n</html>'

            if Word[0] == "console":
                if Word[1] == "var":
                    print(vars_[line.split()[1]])
            
                if Word[1] == "time":
                    time_ = time.strftime("{ %H:%M }")
                    print(time_)

            if line.split()[0] in vars_:
                return str(vars_[line.split()[0]])


    def styler(line, vars_ = {}):
        for i in line.split():
            Word = i.split(".")

            if Word[0] == "CSS":
                if Word[1] == "tag":
                    return Builder.HTML.Tag(Word[2], str(line.split("HTML.tag." + Word[2])[1]), class_="")


    def Meke(file : str, STEK : list, VARS : dict, BODY : list, comm_prefix : str):
        CuteScript.FLAG = "make"
        vars_ = VARS
        for line in BODY:
            if line == "":
                pass
            else:
                items = line.split()
                """Читаем кучу по линиям и делаем очередь из комманд"""  
                
                if comm_prefix + items[0] == "write" and CuteScript.FLAG == "make":
                    if items[2] in vars_ and items[1] in vars_:
                        Write_.write(vars_[items[1]], str(vars_[items[2]]))
                    else:
                        Write_.write(vars_[items[1]], str(items[2]))

                if comm_prefix + items[0] == "print" and CuteScript.FLAG == "make":
                    print(vars_[items[1]])

                if  comm_prefix + items[0] == "end":
                    break

    def start(file : str, comm_prefix = "") -> list:
        strat_time = time.time()
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
                        vars_[items[1]] = int(items[2])
                    except:
                        vars_[items[1]] = 0


                if items[0] == "str":
                    vars_[items[1]] = items[2]


                if items[0] == "rgb":
                    vars_[items[1]] = items[2].split(",")


                if items[0] == "@":
                    vars_[items[1]] = items[2]


                if comm_prefix + items[0] == "subtractionRGB":
                    Vec1 = Types.toIntVec(vars_[items[1]])
                    Vec2 = Types.toIntVec(vars_[items[2]])
                    vars_[items[1]] = Color.subtraction(Vec1, Vec2)


                if comm_prefix + items[0] == "additionRGB":
                    Vec1 = Types.toIntVec(vars_[items[1]])
                    Vec2 = Types.toIntVec(vars_[items[2]])
                    vars_[items[1]] = Color.addition(Vec1, Vec2)


                if comm_prefix + items[0] == "write" and CuteScript.FLAG == "main":
                    if items[2] in vars_ and items[1] in vars_:
                        Write_.WriteLine(vars_[items[1]], str(vars_[items[2]]))
                        STEK_COMMAND.append("write " + vars_[items[1]] + " " + str(vars_[items[2]]))
                    else:
                        Write_.WriteLine(items[1], items[2])
                        STEK_COMMAND.append("write " + items[1] + " " + items[2])


                if comm_prefix + items[0] == "getLine":
                    if items[2] in vars_ and items[1] in vars_:
                        try:
                            if Get_.getType(vars_[items[1]], (str(vars_[items[2]])).split("::")[1]) in type_list_action:
                                new_list = Get_.getLine(vars_[items[1]], (str(vars_[items[2]])).split("::")[1])
                                vars_[items[2]] = new_list.split(",")
                            else:
                                 vars_[items[2]] = Get_.getLine(vars_[items[1]], (str(vars_[items[2]])).split("::")[1])
                        except:
                            pass
                    else:
                        if Get_.getType(vars_[items[1]], items[2]) in type_list_action:
                            new_list = Get_.getLine(vars_[items[1]], items[2])
                            vars_[items[2]] = new_list.split(",")
                        else:
                            vars_[items[2]] = Get_.getLine(vars_[items[1]], items[2])          


                if comm_prefix + items[0] == "clone" and CuteScript.FLAG == "main":
                    vars_[ "clone_" + items[1]] =  vars_[items[1]]


                if items[0] in vars_ and items[1] == "=" and items[2] in vars_:
                    vars_[items[0]] = vars_[items[2]]


                if items[0] in vars_ and items[1] == "+" and items[2] in vars_:
                    try:
                        result = int(vars_[items[0]]) + int(vars_[items[2]])
                        vars_[items[0]] = result
                    except:
                        print("You are trying to perform mathematical addition not with numbers")


                if items[0] in vars_ and items[1] == "-" and items[2] in vars_:
                    try:
                        result = int(vars_[items[0]]) - int(vars_[items[2]])
                        vars_[items[0]] = result
                    except:
                        print("You are trying to do mathematical subtraction not with numbers")


                if comm_prefix + items[0] == "print" and CuteScript.FLAG == "main":
                    print(vars_[items[1]])


                if comm_prefix + items[0] == "toLine":
                    if str(items[1]) == "rgb":
                        normalize = []
                        for i in range(3):
                            normalize.append(str(vars_[items[3]][i]))
                        rgb_l = ",".join(normalize)
                    elif str(items[1]) == "int":
                        vars_[items[2]] = str(items[1]) + "::" + str(items[2]) + "::" + str(vars_[items[3]])


                if comm_prefix + items[0] == "loop":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    count = 0
                    while count < vars_[items[1]]:
                        for q in body[0].split("\n"):
                            STEK_COMMAND.append(CuteScript.command(q, vars_))
                        count += 1


                if comm_prefix + items[0] == "html":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    for q in body[0].split("\n"):
                        STEK_COMMAND.append(CuteScript.command(q, vars_))

                if comm_prefix + items[0] == "css":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    for q in body[0].split("\n"):
                        STEK_COMMAND.append(CuteScript.styler(q, vars_))              

                if comm_prefix + items[0] == "Make":
                    all_body = FILE.split("{")
                    make_body = all_body[1].split("}")[0]
                    CuteScript.Meke(
                        file=file,
                        STEK=STEK_COMMAND,
                        VARS=vars_,
                        BODY=make_body.split("\n"),
                        comm_prefix=comm_prefix
                    )

                if comm_prefix + items[0] == "build":
                    STEK = []
                    for i in STEK_COMMAND:
                        if i == None:
                            pass
                        else:
                            STEK.append(i)
                    if items[1] == "html":
                        Builder.HTML.build(vars_[items[2]], STEK)

        STEK = []
        for i in STEK_COMMAND:
            if i == None:
                pass
            else:
                STEK.append(i)

        print( "[STEK COMMAND] - " + str(STEK))
        print( "[Code execution time] - " + str(time.time() - strat_time) + "ms")
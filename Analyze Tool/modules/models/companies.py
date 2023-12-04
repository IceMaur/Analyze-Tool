class Company:
    def __init__(self, code, name, width_coord, length_coord, total = 0):
        self.__code = code
        self.__name = name
        self.__width_coord = width_coord
        self.__length_coord = length_coord
        self.__total = total

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
    def get_width_coord(self):
        return self.__width_coord

    def set_width_coord(self, width_coord):
        self.__width_coord = width_coord
        
    def get_length_coord(self):
        return self.__length_coord

    def set_length_coord(self, length_coord):
        self.__length_coord = length_coord

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total

    def showUnknown(self):
        print(self.__width_coord + ' ', self.__length_coord + ' ', self.__total)

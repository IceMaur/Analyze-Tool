class Inspector:
    def __init__(self, code, name='', location=''):
        self.__code = code
        self.__name = name
        self.__location = location
        self.__visit_reports = []

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location
        
    def get_visit_reports(self):
        return self.__visit_reports

    def add_visit_report(self, visit_report):
        self.__visit_reports.append(visit_report)

    def show(self):
        print(self.__code + ' ', self.__name + ' ', self.__location)
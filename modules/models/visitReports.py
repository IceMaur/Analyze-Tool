from datetime import date

class VisitReport:
    def __init__(self, inspector_code, company_code, visit_at, created_at, status, comment):
        self.__inspector_code = inspector_code
        self.__company_code = company_code

        self.__visit_at = self.__get_date_by_string(visit_at)
        self.__created_at = self.__get_date_by_string(created_at)

        self.__status = status
        self.__comment = comment

    def get_inspector_code(self):
        return self.__inspector_code

    def set_inspector_code(self, inspector_code):
        self.__inspector_code = inspector_code

    def get_company_code(self):
        return self.__company_code

    def set_company_code(self, company_code):
        self.__company_code = company_code

    def get_visit_at(self):
        return self.__visit_at

    def set_visit_at(self, visit_at):
        self.__visit_at = visit_at
        
    def get_created_at(self):
        return self.__created_at

    def set_created_at(self, created_at):
        self.__created_at = created_at
                
    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
                        
    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        self.__comment = comment

    def __get_date_by_string(self, date_string):
        """Get the date based on a string date"""
        if date_string:
            try:
                year_at = int(date_string[6:10])
                month_at = int(date_string[3:5])
                day_at = int(date_string[0:2])
                return date(year_at, month_at, day_at)
            except:
                return None
        
        return None
        
class Cell:
    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet
        self.__raw_content = '0'
        # Handle other cell references

    def set_content(self, value):
        self.__raw_content = value
        # Handle other cell references

    def get_content(self, value):
        return self.__raw_content
    
    def get_value(self):
        pass
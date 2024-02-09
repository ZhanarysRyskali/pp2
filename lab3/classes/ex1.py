#ex 1
class stringmanip:
    def get_string(self):
        self.string = str(input())
    def upper_case(self):
        return self.string.upper()
string = stringmanip()
string.get_string()
print(string.upper_case())
class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def __email(self):
        return self.__email

    @__email.setter
    def __email(self, value):
        self.__email = value

    @property
    def __file_name(self):
        return self.__file_name

    @__file_name.setter
    def __file_name(self, value):
        self.__file_name = value

    @property
    def __color(self):
        return self.__color

    @__color.setter
    def __color(self, value):
        self.__color = value

    def write(self, a, b, c, d):
        a.write(self.__full_name + "\n")
        b.write(self.__email + "\n")
        c.write(self.__file_name + "\n")
        d.write(self.__color + "\n")

#
import sys
import  re
sys.setrecursionlimit(1000)
file_path = "MOCK_DATA.txt"
file_r = open(file_path, mode="r", encoding="UTF-8")

fullname = "fullname.txt"
email = "email.txt"
file_name = "file_name.txt"
color = "color.txt"


results_fullname = open(fullname, mode="w", encoding="UTF-8")
results_email = open(email, mode="w", encoding="UTF-8")
results_file_name = open(file_name, mode="w", encoding="UTF-8")
results_color = open(color, mode="w", encoding="UTF-8")

my_text = file_r.read()

searcher_name = r"[A-Z][A-z]+\s[a-z]+\s\w+|"\
                r"[A-Z][A-z]+\s\w'\D{2}[A-z]+|"\
                r"[A-Z][A-z]+-[A-z]+|"\
                r"[A-Z][A-z]+\s[A-Z][A-z]+"


# searcher_email =r"[A-Z][A-z]+\t"


result_name = re.findall(searcher_name ,my_text)

for n in result_name:
    print(n)
    results_fullname.write(n + "\n")
print(len(result_name))

# for n1 in results_email:
#     print(n1)
#     results_email.write(n1 + "\n")
# print(len(results_email))
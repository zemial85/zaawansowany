import re


class FileManager:

    def find_py(self):
        pattern = re.compile("\.py")
        for line in open("/home/daniel/PycharmProjects/zaawansowany/nazwy.txt"):
            for match in re.finditer(pattern, line):


with FileManager() as py_finder:
    print(py_finder)
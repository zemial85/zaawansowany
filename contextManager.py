
class FileManager:
    def __init__(self, file_name, mod):
        self.file_name = file_name
        self.mod = mod
        self.file_object = None

    def __enter__(self):
        self. file_object = open(self.file_name, self.mod)
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()


def line_function():
    with open("Im_one_mb_file", "w+") as file_manager:
        num_chars = (1024 * 1024)/6
        file_manager.write("00000\n" * int(num_chars))


line_function()


textfile = "/home/daniel/PycharmProjects/zaawansowany/Im_one_mb_file"


def read_n(file, x):
    with open(file, mode='r') as fh:
        while True:
            data = ''.join(fh.readline() for _ in range(x))

            if not data:
                break

            yield data
            print()


for nlines in read_n(textfile,1):
    print(nlines.rstrip())








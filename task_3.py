import os
import io
import sys
import tempfile

class safe_write:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.backup = None
        self.did_exist = False

    def __enter__(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.backup = f.read()
            self.did_exist = True
        else:
            self.did_exist = False
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is not None:
            if self.did_exist:
                with open(self.filename, 'w', encoding='utf-8') as f:
                    f.write(self.backup)
            else:
                os.remove(self.filename)
            print(f"Во время записи в файл возникло исключение {exc_type.__name__}")
            return True
        return False

class T3:
    def run(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, 'test.txt')

            captured_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = captured_output

            try:
                with safe_write(file_path) as f:
                    f.write('Я знаю, что ничего не знаю, но другие не знают и этого.')

                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f.read())  

                with safe_write(file_path) as f:
                    f.write('Я знаю, что ничего не знаю, но другие не знают и этого. \n')

                with safe_write(file_path) as f:
                    print(
                        'Если ты будешь любознательным, то будешь много знающим.',
                        file=f, flush=True
                    )
                    raise ValueError  

                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f.read())  

            finally:
                sys.stdout = old_stdout

            return captured_output.getvalue().strip()
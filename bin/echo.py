import os
from datetime import datetime

class Echo:
    def echo(self, *text):
        yield " ".join(text)

    def pipe(self, before_pipe_text, file_name):
        if file_name:
            with open(file_name, 'w') as file:
                file.write(before_pipe_text)

            absolute_file_path = os.path.abspath(file_name)
            yield (f"file was created with name: {file_name}, and saved to the following path:\n {absolute_file_path}")

        elif not file_name:
            current_datetime = datetime.now()
            file_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

            with open(file_name, 'w') as file:
                file.write(before_pipe_text)

            absolute_file_path = os.path.abspath(file_name)
            yield (f"file was created with name: {file_name}, and saved to the following path:\n {absolute_file_path}")
from datetime import datetime


class logger:
    """
                   This class shall be used for logging purposes!!.

                   Written By: iNeuron Intelligence
                   Version: 1.0
                   Revisions: None

                   """
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")
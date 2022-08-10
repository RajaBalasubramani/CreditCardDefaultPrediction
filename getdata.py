from flask import Flask,request
import logger
class getdata():
    """
                   This class shall be used for getting data from the user!!.

                   Written By: iNeuron Intelligence
                   Version: 1.0
                   Revisions: None

                   """




    def __init__(self):
        self.file_object = open("Log.txt", 'a+')

        self.logwriter = logger.logger()
        try:
            self.sex = float(request.form['sex'])

            self.marriage = float(request.form['marriage'])

            self.age = float(request.form['age'])

            self.bill_amt = float(request.form['bill_amt'])

            self.education = float(request.form['education'])

            self.pay1 = float(request.form['pay1'])

            self.logwriter.log(self.file_object,"Getting input from the user is successfull")

        except Exception as e:
            self.logwriter.log(self.file_object,f"Didn't able to get data from the user due to {e}")



import getdata
import pickle
import logger



class prediction_():
    """
                       This class shall be used for predicting the user input with the model!!.
                       Written By: iNeuron Intelligence
                       Version: 1.0
                       Revisions: None
                       """

    def __init__(self,data):
        self.data = data
        self.file_object = open("Log.txt", 'a+')
        self.logwriter=logger.logger()

        self.filename = 'creditcardrandom.pickle'
        try:
            self.loaded_model = pickle.load(open('creditcardrandom.pickle', 'rb+'))
            self.logwriter.log(self.file_object,"Model loaded Successfully")
        except Exception as e:
            self.logwriter.log(self.file_object,f"Model doesn't load , Model loading failed due to {e}")
        try:
            self.predic = self.loaded_model.predict([[self.data.sex,self.data.marriage,self.data.age,self.data.bill_amt,
                                                      self.data.education,self.data.pay1]])
            self.logwriter.log(self.file_object, "Prediction Successfull")
        except Exception as e:
            self.logwriter.log(self.file_object,f"Prediction Failed due to {e}")
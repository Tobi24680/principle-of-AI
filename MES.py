import pandas as pd
class MedicalExpertSystem:
    def __init__(self):
        self.symptoms=[]
        self.diagnosis=None
        self.patient_data=pd.DataFrame(columns=["symptoms","Diagnosis"])
    def ask_question(self,question):
        answer=input(question +"(yes/no)").strip().lower()
        if answer=="yes":
            return True
        elif answer=="no":
            return False
        else:
            print("invalid input Enter yes or no")
            return self.ask_question(question)
    def diagnose(self):
        if self.ask_question("do you have a fever?"):
          self.symptoms.append("fever")
        if self.ask_question("do you have a headache?"):
          self.symptoms.append("headache")
        if self.ask_question("do you  have a cough"):
          self.symptoms.append("cough")
        new_data=pd.DataFrame({"Symptoms":[",".join(self.symptoms)],"Diagnosis":[""]})
        self.patient_data=pd.concat([self.patient_data,new_data],ignore_index="True")

        if "fever" in self.symptoms and "headache" in self.symptoms:
            self.diagnosis="You might have the flu."
        elif "fever" in self.symptoms and "cough" in self.symptoms:
            self.diagnosis="You might have the cold."
        else:
            self.diagnosis="your condition is unclear.please consult a doctor."
        self.patient_data.loc[self.patient_data.index[-1],"Diagnosis"]=self.diagnosis
    def run(self):
        print("welcome to MES")
        self.diagnose()
        print("Diagnosis",self.diagnosis)
        print("Patient Data")
        print(self.patient_data)
if __name__=="__main__":
  expert_system=MedicalExpertSystem()
  expert_system.run()
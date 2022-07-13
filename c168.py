class citizen:
    def __init__(self,name,dob,id_number):
        self.citizen_name=name
        self.citizen_dob=dob 
        self.citizen_id_number=id_number 
    def addcitizen(self):
        print("citizen name:" +self.citizen_name)
        print("citizen dob:"+str(self.citizen_dob))
        print("citizen id_number:"+self.citizen_id_number)
    def calculatingage(self):
        age=2022-self.citizen_dob
        print("age of citizen is:"+str(age)+"years")
        
    
citizen1=citizen("avantika",2010,"2013")
citizen1.addcitizen()
citizen1.calculatingage()
citizen2=citizen("ashaaz",2009,"0987")
citizen2.addcitizen()  
citizen2.calculatingage()    
        
    
        
       


        
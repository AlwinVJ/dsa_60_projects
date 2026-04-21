class StudentArray:
    def __init__(self):
        self.data = []
    
    def add_student(self,name,roll):
        self.data.append({"name":name,"roll":roll})
        
    def get_all(self):
        return self.data
    
    def search_students(self,roll):
        for student in self.data:
            if student["roll"] == roll:
                return student
        
        return None
    
    def delete_students(self,roll):
        for i in range(len(self.data)):
            if self.data[i]["roll"]==roll:
                del self.data[i]
                return True
        
        return False
class Resource( object ):
    class_counter= 0
    def __init__(self):
        
        self.id= Resource.class_counter
        Resource.class_counter += 1
        return id

from abc import ABC, abstractmethod


class StorageController(ABC):
    
    def __init__(self):
        super().__init__()
    pass


    @abstractmethod
    def save(self, id:any, obj:any):
        """must return some sort of ID
        
        Arguments:
            obj {any} -- [description]
        """
        pass
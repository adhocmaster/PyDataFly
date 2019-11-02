from ..storage.StorageController import StorageController
from ..library.Configuration import Configuration
import os


class FileStorageController(StorageController):

    def __init__(self, configuration: Configuration):
        # check if the directory exists
        self.directory = configuration.get('storage.directory')

        if os.path.isdir(self.directory) is False:
            os.mkdir(self.directory)

        pass


    def createFilePath(self, id:any):
        return  self.directory + '/' + str(id)


    def save(self, id:any, obj:any):
        s = str(obj)
        filename = self.createFilePath(id)
        with open(filename, 'w') as stream:
            stream.write(s)
        pass


    def exists(self, id:any):
        filename = self.createFilePath(id)
        return os.path.isfile(filename)

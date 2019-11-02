import unittest
from ..library.Configuration import Configuration
from ..storage.FileStorageController import FileStorageController
import os

class FileStorageControllerTest(unittest.TestCase):

    def test_save(self):
        controller = FileStorageController(Configuration())
        controller.save('testfile', 'Please save me')

        assert os.path.isfile(controller.createFilePath('testfile')) == True
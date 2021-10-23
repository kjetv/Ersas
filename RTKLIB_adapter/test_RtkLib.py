from sys import stderr
import unittest
from RtkLib import *

class TestRtkLib(unittest.TestCase):
    def test_runCommand(self):
        with self.assertRaises(BaseException):
            runCommand('adsfasgsfdg')
        self.assertEqual(runCommand('ls'), None)
        self.assertEqual(runCommand('cd'), None)
        self.assertEqual(runCommand('df -h'), None)
        self.assertEqual(runCommand('test -e convbin.exe'), None)
        self.assertEqual(runCommand('test -e rnx2rtkp.exe'), None)
    def test_convbin(self):
        notReconisableExample = getLibraryFolderPath('/testFiles/GunnerusBow.txt')
        ubxExample = getLibraryFolderPath('/testFiles/HavfruenBow.ubx')
        self.assertEqual(convbin(notReconisableExample, RecieverFormat.ubx), None)
        self.assertEqual(convbin(ubxExample), None)
        with self.assertRaises(TypeError):
            convbin(notReconisableExample)




if __name__ == "__main__":
    unittest.main()
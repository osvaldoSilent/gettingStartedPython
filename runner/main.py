#from PackageToInstall.Calculator.FullCalculator import FullCalculator
from Calculator.FullCalculator import FullCalculator
c = FullCalculator()
c.__init__()
print(f"Result: {c.sume()}")
print(f"Result: {c.rest()}")
print(f"Result: {c.cube()}")



#from PackageToInstall.FileHandler.File.HandlerFile import HandlerFile
#from PackageToInstall.FileHandler.File.HandlerFile import HandlerFile

#h = HandlerFile()
#h.__int__("D:/IntellijProjects/PythonProjects/primeroPasos/PackageToInstall/FileHandler/File/Generated/example.txt")

#h.setPath("D:/IntellijProjects/PythonProjects/primeroPasos/PackageToInstall/FileHandler/File/Generated/example2.txt")
#h.create()

#h.write("\nHola Mundo"+
#        "\nEstoy Aprendiendo python")
#h.read()

#h.overWrite("\nCiao Mondo"+
#            "\nsono imparando python")
#h.read()

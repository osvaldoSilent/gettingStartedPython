# ##############################################################
# #################USING CALCULATOR PACKAGE#####################
# ##############################################################
# # this code can work with none previous installation
# # with this code you can verify if the package used to install locally are working properly
# # you can't move this main.py if you want to run this code
# from package_to_install.setup_calculator.FullCalculator import FullCalculator
# main = FullCalculator()
# main.__int__()
# print(main.sumar())
# print(main.raiz())


##############################################################
##############USING PACKAGE FOR HANDLING FILES################
##############################################################
# from package_to_install.setup_fileHandler.MainHandler import MainHandler
# runner = MainHandler()
# runner.__init__()
# # (example) runner.operationW("operation","path","extension", "lines text") <---- this is for writing a existed file
# # (example) runner.operationR("operation","path","extension") <---- this is for reading a existed file
# runner.operationW("write","D:/IntellijProjects/PythonProjects/primeroPasos/generated/example",".txt","utf8",
#                 ("\nFirst paragraph of text"+
#                  "\nto show that you can add"+
#                  "\nnew lines without separator '/ / line / /' "+
#                  "\n\nSecond paragraph//line//"+
#                  "\nto show you can add new paragraphs"+
#                  "\nusing double \ n")
#                 )
# runner.operationR("read","D:/IntellijProjects/PythonProjects/primeroPasos/generated/example",".txt","utf8")

#############################################################
##USING FILEHANDLER PACKAGE INSTALLED IN YOUR PYTHON SYSTEM##
#############################################################
##### this code just can work after run "python setup sdist" on package_to_install and install
##### the packages found on dist directory which is generated after follow the previous step
##### also you can move this main.py and run this code wherever you want and run it successfully

#from setup_calculator.FullCalculator import FullCalculator
#from setup_fileHandler.MainHandler import MainHandler

#f = FullCalculator()
#f.__int__()
#print(f.sumar())
#print(f.raiz())

#runner = MainHandler()
#runner.__init__()
## (example) runner.operationW("operation","path","extension", "lines text") <---- this is for writing a existed file
## (example) runner.operationR("operation","path","extension") <---- this is for reading a existed file
#runner.operationW("write","D:/IntellijProjects/PythonProjects/primeroPasos/generated/example",".txt","utf8",
#                ("\nFirst paragraph of text"+
#                 "\nto show that you can add"+
#                 "\nnew lines without separator '/ / line / /' "+
#                 "\n\nSecond paragraph//line//"+
#                 "\nto show you can add new paragraphs"+
#                 "\nusing double \ n")
#                )
#runner.operationR("read","D:/IntellijProjects/PythonProjects/primeroPasos/generated/example",".txt","utf8")

from package_to_install.setup_binaryFiles.example import Persona
from package_to_install.setup_binaryFiles.example import BinaryFile
persona1 = Persona()
persona1.__int__("Osvaldo","26","H")
persona2 = Persona()
persona2.__int__("Isaac","26","H")
persona3 = Persona()
persona3.__int__("Silent","26","H")

file = BinaryFile()
file.__int__("fogo")
file.create()
file.addList(persona1)
file.addList(persona2)
file.addList(persona3)

file.saveList()


file.read()




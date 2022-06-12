##############################################################
##############################################################
##############################################################
##############################################################
## this code can work with none previous installation
## with this code you can verify if the package used to install locally are working properly
## you can't move this main.py if you want to run this code
#from package_to_install.setup_calculator.FullCalculator import FullCalculator
#main = FullCalculator()
#main.__int__()
#print(main.sumar())
#print(main.raiz())
##############################################################
from package_to_install.setup_fileHandler.MainHandler import MainHandler
runner = MainHandler()
runner.__init__()
runner.operationW("write","D:/IntellijProjects/PythonProjects/primeroPasos/FileHandler/nuevo",".txt","utf8",
                 ("\nFirst paragraph of text"+
                  "\nto show that you can add"+
                  "\nnew lines without separator '/ / line / /' "+
                  "\n\nSecond paragraph//line//"+
                  "\nto show you can add new paragraphs"+
                  "\nusing double \ n")
                 )
runner.operationR("read","D:/IntellijProjects/PythonProjects/primeroPasos/FileHandler/nuevo",".txt","utf8")

##runner.operation("write","D:/IntellijProjects/PythonProjects/primeroPasos/FileHandler/nuevo",".txt","utf8")

## (example) runner.operation("operation","path","extension")

##############################################################
##############################################################
##############################################################
##############################################################


##############################################################
##############################################################
##############################################################
##############################################################
## this code just can work after run "python setup sdist" on package_to_install and install
## the calculator package found on dist directory which is generated after follow the previous step
## also you can move this main.py and run this code wherever you want and run it successfully
#from setup_package.FullCalculator import FullCalculator
#f = FullCalculator()
#f.__int__()
#print(f.sumar())
#print(f.raiz())
##############################################################
##############################################################
##############################################################
##############################################################



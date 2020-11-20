##Get CSV File

from javax.swing import JFrame
from javax.swing import JFileChooser
import csv

frame = JFrame("File Chooser")
fileChooser = JFileChooser()

option = fileChooser.showOpenDialog(frame)

if option == JFileChooser.APPROVE_OPTION :
            selectedFile = fileChooser.getSelectedFile()
            print "Importing from file" + selectedFile.getAbsolutePath()
            #Open file for reading
            inputFile = csv.reader(open(selectedFile.getAbsolutePath()), delimiter=' ', quotechar='|')
            for row in inputFile :
                data = row[0].split(",")
                print "Importing Atrribute :" + data[0]

                dtType = Modelio.getInstance().getModelingSession().findByAtt(DataType,"Name",data[1])
                if dtType.size() == 0 :
                    print "Data type " + data[1] + " not found, so skipping " + data[0]
                    continue
                newAttr = Modelio.getInstance().getModelingSession().getModel().createElement("Attribute")
                newAttr.setName(data[0])
                newAttr.setType(dtType[0])
                newAttr.setOwner(elements[0])

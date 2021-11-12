import xml.etree.ElementTree as ET
import os


def xml2labels(file):

    tree = ET.parse(file)
    root = tree.getroot()
    img_name = file.replace('xml','jpg')
    output = '{"imageGcsUri": "gs://cloud-ai-platform-abfdcf95-6d4a-4065-a425-19eca8e4051b/'+img_name+'"'
    first_ship = True
    fileexit = "";
    for object in root.findall('object'):
        box = object.find('bndbox')
        xmin = box.find('xmin').text
        ymin = box.find('ymin').text
        xmax = box.find('xmax').text
        ymax = box.find('ymax').text
        xmin = int(xmin)/800
        ymin = int(ymin)/800
        xmax = int(xmax)/800
        ymax = int(ymax)/800
        
        if first_ship:
            output += ', "boundingBoxAnnotations": [{"displayName": "Ship", "xMin": "' 
            first_ship = False
        else:
            output += ', {"displayName": "Ship", "xMin": "' 
        output +=  str(xmin) + '", "yMin": "' + str(ymin) + '", "xMax": "' + str(xmax) + '", "yMax": "' + str(ymax) + '"}'
    if first_ship:
        output += '}'    
    else: 
        output += ']}' 
    return (output)

my_file=open("ImportImages15.jsonl","a")

for filename in os.listdir() :
    if filename.startswith('15'):
        jsonline = xml2labels(filename)
        my_file.write(jsonline+'\n')
        
#{"imageGcsUri": "gs://bucket/filename2.gif", "boundingBoxAnnotations": [{"displayName": "Tomato", "xMin": "0.8", "yMin": "0.2", "xMax": "1.0", "yMax": "0.4"},{"displayName": "Salad", "xMin": "0.0", "yMin": "0.0", "xMax": "1.0", "yMax": "1.0"}], "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "training"}}
#{"imageGcsUri": "gs://bucket/filename1.jpeg", "boundingBoxAnnotations": [{"displayName": "Tomato", "xMin": "0.3", "yMin": "0.3", "xMax": "0.7", "yMax": "0.6"}], "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "test"}}
    # for att in object.iter('bndbox'):
    #     for pos in att.getiterator():
    #         print(pos.tag, pos.attrib)

# "0.3", "yMin": "0.3", "xMax": "0.7", "yMax": "0.6"}], "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "test"}}'

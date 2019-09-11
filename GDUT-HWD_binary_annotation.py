import xml.etree.ElementTree as ET
from os import getcwd, getenv
from os.path import join

sets = ['trainval', 'test']
classes = ["hardhat", "none"]	#source: name field of labelmap_hardhat.prototxt


def convert_annotation(dataset_path, image_id, list_file):
    in_file = open(dataset_path + '/Annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        class_name = obj.find('name').text
        if class_name not in classes:
            continue
        class_id = classes.index(class_name)
        xmlbox = obj.find('bndbox')
        bbox = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        # print(class_name), print(class_id), print(bbox)
        # print(" " + ",".join([str(a) for a in bbox]) + ',' + str(class_id))
        list_file.write(" " + ",".join([str(a) for a in bbox]) + ',' + str(class_id))


# > main method
dataset_path = join(getenv("HOME"), 'data/Hardhat')
# print(dataset_path)

for image_set in sets:
    image_ids = open(dataset_path + '/ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('Hardhat_binary_%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/JPEGImages/%s.jpg'%(dataset_path, image_id))
        convert_annotation(dataset_path, image_id, list_file)
        list_file.write('\n')
    list_file.close()

# -- Test : convert_annotation
'''
image_id = '00669'
convert_annotation(dataset_path, image_id, list_file)
'''

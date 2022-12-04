import json
import xmltodict
import time


def convert():
    with open("schedule_tuesday.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()

        json_data = json.dumps(data_dict)
        with open("schedule_tuesday_lib.json", "w") as json_file:
            json_file.write(json_data)
            json_file.close()


start = time.time()
for i in range(100):
    convert()
print('lib parser for 100 examples worktime:' + str(time.time() - start))

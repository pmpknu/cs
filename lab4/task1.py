import time


class couple:
    def __init__(self):
        self.subject = None
        self.time = None
        self.address = None
        self.teacher = None
        self.format = None

    def str(self):
        return '\t\t"subject": "' + str(self.subject) + '",\n' +\
               '\t\t"time": "' + str(self.time) + '",\n' +\
               '\t\t"address": "' + str(self.address) + '",\n' +\
               '\t\t"teacher": "' + str(self.teacher) + '",\n' +\
               '\t\t"format": "' + str(self.format) + '"\n'


class schedule:
    def __init__(self, couples: list[couple]):
        self.couples = couples

class schedule_parse_xml:
    def parseline(self, line, couple):
        name = line[(line.find('<') + 1):line.find('>')]

        content = line.replace('<' + name + '>', '')
        content = content.replace('</' + name + '>', '')
        content = content.replace('\n', '')
        content = content[8:]

        if name == "subject":
            couple.subject = content
        elif name == "time":
            couple.time = content
        elif name == "address":
            couple.address = content
        elif name == "teacher":
            couple.teacher = content
        elif name == "format":
            couple.format = content

        return couple

    def run(self, fname):
        f = open(fname + '.xml', 'r')

        spec = '<?xml version="1.0" encoding="windows-1251"?>\n'
        xmlversion = f.readline()

        #print("XML opened")
        if spec not in xmlversion:
            print("Error:", xmlversion)
            f.close()
            return -1

        couples = []
        i = -1
        for line in f:
            if line.find("couple") != -1 and line.find("/couple") == -1:
                c = couple()
                couples.append(c)
                i += 1
            if line.find("schedule") == -1:
                couples[i] = self.parseline(line, couples[i])

        f.close()
        #print("XML closed")
        return schedule(couples)

class schedule_build_json:
    def build(self, schedule: schedule):
        finalstr = '{\n  "schedule": {\n'
        if len(schedule.couples) > 1:
            finalstr += '\t"couple": [\n'
        else:
            finalstr += '\t"couple": {\n'

        for c in schedule.couples:
            finalstr += '\t  {\n' + c.str() + '\t  },\n'

        finalstr = finalstr[:-2] + '\n'

        if len(schedule.couples) > 1:
            finalstr += '\t]\n'
        else:
            finalstr += '\t}\n'

        finalstr += '  }\n}'

        return finalstr

    def print_str_to_json(self, fname, s):
        f = open(fname + '_my.json', 'w')
        #print("JSON opened")
        f.write(s)
        #print("JSON closed")
        f.close()

def schedule_xml_to_json(fname):
    p = schedule_parse_xml()
    b = schedule_build_json()
    s = b.build(p.run(fname))
    b.print_str_to_json(fname, s)

start = time.time()
for i in range(100):
    schedule_xml_to_json('schedule_tuesday')
print('my parser for 100 examples worktime:' + str(time.time() - start))

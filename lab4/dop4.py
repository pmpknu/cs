class couple:
    def __init__(self):
        self.subject = None
        self.time = None
        self.address = None
        self.teacher = None
        self.format = None

    def str(self):
        return str(self.subject) + ',' + str(self.time) + ',' + str(self.address) + ',' + str(self.teacher) + ',' + str(self.format) + '\n'

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
        if spec in xmlversion:
            print("XML opened")
        else:
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
        print("XML closed")
        return schedule(couples)


class schedule_build_csv:
    def build(self, schedule: schedule):
        finalstr = 'subject,time,address,teacher,format\n'

        for c in schedule.couples:
            finalstr += c.str()

        return finalstr

    def print_str_to_csv(self, fname, s):
        f = open(fname + '_my.csv', 'w')
        print("CSV opened")
        f.write(s)
        print("CSV closed")
        f.close()

def schedule_xml_to_csv(fname):
    p = schedule_parse_xml()
    b = schedule_build_csv()
    s = b.build(p.run(fname))
    b.print_str_to_csv(fname, s)


schedule_xml_to_csv('schedule_tuesday')

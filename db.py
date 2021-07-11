import json
import re

class DB:

    def __init__(self, path):

        self.data = self.load_file(path)
        self.pre_process()

    def load_file(self, path):

        with open(path) as f:
            data = json.load(f)

        return data

    def pre_process(self):

        for i in self.data:
            try:
                text = i['openingHours']
                m = re.findall('([A-Z][a-z][a-z])(, | - )([A-z][a-z][a-z]) ([0-9]*:[0-9]* - [0-9]*:[0-9]*)', text)
                for x in m:
                    day = x[0] + x[1]
                    time = x[3]
                    new_day = day[0:3] + ' ' + time    

                    text = text.replace(day, "")
                    text = text + " / " + new_day
                i['openingHours'] = text
            except Exception as e:
                print(e)        
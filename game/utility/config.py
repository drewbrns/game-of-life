# /usr/bin/env python
import os
import json


class Preferences(object):

    def __init__(self):
        config = self.load_config()
        self.rows = config['rows']
        self.columns = config['columns']
        self.ratio = config['ratio']

    def load_config(self):
        try:
            p = os.path.join(os.getcwd(), 'game', 'utility', 'config.json')
            with open(p, 'r') as f:
                return json.load(f)
        except ValueError, e:
            print e
            return {'rows': 60, 'columns': 60, 'ratio': 0.4}
        except IOError, e:
            print e

    def save_config(self, config):
        p = os.path.join(os.getcwd(), 'game', 'utility', 'config.json')
        with open(p, 'w') as f:
            json.dumps(config, f)
            f.write(json.dumps(config, f))

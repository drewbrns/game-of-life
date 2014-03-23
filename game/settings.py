# /usr/bin/env python

class Settings(object):
    
    def __init__(self):
        
        
        os.path.join(BASE_DIR, 'static')
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))


    def load_config(self):
        try:
            with open(r'config.json','r') as f:
                return json.load(f)
        except ValueError:
            return {'size':100, 'ratio':0.6}
        except IOError:
            pass
    
    def save_config(self, config):        
        with open('config.json','w') as f:
            json.dumps(config,f)
            f.write(json.dumps(config,f))
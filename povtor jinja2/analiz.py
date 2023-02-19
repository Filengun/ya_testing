import json

import jinja2

with open('data.json') as f:
    incoming_request = f.read() #передали json входящий

template_base = jinja2.FileSystemLoader('')
env = jinja2.Environment(loader=template_base)
template = env.get_template('data2.json')
incoming_request_1  = json.loads(incoming_request)
print(incoming_request_1)
variable = template.render(incoming_request_1=incoming_request_1)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print(variable)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print(json.loads(variable))

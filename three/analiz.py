import json, jinja2

with open('data.json') as f:
    incoming_request = f.read() #передали json входящий

with open('data2.json') as w:
    template_base = w.read() #передали json шаблон


template = jinja2.Template(template_base)
incoming_request_1  = json.loads(incoming_request)
print(incoming_request_1)
variable = template.render(incoming_request_1=incoming_request_1)
#print(incoming_request)
print('----------')
print(variable)
print('----------')
print(json.loads(variable))

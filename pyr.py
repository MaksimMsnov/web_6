from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from wsgiref.simple_server import make_server
from jinja2 import FileSystemLoader,Environment

assets = [
'app.js',
'react.js',
'leaflet.js',
'D3.js',
'moment.js',
'math.js',
'main.css',
'bootstrap.css',
'normalize.css',
]

style = []
script = []

for element in assets:
  element_split = element.split('.')
  if element_split[1] == 'css':
    style.append(element)
  elif element_split[1] == 'js':
    script.append(element)
  
def index(request):
  envir = Environment(loader=FileSystemLoader('.'))
  template = envir.get_template('index.html').render(javascripts=script, styles=style)
  return Response(template)

def about(request):
  envir = Environment(loader=FileSystemLoader('.'))
  template = envir.get_template('about/about.html').render(javascripts=script, styles=style)
  return Response(template)

if __name__ == '__main__':
  config = Configurator() 
  config.add_route('index', '/')
  config.add_view(index, route_name='index')
  config.add_route('about', '/about')
  config.add_view(about, route_name='about')
  application = config.make_wsgi_app()
  server = make_server('0.0.0.0', 8000, application)
  server.serve_forever()
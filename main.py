import bottle
import os
import sys

@bottle.route('/downloads/<filename:path>',method='POST')
@bottle.route('/downloads/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./downloads')

@bottle.route('/pic/<filename:path>',method='POST')
@bottle.route('/pic/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./pic')
@bottle.route('/<filename:path>',method='POST')
@bottle.route('/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./mainpage')
@bottle.route('/',method='POST')
@bottle.route('/',method='GET')
def index():
    return bottle.static_file('mainpage/index.html', root='.')

@bottle.route('/tutorial',method='POST')
@bottle.route('/tutorial',method='GET')
def download():
    return bottle.static_file('tutorial.html', root='./tutorial')




if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
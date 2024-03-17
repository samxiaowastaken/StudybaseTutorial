import bottle
import os
import sys

@bottle.route('/downloads/<filename:path>',method='POST')
@bottle.route('/downloads/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./downloads')

@bottle.route('/pic/<filename:path>',method='POST')
@bottle.route('/pic/<filename:path>',method='GET')
def get_pic(filename):
    return bottle.static_file(filename, root='./pic')

@bottle.route('/tutorial/<filename:path>',method='POST')
@bottle.route('/tutorial/<filename:path>',method='GET')
def tutorial(filename):
    return bottle.static_file(filename+".html", root='./tutorial')
@bottle.route('/<filename:path>',method='POST')
@bottle.route('/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./mainpage')
@bottle.route('/',method='POST')
@bottle.route('/',method='GET')
def index():
    return bottle.static_file('mainpage/index.html', root='.')






if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
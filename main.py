import bottle
import os
import sys


@bottle.route('/<filename:path>',method='POST')
@bottle.route('/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./mainpage')
@bottle.route('/',method='POST')
@bottle.route('/',method='GET')
def index():
    return bottle.static_file('mainpage/index.html', root='.')

@bottle.route('/style.css',method='POST')
@bottle.route('/style.css',method='GET')
def index():
    return bottle.static_file('style.css', root='.')
@bottle.route('/download',method='POST')
@bottle.route('/download',method='GET')
def download():
    return bottle.static_file('downloads/download.html', root='./downloads')

@bottle.route('/download/<filename:path>',method='POST')
@bottle.route('/download/<filename:path>',method='GET')
def download(filename):
    return bottle.static_file(filename, root='./downloads')


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
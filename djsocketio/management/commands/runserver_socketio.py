from optparse import make_option

from django.core.management.base import BaseCommand
from django.utils.importlib import import_module
from django.conf import settings

from gevent import monkey

monkey.patch_all()

from socketio import socketio_manage
from socketio.server import SocketIOServer


namespaces = dict()

for app in settings.INSTALLED_APPS:
    try:
        live = import_module('%s.live' % app, 'live')
    except ImportError:
        pass
    else:
        Namespace = live.Namespace
        if hasattr(Namespace, 'name'):
            name = Namespace.name
        else:
            name = app.split('.')[-1]
        namespaces['/' + name] = Namespace


class Application(object):

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/')

        if path.startswith('socket.io'):
            socketio_manage(environ, namespaces)
        else:
            return not_found(start_response)


def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']


class Command(BaseCommand):
    help = 'Socket.io Server for Django'

    option_list = BaseCommand.option_list + (
        make_option(
            '--port',
            action='store',
            dest='port',
            default=8000,
            type='int',
            help='Port used for incomings socketio requests default to 8000'),
        make_option(
            '--host',
            action='store',
            dest='host',
            default=8000,
            help='Host'),
        )

    def handle(self, **options):
        print 'GO GO GO Socket IO'
        print 'Listening on port %s:%s' % (options['host'], options['port'])
        SocketIOServer(
            ('0.0.0.0', options['port']),
            Application(),
            resource='socket.io',
            policy_server=True,
            policy_listener=('0.0.0.0', 843),
        ).serve_forever()

Django SocketIO Alternative
===========================

Alternative Django support for Gevent SocketIO, this is based on 
`mrjmad example project <https://github.com/mrjmad/django_socketio_test>`_.

What is it useful for
---------------------

SocketIO is an abstraction layer over several methods to maintain a connection
between the client and the server otherwise said long-polling this includes
`websockets <http://www.w3.org/TR/websockets/>`.

Checkout `what are websockets? <http://talk.webplatform.org/forums/index.php/2290/what-are-websockets>`_.

Documentation
-------------

Add ``django_socketio_alt`` to your ``INSTALLED_APPS`` in ``settings.py``

Create a ``live.py`` in an application of your project. django-socketio-alt
will discover every ``live.py`` that are in applications installed against
Django, so becarful with what you do install in production. ``live.py`` can 
start like this::


  from socketio.namespace import BaseNamespace
  from socketio.mixins import RoomsMixin, BroadcastMixin


  class Namespace(BaseNamespace, RoomsMixin, BroadcastMixin):

      def emit_to_me(self, event, *args):
          pkt = dict(
               type="event",
               name=event,
               args=args,
               endpoint=self.ns_name)
          self.socket.send_packet(pkt)

You can specify a namespace name using the ``name`` property like so::

  class Namespace(BaseNamespace, RoomsMixin, BroadcastMixin):

      name = 'chat'

If you do not, the default is to use the name of the app, for instance if the 
app is registred as ``spam.egg.chat``, the namespace's name will be ``chat``.
Connection to this namespace in the client will be done using the following 
code::

  var socket = io.connect('http://localhost:8000/djchatio');

Now everything you need to know is in 
`Gevent SocketIO documentation <http://gevent-socketio.readthedocs.org>`_ 
and for some copy-paste goodness you can have a look at the example application
in `example directory <https://github.com/amirouche/django-socketio-alt/tree/master/example/djchatio/live.py>`_.

Happy living!


How to run the example application
----------------------------------

To run the example app you will need to install ``gevent-socketio``,
if you did not ``pip install django-socketio-alt`` already::

  $> pip install gevent-socketio

Since the default port for doing websocket is ``8000`` and the example
app use this default you need to run the django project on another port::

  $> ./manage.py 0.0.0.0:8001

Then run the SocketIO thread with the following command::

  $> ./manage.py runserver_socketio

Open two `http://0.0.0.0:8001/ <http://0.0.0.0:8001/>`_ windows
and start the conversation.


Links
-----

- `forge <https://github.com/amirouche/django-socketio-alt>`_
- `SocketIO <http://socket.io/>`_
- `Gevent SocketIO <http://gevent-socketio.readthedocs.org/>`_


Authors
-------

- `Mrjmad <https://github.com/mrjmad/>`_
- `Amirouche <https://github.com/amirouche/>`_

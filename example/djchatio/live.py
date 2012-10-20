import random

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin


nicknames = list()


class Namespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def emit_to_me(self, event, *args):
        pkt = dict(
             type="event",
             name=event,
             args=args,
             endpoint=self.ns_name)
        self.socket.send_packet(pkt)

    def on_nickname(self):
        A = random.choice('1234567890')
        B = random.choice('1234567890')
        nickname = 'user' + A + B
        nicknames.append(nickname)
        self.socket.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', nicknames)
        # Just have them join a default-named room
        self.join('main_room')
        self.emit_to_me('nickname', nickname)

    def recv_disconnect(self):
        # Remove nickname from the list.
        nickname = self.socket.session['nickname']
        nicknames.remove(nickname)
        self.broadcast_event('announcement', '%s has disconnected' % nickname)
        self.broadcast_event('nicknames', nicknames)
        self.disconnect(silent=True)

    def on_user_message(self, msg):
        self.emit_to_room(
            'main_room',
            'msg_to_room',
            self.socket.session['nickname'], msg
        )

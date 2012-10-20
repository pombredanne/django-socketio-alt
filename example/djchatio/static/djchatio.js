WEB_SOCKET_SWF_LOCATION = "/static/WebSocketMain.swf";
WEB_SOCKET_DEBUG = true;

// socket.io specific code
var socket = io.connect('http://localhost:8000/djchatio');

socket.on('connect', function () {
    socket.emit('nickname');
});

socket.on('nickname', function (msg) {
    $('#nickname').append($('<p>').append($('<em>').text(msg)));
});

socket.on('announcement', function (msg) {
    $('#lines').append($('<p>').append($('<em>').text(msg)));
});

socket.on('nicknames', function (nicknames) {
    $('#nicknames').empty();
    for (var i in nicknames) {
        $('#nicknames').append($('<li>').text(nicknames[i]));
    }
});

socket.on('msg_to_room', function message (from, msg) {
    $('#lines').append($('<p>').append($('<b>').text(from + ': '), msg));
});

socket.on('reconnect', function () {
    $('#lines').remove();
    message('System', 'Reconnected to the server');
});

socket.on('need_reconnect', function () {
    window.location="/";
});

socket.on('reconnecting', function () {
    message('System', 'Attempting to re-connect to the server');
});

socket.on('error', function (e) {
    message('System', e ? e : 'A unknown error occurred');
});


// send message
$(function () {
    $('#send').click(function () {
        $('#message').val();
        socket.emit('user message', $('#message').val());
        clear();
        $('#lines').get(0).scrollTop = 10000000;
        return false;
    });

    function clear () {
        $('#message').val('').focus();
    };
});

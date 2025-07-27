from  flask import Flask,render_template
from flask_socketio import SocketIO,emit
app=Flask(__name__)
socketio=SocketIO(app)
@app.route('/')
def index():
     return render_template('index.html')
@socketio.on('sendmessage')
def handle_send_message(data):
    username=data['username']
    message=data['message']
    print(f"{username}:{message}")
    emit('recievemessage',{'username':username,'message':message},broadcast=True)
if __name__=='__main__':
    socketio.run(app,debug=True)
import os
port=int(os.environ.get("PORT".5000))
socketio.run(app,host='0.0.0.0',port=port)


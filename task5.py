from  flask import Flask,render_template
from flask_socketio import SocketIO,emit
import os
app=Flask(__name__)
socketio=SocketIO(app)
@app.route('/')
def index():
     return render_template('index.html')
@socketio.on('sendmessage')
def handle_send_message(data):
    username=data['username']
    message=data['message']
    time=data['time']
    print(f"{username}:{message}:{time}")
    emit('recievemessage',{'username':username,'message':message,'time':time},broadcast=True)
if __name__=='__main__':
     port=int(os.environ.get('PORT',5000))
     socketio.run(app,host='0.0.0.0',port=port,debug=True)

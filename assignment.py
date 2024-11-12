from flask import Flask
import subprocess
import datetime
import pytz
import os
import getpass

app = Flask(__name__)

def get_system_info():
    try:
        username = getpass.getuser()
    except:
        username = "codespace"
        
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], 
                                           text=True,
                                           timeout=5)
    except:
        top_output = "Error fetching top data"
    
    return username, server_time, top_output

@app.route('/')
def home():
    return "Server is running. Go to /htop for system information."  # Fixed the message

@app.route('/htop')
def htop():
    username, server_time, top_output = get_system_info()
    
    html = f"""
    <pre>
Name: Akash Ghosh
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
    </pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
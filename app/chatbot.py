
import os
from langflow.load import run_flow_from_json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
TWEAKS = {
  "ChatInput-tbqTl": {},
  "AstraVectorStoreComponent-sN84D": {},
  "ParseData-APigB": {},
  "Prompt-xRrDe": {},
  "ChatOutput-EwNUM": {},
  "SplitText-EBiOn": {},
  "File-z490u": {},
  "AstraVectorStoreComponent-dEczs": {},
  "OpenAIEmbeddings-L1Wwg": {},
  "OpenAIEmbeddings-5Yo5i": {},
  "OpenAIModel-wFTJS": {},
  "File-mZ1Ez": {},
  "File-HVs8H": {}
}

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
   
@app.route('/chat',methods=['POST'])
def chat():
    name = request.form.get('name')
    print(name)
    result = run_flow_from_json(flow="flow.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
    print(result)
    if name:
        print('Request for chat page received with question =%s'% name)
        answer = result[0].outputs[0].results

if __name__ == '__main__':
   app.run()




from flask import Flask, render_template
from utils import show_all_script_files

app = Flask(__name__)


'''
An argument to the function is tied to the route variable 
'''

@app.route('/')
def index_page():
    '''
    Note to myself: render_template() will load a html template from the templates folder
    You can also pass arguments to this to be rendered in the html page
    '''

    page_title = "Serpent's Divination"

    script_file_data = show_all_script_files()

    print(script_file_data)

    return render_template('index.html', title=page_title, file_data = script_file_data)

if __name__ == '__main__':
    app.run(debug=True)
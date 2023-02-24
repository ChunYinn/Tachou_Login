from database import *

app = Flask(__name__)  

name = None
session = "logout"

@app.route('/', methods =["GET", "POST"])
def index():
    if (session!="login"):
        return redirect(url_for('login'))
    
    rework_list = get_rework_list()
    print(rework_list)

    return render_template("index.html", 
                        rework_list=rework_list,
                        name=name)


@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == 'POST':
        global name
        name = verify_login()
        if name != None:
            global session
            session ='login'
            print(session)
            return redirect('/')
        return redirect(url_for('login'))
    elif request.method=='GET':
        return(render_template('login.html'))

@app.route('/rework', methods =["GET", "POST"])
def rework():
    return render_template('rework.html')

if __name__=='__main__':
    app.run(debug=True)

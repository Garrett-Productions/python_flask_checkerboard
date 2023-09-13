from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html')

@app.route('/<int:num>')
def checkerboardChoose(num):
    print("This is my running function")
    return render_template('index2nd.html', num = num)

@app.route ('/<int:num>/<int:colnum>')
def chooseSetup(num,colnum):
    return render_template('index3rd.html', num = num, col = colnum)


@app.route ('/<int:num>/<int:colnum>/<color1>/<color2>')
def diffSetup(num,colnum,color1,color2):
    return render_template('index4th.html', num = num, col = colnum, color = color1, diffcolor = color2 )


if __name__=="__main__":
    app.run(debug=True, port = 5001)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        date_of_birth = request.form.get('dateofbirth')

        # يمكنك هنا إضافة أي معالجة أو تحقق من المدخلات إذا لزم الأمر
        return render_template('index.html', name=name, age=age, date_of_birth=date_of_birth)
    
    return render_template('index.html', name=None)

if __name__ == '__main__':
    app.run(debug=True)



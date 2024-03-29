from flask import render_template, request, redirect, url_for
from scat import app
from scat import db
from scat.models.employee import Employee


@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('scat/index.html', my_dict=my_dict)

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('scat/sampleform.html')
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します。')
        req1 = request.form['data1']
        return f'POST受け取ったよ: {req1}'

@app.route('/add_employee', methods=['GET', 'POST'])
def add_amployee():
    if request.method == 'GET':
        return render_template('scat/add_employee.html')
    if request.method == 'POST':
        form_name = request.form.get('name')  # str
        form_mail = request.form.get('mail')  # str
        # チェックなしならFalse。str -> bool型に変換
        form_is_remote = request.form.get('is_remote', default=False, type=bool)
        form_department = request.form.get('department')  # str
        # int, データないとき０
        form_year = request.form.get('year', default=0, type=int)

        employee = Employee(
            name=form_name,
            mail=form_mail,
            is_remote=form_is_remote,
            department=form_department,
            year=form_year
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))
    
@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('scat/employee_list.html', employees=employees)
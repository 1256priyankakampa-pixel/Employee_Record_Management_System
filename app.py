from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages


# ✅ Database connection
def get_db_connection():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn


# ✅ Homepage - List employees + Search + Department dropdown
@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('q', '').strip()
    conn = get_db_connection()

    # Fetch employees with optional search
    if search_query:
        employees = conn.execute(
            'SELECT * FROM employees WHERE name LIKE ? OR department LIKE ?',
            (f'%{search_query}%', f'%{search_query}%')
        ).fetchall()
    else:
        employees = conn.execute('SELECT * FROM employees').fetchall()

    # Fetch distinct departments for dropdown in Add modal
    departments = conn.execute(
        'SELECT DISTINCT department FROM employees WHERE department IS NOT NULL AND department != ""'
    ).fetchall()
    department_list = [d['department'] for d in departments]

    conn.close()
    return render_template(
        'index.html',
        employees=employees,
        search_query=search_query,
        department_list=department_list
    )


# ✅ Add employee (via modal)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)',
        (name, department, salary)
    )
    conn.commit()
    conn.close()

    flash('✅ Employee added successfully!', 'success')
    return redirect(url_for('index'))


# ✅ Edit employee details
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        salary = request.form['salary']

        conn.execute(
            'UPDATE employees SET name=?, department=?, salary=? WHERE id=?',
            (name, department, salary, id)
        )
        conn.commit()
        conn.close()

        flash('📝 Employee updated successfully!', 'info')
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', employee=employee)


# ✅ Delete employee with confirmation modal
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()
    conn.close()

    flash('🗑️ Employee deleted successfully!', 'danger')
    return redirect(url_for('index'))


# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)

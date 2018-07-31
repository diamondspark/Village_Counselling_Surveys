from flask import Flask, render_template, redirect, request, jsonify,make_response,send_from_directory,current_app
import os
import Driver

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sort_test',methods= ["GET"])
def sorting():
    uploads = '/Users/mop2014/Desktop/_Mohit/bi-att-flow'
    return send_from_directory(directory=uploads, filename='run-demo.py')


@app.route('/sort/<ph>/<kind>')
def app_sort(ph,kind,methods=["GET","POST"]):
    print "app_sort"
    if ph == '1':
        Driver.sort_ph1()
        uploads = '/data/Mohit/MyGarbage/Village_Counselling_Surveys/flaskapp/'
        if kind == 'csv':
            filename='ph1.csv'
        if kind =='excel':
            filename = 'ph1.xlsx'
        return send_from_directory(directory=uploads, filename=filename, cache_timeout=-1, as_attachment=True)
    if ph =='2':
        Driver.sort_ph2()
        uploads = '/data/Mohit/MyGarbage/Village_Counselling_Surveys/flaskapp/'
        if kind == 'csv':
            filename='ph2.csv'
        if kind =='excel':
            filename = 'ph2.xlsx'
        return send_from_directory(directory=uploads, filename=filename, cache_timeout=-1, as_attachment=True)

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

##    df = Driver.sort(col_name)
##    df.to_excel('/home/ubuntu/flaskapp/data/sorted_repo.xlsx')
###    df.to_excel('/var/www/html/flaskapp/data/sorted_repo.xlsx')
##    uploads = '/home/ubuntu/flaskapp/data/'
##    return send_from_directory(directory=uploads, filename='sorted_repo.xlsx')
####    print df.head()

if __name__ == "__main__":
    app.run(debug=True)

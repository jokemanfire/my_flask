from flask import Flask,render_template,request,redirect,url_for
from db_search import select_database
from config import server_config as ss
import time
import datetime
import random

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/result', methods=['GET','POST'])
def do_this():
    if request.method == 'POST':
      #获得数据
        destination = request.form.get('destination')
        d1 = request.values.get('sexrdo')
        d2 = request.values.getlist('chkhobby')
      #得到时间差
        date = request.values.getlist('date')
        date1 = date[0]
        date2 = date[1]
        t1 = time.strptime(date1,'%Y-%m-%d')
        t2 = time.strptime(date2,'%Y-%m-%d')
        #print(t1[:3],t2[:3])
        t1 = datetime.datetime(*t1[:3])
        t2 = datetime.datetime(*t2[:3])
        b_date = (t2-t1).days
      #判断输入数据
        #print(destination)
        #print('-------------')
        if destination.strip() == '':
            return render_template('error.html')
       #判断时间
        if b_date <= 0:
            return render_template('error.html')
        print(destination,d1,d2,b_date)

        food, view, hotel = select_database(destination,d1,d2[0],d2[1],d2[2],b_date)
        #print(food,view,hotel)
        if food == -1:
            return render_template('error.html')
       #计算预算
        totol_money = 0
        for k in food:
            if k != None:
                totol_money += k[4]*3*b_date
                break
        for j in hotel:
            if j != None:
                totol_money += j[4]*b_date
                break
        if d1 == '女':
            totol_money += random.randint(100, 200)
        elif d1 == '男':
            totol_money += random.randint(50,100)
        return render_template('result.html',food=food, view=view, hotel=hotel,totol_money=totol_money)
    else:
        return redirect(url_for('main'))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def no_page(e):
    return render_template('500.html')

if __name__ == '__main__':
    app.run()

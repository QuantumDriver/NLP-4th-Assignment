from flask import Flask, render_template

app = Flask(__name__)

# 如何返回一个网页
# 如何给模板填充数据
@app.route('/')
def index():

    # 比如需要传递网址
    url_str = 'www.itheimaaaa.com'

    return render_template('index.html', url_str=url_str)

if __name__ == '__main__':
    # debug可以实时更新
    app.run(debug=True)


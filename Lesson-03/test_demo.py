# 1.导入Flask类作为扩展
from flask import Flask
# 2.创建Flask类的实例，
# __name__参数的作用是确定资源所在路径
app = Flask(__name__)

# 3.定义路由及视图函数
# Flask中定义路由是通过装饰器实现的
# 路由默认只支持GET，如果需要增加，要自行指定
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return '一路顺风呀~'

# 使用同一个视图函数来显示不同用户的订单信息
# <>定义路由的参数，<>内需要起个名字
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    # <order_id>
    # 参数类型，默认是字符串 unicode
    print(type(order_id))

    # 有的时候需要对路由做访问优化，订单应该是int类型

    # 需要在视图函数的()内填入参数名，后面的代码才能进行使用
    return 'order_id %s' % order_id

# 4.启动程序
if __name__ == '__main__':
    # 执行了app.run()就会将Flask程序运行在一个简易的服务器上(Flask提供)
    app.run()


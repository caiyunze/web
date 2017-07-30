@application.route('/')
def index():
    """首页
    使用模板显示页面
    """
    # 读取已提交的数据
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

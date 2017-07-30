@application.route('/post', methods=['POST'])
def post():
    """用于提交评论的URL
    """
    # 获取已提交的数据
    name = request.form.get('name')  # 名字
    comment = request.form.get('comment')  # 留言
    create_at = datetime.now()  # 投稿时间（当前时间）
    # 保存数据
    save_data(name, comment, create_at)
    # 保存后重定向到首页
    return redirect('/')

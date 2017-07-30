def load_data():
    """返回已提交的数据
    """
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    # 返回greeting_list。如果没有数据则返回空表
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

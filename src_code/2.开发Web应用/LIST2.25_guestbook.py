@application.template_filter('nl2br')
def nl2br_filter(s):
    """将换行符置换为br标签的模板过滤器
    """
    return escape(s).replace('\n', Markup('<br>'))


@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """使datetime对象更容易分辨的模板过滤器
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')

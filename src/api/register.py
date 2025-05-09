"""
@File: register.py
@Date: 2024/6/13 10:20
@desc: 统一接口注册
"""
import traceback
from flask import request, jsonify
from wpylib.util.http import resp_error
from src.init.init import global_instance_flask, global_instance_logger


# 注册错误handler
@global_instance_flask.get_instance_app().errorhandler(Exception)
def error_handler(e):
    """
    全局异常捕获
    """
    request_base_url = request.base_url

    if request_base_url.endswith("/api") or request_base_url.endswith("/api/"):
        return jsonify({
            "data": "ok",
        })

    if request_base_url.endswith("/favicon.ico") or request_base_url.endswith("/favicon.ico/"):
        return jsonify({
            "data": "ok",
        })

    # 非根路径的请求
    global_instance_logger.log_error(
        msg="error_handler",
        biz_data={
            "exception": traceback.format_exc(),
            "exception_msg": f"{e!r}",
            "request_base_url": request_base_url,
        }
    )
    return resp_error(data={"exception": f"{e!r}"})


def register():
    """
    注册接口
    1. 注意访问地址必须和配置的路由一样, 如果最后没有配置/分隔符, 访问的时候也不要加
    """
    # 1. 获取全局flask实例
    app = global_instance_flask.get_instance_app()

    # 2. 注册接口
    # app.add_url_rule(
    #     '/api/xx/xx', view_func=xx, methods=['GET']
    # )

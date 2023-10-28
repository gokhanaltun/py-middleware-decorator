def add_middlewares(middleware_list: []):
    def decorator(view_func):
        def wrapper(*args, **kwargs):
            for middleware_func in middleware_list:
                response = middleware_func(*args, **kwargs)
                if response:
                    return response
            return view_func(*args, **kwargs)
        return wrapper
    return decorator

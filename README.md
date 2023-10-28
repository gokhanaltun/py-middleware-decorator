# Flask and Django middleware decorator for spesific routes

This module allows you to add route-specific middlewares to your view functions in Flask and Django.

Example:

```python
from middleware_decorator import add_middlewares
from middlewares import middleware1, middleware2
 
@add_middlewares([middleware1, middleware2])
def index_view(request):
    # You can perform view operations here.
    return response
```


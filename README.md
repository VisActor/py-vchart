# py-vchart

Install 
```
  pip3 install py-vchart==1.0.0
```

Usage
```python
from pyvchart import render_chart
# spec的定义参考 https://www.visactor.io/vchart/guide/getting-started 中的json
spec = {
  "type": 'bar',
  "data": [
    {
      "id": 'barData',
      "values": [
        { "month": 'Monday', "sales": 22 },
        { "month": 'Tuesday', "sales": 13 },
        { "month": 'Wednesday', "sales": 25 },
        { "month": 'Thursday', "sales": 29 },
        { "month": 'Friday', "sales": 38 }
      ]
    }
  ],
  "xField": 'month',
  "yField": 'sales',
  "crosshair": {
    "xField": { "visible": True }
  }
};

render_chart(spec)

```


```python
# spec 必填参数
spec 是一个vchart 格式的json数据，格式如上图示例
# 可选参数
width = '500px'
height = '500px'
colors = ['#EB6F02', '#76BEC8', '#D44977', '#EF85A7', '#675DAE', '#B6BC65', '#829E0B', '#A6A6E1'];

render_chart(obj, width, height, colors)
```
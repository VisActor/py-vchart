# py-vchart

```python
from pyvchart import render_chart
# spec的定义参考 https://www.visactor.io/vchart/guide/getting-started 中的json
spec = {
    "type": "line",
    "xField": "x",
    "yField": "y",
    "data": [
        {
            "name": "lineData",
            "values": [
                {
                    "x": 0,
                    "y": 28
                },
                {
                    "x": 1,
                    "y": 43
                },
                {
                    "x": 2,
                    "y": 81
                },
                {
                    "x": 3,
                    "y": 19
                },
                {
                    "x": 4,
                    "y": 52
                },
                {
                    "x": 5,
                    "y": 24
                },
                {
                    "x": 6,
                    "y": 87
                },
                {
                    "x": 7,
                    "y": 17
                },
                {
                    "x": 8,
                    "y": 17
                },
                {
                    "x": 9,
                    "y": 49
                }
            ]
        }
    ]
}

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
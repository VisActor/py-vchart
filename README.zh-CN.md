<div align="center">
  <a href="https://github.com/VisActor#gh-light-mode-only" target="_blank">
    <img alt="VisActor Logo" width="200" src="https://github.com/VisActor/.github/blob/main/profile/logo_500_200_light.svg"/>
  </a>
  <a href="https://github.com/VisActor#gh-dark-mode-only" target="_blank">
    <img alt="VisActor Logo" width="200" src="https://github.com/VisActor/.github/blob/main/profile/logo_500_200_dark.svg"/>
  </a>
</div>

<div align="center">
  <h1>PyVchart</h1>
</div>

<div align="center">

[English](./README.md) | 简体中文

</div>

## 简介
  PyVchart 是VChart图表库的python包，支持在Notebook和python环境中渲染图表

### 安装
```
  pip3 install py-vchart==1.0.0
```

### 使用
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
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

English| [简体中文](./README.zh-CN.md)

</div>

## Doc
PyVchart is a Python package for the VChart chart library, which supports rendering charts in both Notebook and Python environments.


### Install 
```
  pip3 install py-vchart==1.0.0
```

### 📊 A Chart Example

<img src="https://user-images.githubusercontent.com/135952300/246996854-95cf0db3-42a2-41f9-8f15-8b7bbec1794c.png" style="width: 500px">

```python
from pyvchart import render_chart
# spec's definition referenced in the JSON of https://www.visactor.io/vchart/guide/getting-started
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
# spec required
spec is a JSON data in vchart format, as shown in the example above.
# optional params
width = '500px'
height = '500px'
colors = ['#EB6F02', '#76BEC8', '#D44977', '#EF85A7', '#675DAE', '#B6BC65', '#829E0B', '#A6A6E1'];

render_chart(obj, width, height, colors)
```
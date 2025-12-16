<p align="center">
    <img src="https://github.com/VisActor/.github/raw/main/profile/logo_500_200_dark.svg" alt="pyvchart logo" width=200 height=200 />
</p>
<h1 align="center">pyvchart</h1>
<p align="center">
    <em>Python ❤️ VChart = pyvchart</em>
</p>
<p align="center">
    <a href="https://github.com/pyvchart/pyvchart/actions">
        <img src="https://github.com/pyvchart/pyvchart/actions/workflows/python-app.yml/badge.svg" alt="Github Actions Status">
    </a>
    <a href="https://codecov.io/gh/pyvchart/pyvchart" >
        <img src="https://codecov.io/gh/pyvchart/pyvchart/branch/main/graph/badge.svg?token=q4Op7n64fK" alt="Codecov"/>
    </a>
</p>
<p align="center">
    <a href="https://github.com/pyvchart/pyvchart/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

[中文 README](README.md) | [English README](README.en.md) | [日本語（にほんご）README](README.jp.md)

## 📣 简介

[VisActor/VChart](https://github.com/VisActor/VChart) 是一个由字节跳动开源可视化解决方案 VisActor 的核心图表组件库。它基于它基于可视化语法库 VGrammar 和渲染引擎 VRender 进行封装，在满足数据呈现的同时，还支持面向叙事场景的动画编排、丰富的交互能力和定制化的图表风格，简单易用的配置大大降低了用户的学习成本。而 Python 是一门富有表达力的语言，非常适合用于数据处理、AI 等场景。当数据分析，建模遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts) 和 [py-vchart](https://github.com/VisActor/py-vchart) 诞生了。

## ✨ 特性

* [pyecharts](https://github.com/pyecharts/pyecharts) like 的 API 设计，使用如丝滑般流畅，支持链式调用
* 囊括了 VChart 的所有图表，应有尽有
* 支持主流 Notebook 环境，Jupyter Notebook、JupyterLab (**Coming soon...**)
* 可轻松集成至 Flask，Sanic，Django 等主流 Web 框架 (**Coming soon...**)
* 高度灵活的配置项，可轻松搭配出精美的图表
* 详细的文档和示例，帮助开发者更快的上手项目

## 🔰 安装

**pip 安装**
```shell
# 安装
$ pip install py-vchart -U

```

**源码安装**
```shell
# 源码安装
$ git clone https://github.com/VisActor/py-vchart.git
$ cd py-vchart
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 使用

使用案例在此处：[Examples](https://github.com/pyvchart/chart-examples)

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -r test/requirements.txt
$ make
```

### 集成测试

使用 Github Actions 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 😉 Author

pyvchart 主要由以下几位开发者开发维护

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)
* [@FunctionRun](https://github.com/FunctionRun)

更多贡献者信息可以访问 [pyvchart/graphs/contributors](https://github.com/pyvchart/pyvchart/graphs/contributors)

## 💡 贡献 [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/VisActor/py-vchart/blob/main/CONTRIBUTING.md#your-first-pull-request)

如想参与贡献，请先阅读[行为准则](./CODE_OF_CONDUCT.md) 和[贡献指南](./CONTRIBUTING.zh-CN.md)。

细流成河，终成大海！

期待能有更多的开发者参与到 pyvchart 的开发中来，我们会保证尽快 Reivew PR 并且及时回复。但提交 PR 请确保

1. 通过所有单元测试，如若是新功能，请为其新增单元测试
2. 遵守开发规范，使用 black 以及 isort 格式化代码（$ pip install -r requirements-dev.txt）
3. 如若需要，请更新相对应的文档

我们也非常欢迎开发者能为 pyvchart 提供更多的示例，共同来完善文档，~~文档项目位于 [pyvchart/website](https://github.com/pyvchart/website)~~ (文档在准备中...)

<a href="https://github.com/visactor/py-vchart/graphs/contributors"><img src="https://contrib.rocks/image?repo=visactor/py-vchart" /></a>

## Star History

<a href="https://gitdata.xuanhun520.com/#VisActor/py-vchart&Date">
<picture >
  <source media="(prefers-color-scheme: dark) and (max-width: 800px)" srcset="https://gitdata.xuanhun520.com/api/starimg?repos=VisActor/py-vchart&type=Date&theme=dark" />
  <source  media="(prefers-color-scheme: light) and (max-width: 800px)" srcset="https://gitdata.xuanhun520.com/api/starimg?repos=VisActor/py-vchart&type=Date&theme=light" />
  <img style="width: 800px; height: 533px;" alt="Star History Chart" src="https://gitdata.xuanhun520.com/api/starimg?repos=VisActor/py-vchart&type=Date&theme=dark" />
</picture>
</a>


## 📃 License

MIT [©VisActor](https://github.com/VisActor)

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

## 📣 Introduction

[VisActor/VChart](https://github.com/VisActor/VChart) is a core chart component library of the open-source visualization solution VisActor by ByteDance. It is based on the visualization grammar library VGrammar and the rendering engine VRender, providing not only data presentation but also support for animation orchestration for narrative scenarios, rich interaction capabilities, and customizable chart styles. The simple and easy-to-use configuration greatly reduces the learning cost for users. Python, with its expressive syntax, is well-suited for data processing and AI scenarios. When data analysis and modeling meet data visualization, [pyecharts](https://github.com/pyecharts/pyecharts) and [pyvchart](https://github.com/pyvchart/pyvchart) were born.

## ✨ Features

* API design similar to [pyecharts](https://github.com/pyecharts/pyecharts), smooth and fluent usage, supports method chaining
* Includes all charts from VChart, everything you need
* Supports mainstream Notebook environments, Jupyter Notebook, JupyterLab (**Coming soon...**)
* Can be easily integrated into mainstream Web frameworks such as Flask, Sanic, Django (**Coming soon...**)
* Highly flexible configuration options, allowing for the creation of beautiful charts with ease
* Detailed documentation and examples to help developers get started quickly

## 🔰 Installation

**pip installation**
```shell
# Install
# 【❕Note❕】Currently, it cannot be used because there is an old, unmaintained project with a similar name on PyPI, and it is temporarily unable to upload the wheel to PyPI.
$ pip install pyvchart -U

# Temporary Solution
$ pip install git+https://github.com/pyvchart/pyvchart@v0.1.0
```


**Source code installation**
```shell
# Install version v1 and above
$ git clone https://github.com/pyvchart/pyvchart.git
$ cd pyvchart
$ pip install -r requirements.txt
$ python setup.py install
```


## 📝 Usage

Usage examples are here：[Examples](https://github.com/pyvchart/chart-examples)

## ⛏ Code Quality

### Unit Testing

```shell
$ pip install -r test/requirements.txt
$ make
```


### Integration Testing

Using GitHub Actions for continuous integration.

### Code Style

Using [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/), and [pylint](https://www.pylint.org/) to improve code quality.

## 😉 Author

pyvchart is mainly developed and maintained by the following developers

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

More contributor information can be found at [pyvchart/graphs/contributors](https://github.com/pyvchart/pyvchart/graphs/contributors)

## 💡 Contribution

We look forward to more developers participating in the development of pyvchart. We will ensure timely review of PRs and prompt responses. However, when submitting a PR, please ensure:

1. All unit tests pass, and add unit tests for new features if necessary
2. Adhere to the development guidelines, format the code using black and isort (run `$ pip install -r requirements-dev.txt`)
3. Update relevant documentation if necessary

We also welcome developers to provide more examples for pyvchart to help improve the documentation. The documentation project is located at [pyvchart/website](https://github.com/pyvchart/website)

## 📃 License

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)
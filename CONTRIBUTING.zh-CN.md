首先为你选择加入开源贡献行列的行为点赞 👍🏻。再者，十分感谢你选择参与到 VisActor 社区，为这个开源项目做出贡献。

## py-vchart 贡献指南

py-vchart 团队通常在 github 上进行开发和 issue 维护，请打开 [Github 网站](https://github.com/)，点击右上角 `Sign up` 按钮，注册一个自己的账号，开启你开源之旅的第一步。

在 [py-vchart 仓库](https://github.com/VisActor/py-vchart)中，我们有一份面向所有开源贡献者的[指南](https://github.com/VisActor/py-vchart/blob/develop/CONTRIBUTING.zh-CN.md)，介绍了有关版本管理、分支管理等内容，**请花几分钟时间阅读了解一下**。

## 你的第一个 Pull Request

### Step0：安装 Git

Git 是一种版本控制系统，用于跟踪和管理软件开发项目中的代码变更。它帮助开发者记录和管理代码的历史记录，方便团队协作、代码版本控制、合并代码等操作。通过 Git，您可以追踪每个文件的每个版本，并轻松地在不同版本之间进行切换和比较。Git 还提供了分支管理功能，使得可以同时进行多个并行开发任务。

- 访问 Git 官方网站：<https://git-scm.com/>
- 下载最新版本的 Git 安装程序。
- 运行下载的安装程序，按照安装向导的提示进行安装。
- 安装完成后，你可以通过命令行使用 `git version` 命令确认安装成功。

### Step1：Fork 项目

- 首先需要 fork 这个项目，进入[py-vchart 项目页面](https://github.com/VisActor/py-vchart)，点击右上角的 Fork 按钮

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/fork.PNG)

- 你的 github 帐号中会出现 xxxx(你的 github 用户名)/py-vchart 这个项目
- 在本地电脑上使用以下命令: 得到一个 py-vchart 文件夹

```
// ssh
git clone git@github.com:xxxx(你的github用户名)/py-vchart.git
// https
git clone https://github.com/xxxx(你的github用户名)/py-vchart.git
```

### Step2：获取项目代码

- 进入 py-vchart 文件夹，添加 py-vchart 的远程地址

```
git remote add upstream https://github.com/VisActor/py-vchart.git
```

- 获取 py-vchart 最新源码

```
git pull upstream develop
```

### Step3：创建分支

- 好了，现在可以开始贡献我们的代码了。py-vchart 默认分支为 develop 分支。无论是功能开发、bug 修复、文档编写，都请新建立一个分支，再合并到 develop 分支上。使用以下代码创建分支：

```
// 创建功能开发分支
git checkout -b feat/xxxx

// 创建问题修复开发分支
git checkout -b fix/xxxx

// 创建文档、demo分支
git checkout -b docs/add-funnel-demo
```

假设我们创建了文档修改分支 `docs/add-funnel-demo`

- 现在我们可以在分支上更改代码了
- 假设我们已经添加了一些代码，提交到代码库
- git commit -a -m "docs: add custom funnel demo and related docs" 。VisActor 的 commit 提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 规范

  - `<type>[optional scope]: <description>`
  - 其中常用的`type`包括 docs（文档、日志修改）、feat（新功能）、fix（问题修复）、refactor（代码重构）等，请根据实际情况选择。
  - 请用简短精确的英文描述编写 description

### Step4：合并修改

- 一个常见的问题是远程的 upstream (@visactor/py-vchart) 有了新的更新， 从而会导致我们提交的 Pull Request 时会导致冲突。 因此我们可以在提交前先把远程其他开发者的 commit 和我们的 commit 合并。使用以下代码切换到 develop 分支:

```
git checkout develop
```

- 使用以下代码拉出远程的最新代码:

```
git pull upstream develop
```

- 切换回自己的开发分支:

```
git checkout docs/add-funnel-demo
```

- 把 develop 的 commit 合并到自己分支：

```
git rebase develop
```

- 把更新代码提交到自己的分支中:

```
git push origin docs/add-funnel-demo
```

### Step5：提交 Pull Request

你可以在你的 github 代码仓库页面点击 `Compare & pull request` 按钮。

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR.png)

或通过 `contribute` 按钮创建：

<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR-2.png">
</div>

按照模板填写本次提交的修改内容：

- 勾选这是什么类型的修改
<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-checklist.png">
</div>

- 填写关联的 issue

<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/related-issue.png">
</div>

- 若有复杂变更，请说明背景和解决方案

<div align='center'>
<img style="height:120px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-background.png">
</div>

相关信息填写完成后，点击 Create pull request 提交。

## **轻松步入 py-vchart 开源贡献之旅**

"**good first issue**" 是一个在开源社区常见的标签，这个标签的目的是帮助新贡献者找到适合入门的问题。

py-vchart 的入门问题，你可以通过 [issue 列表](https://github.com/VisActor/py-vchart/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) 查看，目前包括两类：

- Demo 案例制作
- 简单功能开发

如果你当前**有时间和意愿**参与到社区贡献，可以在 issue 里看一看 **good first issue**，选择一个感兴趣、适合自己的认领。

相信你一定是一个有始有终的同学，所以，当你了解并决定认领一个 issue 后，请在 issue 下留言告知大家。

### Demo Task 开发指南

待补充...

## 拥抱 VisActor 社区

在你为 VisActor 贡献代码之余，我们鼓励你参与其他让社区更加繁荣的事情，比如：

1. 为项目的发展、功能规划 等提建议。
2. 创作文章、视频，开办讲座来宣传 VisActor。
3. 撰写推广计划，同团队一同执行。

VisActor 也在努力帮助参与社区建设的同学一同成长，我们计划（但不限于，期待大家更多的建议）提供如下帮助：

1. 以 VisActor 为基础的数据可视化研发培训，帮助参与的同学在编程技能、可视化理论、架构设计等多个方面快速成长。
2. 定期评选“代码贡献奖”和“社区推广奖”。
3. 组织社区成员参与开源活动。

## 常见问题

待补充...

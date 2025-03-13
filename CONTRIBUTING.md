First of all, we'd like to give you a thumbs up 👍🏻 for choosing to join the open-source contribution community. Moreover, we're extremely grateful that you've chosen to participate in the VisActor community and contribute to this open-source project.

## py-vchart Contribution Guide

The py-vchart team typically conducts development and issue maintenance on GitHub. Please visit the [GitHub website](https://github.com/), click the `Sign up` button in the top right corner, and register your own account to take the first step on your open-source journey.

In the [py-vchart repository](https://github.com/VisActor/py-vchart), we have a [guide](https://github.com/VisActor/py-vchart/blob/develop/CONTRIBUTING.zh-CN.md) for all open-source contributors, which covers topics such as version management and branch management. **Please take a few minutes to read and understand it.**

## Your First Pull Request

### Step 0: Install Git

Git is a version control system used to track and manage code changes in software development projects. It helps developers record and manage the history of code, facilitating team collaboration, code version control, code merging, and other operations. With Git, you can track every version of each file and easily switch between and compare different versions. Git also provides branch management functionality, allowing multiple parallel development tasks to be carried out simultaneously.

- Visit the official Git website: <https://git-scm.com/>
- Download the latest version of the Git installer.
- Run the downloaded installer and follow the prompts in the installation wizard to complete the installation.
- After installation, you can confirm the successful installation by using the `git version` command in the command line.

### Step 1: Fork the Project

- First, you need to fork this project. Go to the [py-vchart project page](https://github.com/VisActor/py-vchart) and click the Fork button in the top right corner.

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/fork.PNG)

- A project named xxxx(your GitHub username)/py-vchart will appear in your GitHub account.
- Use the following command on your local computer to create a py-vchart folder:

```
// ssh
git clone git@github.com:xxxx(你的github用户名)/py-vchart.git

// https
git clone https://github.com/xxxx(你的github用户名)/py-vchart.git
```

### Step 2: Get the Project Code

- Enter the py-vchart folder and add the remote address of py-vchart.

```
git remote add upstream https://github.com/VisActor/py-vchart.git
```

- Fetch the latest source code of py-vchart.

```
git pull upstream develop
```


### Step 3: Create a Branch

- Now, you can start contributing your code. The default branch of py-vchart is the develop branch. Whether it's for feature development, bug fixing, or documentation writing, please create a new branch and then merge it into the develop branch. Use the following commands to create a branch:

```
// Create a feature development branch
git checkout -b feat/xxxx

// Create a bug fix development branch
git checkout -b fix/xxxx

// Create a documentation or demo branch
git checkout -b docs/add-funnel-demo
```


Suppose we've created a documentation modification branch named `docs/add-funnel-demo`.

- Now, you can make changes to the code on this branch.
- Assume you've added some code and are ready to commit it to the repository. Use the command `git commit -a -m "docs: add custom funnel demo and related docs"`. VisActor's commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

  - `<type>[optional scope]: <description>`
  - Common `type` values include docs (documentation and log modifications), feat (new features), fix (bug fixes), refactor (code refactoring), etc. Please choose according to the actual situation.
  - Please write a brief and precise English description for the `description`.

### Step 4: Merge Changes

- A common issue is that the remote upstream (@visactor/py-vchart) has new updates, which may cause conflicts when you submit a Pull Request. Therefore, you can merge the commits from other remote developers with your own commits before submitting. Use the following command to switch to the develop branch:

```
git checkout develop
```


- Use the following command to pull the latest code from the remote:

```
git pull upstream develop
```

- Switch back to your development branch:

```
git checkout docs/add-funnel-demo
```

- Merge the commits from the develop branch into your own branch:

```
git rebase develop
```

- Push the updated code to your own branch:

```
git push origin docs/add-funnel-demo
```


### Step 5: Submit a Pull Request

You can click the `Compare & pull request` button on your GitHub repository page.

![](https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR.png)

Or create a pull request through the `contribute` button:

<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/create-PR-2.png">
</div>

Fill in the modification details for this submission according to the template:

- Select the type of modification.
<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-checklist.png">
</div>

- Fill in the related issue.
<div align='center'>
<img style="width:200px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/related-issue.png">
</div>

- If there are complex changes, please explain the background and solution.
<div align='center'>
<img style="height:120px" src="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/VChart/contribution-guide/issue-background.png">
</div>

After filling in the relevant information, click `Create pull request` to submit.

## Easily Step into the py-vchart Open-Source Contribution Journey

"**good first issue**" is a common label in the open-source community. The purpose of this label is to help new contributors find suitable entry-level issues.

You can view the entry-level issues for py-vchart through the [issue list](https://github.com/VisActor/py-vchart/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22). Currently, there are two types:

- Demo case production
- Simple feature development

If you **have the time and willingness** to participate in community contributions, you can take a look at the **good first issue** in the issue list and choose one that interests you and suits you.

We believe you're a person who sees things through. So, after you understand and decide to claim an issue, please leave a message under the issue to inform everyone.

### Demo Task Development Guide

To be supplemented...

## Embrace the VisActor Community

While you're contributing code to VisActor, we encourage you to participate in other activities that will make the community more prosperous, such as:

1. Providing suggestions for the project's development, feature planning, etc.
2. Creating articles, videos, and hosting lectures to promote VisActor.
3. Writing promotion plans and executing them with the team.

VisActor is also working hard to help students participating in community building grow together. We plan (but are not limited to, and look forward to more suggestions from everyone) to provide the following assistance:

1. Data visualization R & D training based on VisActor to help participating students grow rapidly in programming skills, visualization theory, architecture design, and other aspects.
2. Regularly awarding the "Code Contribution Award" and the "Community Promotion Award".
3. Organizing community members to participate in open-source activities.

## Frequently Asked Questions

To be supplemented...
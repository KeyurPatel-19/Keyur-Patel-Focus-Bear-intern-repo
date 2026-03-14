# Git Concepts: Staging vs. Committing

## Write a summary in git_understanding.md:

### What is the difference between staging and committing?

In Git, staging and committing are two separate steps used to save changes in a project.

Staging means preparing specific changes that you want to include in the next commit. When you stage a file using git add, Git moves those changes into the staging area, which acts like a temporary space where you select what will be included in the next snapshot of your project.

Committing means permanently saving the staged changes into the Git repository. When you run git commit, Git records those staged changes along with a commit message that explains what was modified.

In simple terms, staging selects the changes, and committing saves them to the project history.

### Why does Git separate these two steps?

Git separates staging and committing to give developers more control over what gets saved in each commit. Sometimes a developer may change several files but only want to save certain changes at a time. The staging area allows you to carefully choose which modifications should be included in a commit.

This helps keep commits clean, organized, and meaningful, which is important when working in teams or when reviewing project history later.

### When would you want to stage changes without committing?

There are several situations where staging changes without committing can be useful. For example, if you modify multiple files but only want to commit some of them first, you can stage only the relevant files while leaving others unstaged.

It is also helpful when reviewing changes before saving them. By staging files and checking git status, you can confirm exactly what will be included in the next commit. If something is staged by mistake, it can easily be unstaged before committing.

This process helps ensure that commits remain clear, accurate, and well-structured.

## Branching & Team Collaboration

Branches help developers work on changes safely without affecting the main version of the project.

## Branching & Team Collaboration Reflection

### Why is pushing directly to main problematic?
Pushing directly to main is risky because it can affect the stable version of the project immediately. If the code has a mistake, bug, or incomplete work, it can create problems for the whole team. It also makes collaboration harder because important changes go live without proper checking.

### How do branches help with reviewing code?
Branches give developers a safe space to work on their own changes without disturbing the main project. Once the work is ready, it can be reviewed before merging. This makes it easier to catch mistakes, improve code quality, and discuss changes with the team.

### What happens if two people edit the same file on different branches?
If two people edit the same part of the same file on different branches, Git may create a merge conflict when the branches are merged. This means Git cannot decide which change should be kept automatically, so the conflict must be resolved manually.
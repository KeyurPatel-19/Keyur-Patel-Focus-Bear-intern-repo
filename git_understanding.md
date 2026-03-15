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

## Cherry-pick test
This line was added on the cherry-pick-test branch.

## Advanced Git Commands & Reflection

## What does each command do?
### git checkout main -- <file>
This command restores a specific file from the main branch without changing the rest of the branch. I would use it when I accidentally edit one file and want to bring back the clean version from main without losing my other work.

### git cherry-pick <commit>
This command applies one specific commit from another branch onto the current branch. I would use it in a real project when I only need one useful fix or feature from another branch and do not want to merge everything from that branch.

### git log
This command shows the commit history of the repository. I would use it to understand what changes were made over time, who made them, and to find commit IDs for other Git operations.

### git blame <file>
This command shows who last modified each line in a file and when. I would use it in a real project when I want to understand why a certain line was changed or find the right person to ask about that code.

## When would you use it in a real project (hint: these are all really important in long running projects with multiple developers)?

In a real project, I would use these commands to safely manage changes, track project history, restore files, and bring in only the exact fixes I need without disturbing other team members’ work.

## What surprised me while testing these commands?
What surprised me was how powerful Git is for handling specific changes without affecting the whole project. I found cherry-pick especially interesting because it lets me move only one commit instead of merging an entire branch. I also found git blame useful because it gives clear history at the line level, which can be very helpful in team projects.


## Debugging with git bisect

### What does git bisect do?
git bisect helps find the exact commit that introduced a bug by using binary search. Instead of checking every commit manually, Git checks commits in between a known good commit and a bad commit until it identifies the first bad one.

### When would you use it in a real-world debugging situation?
I would use git bisect when a project suddenly starts failing, but I do not know which commit caused the issue. It is especially useful in projects with many commits and multiple developers because it saves time and makes debugging more systematic.

### How does it compare to manually reviewing commits?
git bisect is much faster and more efficient than manually reviewing commits one by one. Manual checking can take a long time and is easy to get confused with, while git bisect narrows the problem down quickly and gives a more reliable result.


# Writing Meaningful Commit Messages

## Best practices
- Keep the message clear and specific.
- Describe what changed.
- Use imperative tone, such as "Add", "Fix", or "Update".
- Keep the first line short and readable.
- Avoid vague messages like "fixed stuff".

## Commit style test 1
Testing a vague commit message.

## Commit style test 2
Testing an overly detailed commit message.

## Reflection

### What makes a good commit message?
A good commit message is short, clear, and specific. It should explain what changed in a way that is easy for others to understand later.

### How does a clear commit message help in team collaboration?
A clear commit message helps team members quickly understand changes without opening every file. It makes reviews, debugging, and project history easier to follow.

### How can poor commit messages cause issues later?
Poor commit messages make it hard to understand why a change was made. This can slow down debugging, confuse teammates, and make project history less useful.


## Pull Request Practice

I created a new branch and practiced creating a pull request to understand how developers collaborate and review code changes in GitHub.
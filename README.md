## Part 1: Our Project

### What program will we build?
We're building a study planner for students. You enter your classes, assignments, and exam dates (or paste in your syllabus), and it makes a day-by-day study schedule that works backward from your deadlines. It also warns you when a week is going to be overloaded.

### Why is it useful or interesting?
Most students have 4–5 classes, each with its own syllabus and deadlines, and it's easy to miss that three big things are due the same week until it's too late. Our program puts everything in one place, spots crunch weeks ahead of time, and turns "I have a lot due" into an actual plan for each day. 

### Why will it take two weeks?
An LLM can get us a basic version (a form and a list of tasks) pretty quickly, but making it actually good takes much longer. After the prototype we plan to:
- Add syllabus import that pulls due dates out of real, messy syllabus text
- Make the scheduling smarter so it spreads work out instead of cramming it before deadlines
- Handle edge cases like overlapping deadlines and impossible workloads
- Let the schedule adjust when you miss a study session
- Add a calendar view and export to Google Calendar
- Save data so it's there when you come back
- Test it with our real class schedules and fix bugs

### How will we demo it in class?
We'll paste in a real syllabus and show the dates it finds, add a second class, and show the study plan it makes.

## Part 2

1. Forking makes your own copy of someones repo on github. Cloning downloads a repo onto your computer.

2. A feature branch is a separate line of work where you build one feature or change without touching the main branch.

3. A pull request shows whats has been changed
4. Someone reviews is or leaves comments to fix things if needed.

5. Fork: You already forked your partner's repo on GitHub, so you have your own copy online.
Clone: Download your fork to your computer.
Branch: Create a feature branch and switch onto it.
Create the file: Make foo.md in the project folder.
Stage: Mark foo.md to be included in the next commit.
Commit: Save the change as a snapshot with a message.
Push: Upload the feature branch to your fork on GitHub.
Pull request: On GitHub, open a PR from your fork's branch to your partner's main branch.
Review and merge: Your partner reviews the PR and merges it, which accepts the change into their repo.

6. git clone <your-fork-URL>
cd <repo-name>
git checkout -b add-foo
touch foo.md
git add foo.md
git commit -m "Add foo.md"
git push origin add-foo

7. git add is like th waiting room for the changes
   git commit puts them in permanant

8. gitignore file is a list of files that Git should ignore. Anything on that list never gets saved to your repo or uploaded to GitHub.

You use it to keep out things that shouldn't be shared, like passwords, API keys, and junk files your computer creates automatically

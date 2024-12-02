# How to run the project after installing everything
This is for **very beginners** like me 😊  

Experienced members helped me build the environment and set everything up. Following are the steps after that. Please correct me if anything is wrong!

## Tools
- Docker: Run applications in an isolated environment
- ChromaDB: The database to keep your data
- FastAPI: A main tool to support building your application
- Postman: API platform
- Visual Studio Code: Write your code here
- GitHub: Manage your code here
- Ruff and Black: check and format your code

## Steps
### Open tools and terminal windows
Visual Studio Code, Postman, Docker Desktop, three terminal windows
### Build your virtual environment using docker
1. In a terminal window, go to your project's directory (rag directory in our case)
2. `docker compose up --build`
### Keep your files up to date through GitHub
1. In the second terminal window, go to your project's directory (rag directory)
2. `git branch` see what branches are there and check which branch you are in
3. `git switch main` go to the main branch
4. `git pull` keep your files up to date
5. `git branch new-branch-name` make a new branch out of a main branch. You will be working in this branch.
6. `git status` if you want to check your current status
### Run a python file
1. In the third terminal window, go to your project's directory (rag directory)
2. `docker exec -it fastapi sh` start using the virtual environment (container)
3. You see many #s. Don't be surprised 😉
4. `python3 path_to_your_file/your_python_file.py` now you can see your file running! Yay!
### Saving your progress and updating it in GitHub
0. Suppose you made changes to `your_python_file.py`
1. In the second terminal window, where you operated `git` commands,
2. Check and clean your code first by doing: `ruff check your_python_file.py` and `black your_python_file.py`
3. `git add your_python_file.py` to say you want to get this file updated (alternatively, use `git add -u` when you've deleted files. This command adds the difference for you automatically, including the files you deleted.)
4. `git commit -m "describe the changes I made"` to confirm that those you added are the ones you want to update.
5. `git push` to get your updates reflected on GitHub (If they provide a longer command for you to copy-paste, do so.)
6. Go to your GitHub page
7. Once you check the difference, if that is good, proceed to make a pull request
8. If the difference is not okay, make changes to your files and follow steps 2 to 4 again.
9. When making a pull request, assign Assignees, reviewers, and labels.


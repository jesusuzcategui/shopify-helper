from github import Github
from ..database.db import Db
import os
import prompt_toolkit
import termcolor
from rich.table import Table
from rich.console import Console
from ..menu import render

class gitHelper:
    def __init__(self):
        self.username = "jesusktgdev"
        self.token = "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"
        self.email = "jesus.uzcategui@gradiweb.com"
        self.name = "Jesus Uzcategui"
        self.git = Github( self.token )
        self.Db = Db()
        self.Console = Console()

    def setAuthor(self):
        command = "git config user.name " + self.name + " && git config user.email " + self.email;
        os.system(command) 
    
    def showProject(self):
        result = self.Db.list(id=None);
        table = Table(title="Shops registered")
        tableCols = ["ID", "Url", "Path"]
        formatedRows = []

        for col in tableCols:
            table.add_column(col)

        for row in result:
            formatedRows.append([
                str(row[0]),
                row[1],
                row[2]
            ])
        
        for fr in formatedRows:
            table.add_row(*fr, style="bright_green")

        self.Console.print(table)

        termcolor.cprint('Select a project by ID', "green")

        option = int(prompt_toolkit.prompt("Put a ID: "))

        select = option - 1

        record = result[select]

        path = record[2]

        os.chdir(path)

        print("You now are: ", os.getcwd())

        self.submenu()

        
    
    def submenu(self):
        termcolor.cprint('Options', "blue")
        termcolor.cprint('1) Show repositories', "green")

        option = prompt_toolkit.prompt("Put a option: ")
        option = int(option)

        if option == 1:
            self.showRepositories()
    

    def clone(self, repo):

        branches = self.showBranch(repo)

        termcolor.cprint("Select a branch", "blue")

        option = int(prompt_toolkit.prompt("Put a ID: "))

        select = branches[option - 1]
                
        gitUri = repo.clone_url.replace("https://", "")

        uriClone = "https://"+self.username+":"+self.token+"@"+gitUri

        commandClone = "git clone --branch " + select.name + " " + uriClone + " ."

        os.system(commandClone)

        self.setAuthor()

        nameBranch = prompt_toolkit.prompt("Branch name: ")

        if not nameBranch:
            termcolor.cprint("Please put name branch", "warning")
            nameBranch = prompt_toolkit.prompt("Branch name: ")
            
        os.system("git checkout -b " + nameBranch)

        self.menuGit(repo)
    
    def merge(self, repo):
        branches = self.showBranch(repo)

        termcolor.cprint("Select a branch", "blue")

        option = int(prompt_toolkit.prompt("Put a ID: "))

        select = branches[option - 1]

        commandToMerge = "git merge " + select.name;

        os.system(commandToMerge)

        self.menuGit(repo)
    
    def pull(self, repo):
        branches = self.showBranch(repo)

        termcolor.cprint("Select a branch", "blue")

        option = int(prompt_toolkit.prompt("Put a ID: "))

        select = branches[option - 1]

        commandToMerge = "git pull origin " + select.name;

        os.system(commandToMerge)

        self.menuGit(repo)
    

    def showBranch(self, repo):
        titleTable = repo.full_name + " Branch"
        table = Table(title=titleTable)
        tableCols = ["ID", "Branch"]

        branches = repo.get_branches()

        for col in tableCols:
            table.add_column(col)
        
        for index, row in enumerate(branches, start=1):
            fr = [
                str(index),
                row.name
            ]

            table.add_row(*fr, style="bright_green")
        
        
        self.Console.print(table);

        return branches

    
    def showRepositories(self):
        repository = self.git.get_user().get_repos()
        table = Table(title="Repositories")
        tableCols = ["ID", "Repository"]

        for col in tableCols:
            table.add_column(col)
        
        for index, row in enumerate(repository, start=1):
            fr = [
                str(index),
                row.full_name
            ]

            table.add_row(*fr, style="bright_green")
        
        
        self.Console.print(table);

        termcolor.cprint('Select a repository by ID', "green")

        option = int(prompt_toolkit.prompt("Put a ID: "))

        select = option - 1

        repo = repository[select]

        self.menuGit(repo)
    

    def menuGit(self, repo):
        termcolor.cprint("What's next now?", "blue")
        termcolor.cprint('1) Clone', "green")        
        termcolor.cprint('2) Merge', "green")
        termcolor.cprint('3) Pull', "green")
        termcolor.cprint('4) Back to menu', "green")

        option2 = int(prompt_toolkit.prompt("Put a option: "))

        if option2 == 1:
            self.clone(repo)
        elif option2 == 2:
            self.merge(repo)
        elif option2 == 3:
            self.pull(repo)
        else:
            render.render()
    

    def menu(self):
        termcolor.cprint('Wellcome GIT Options', "blue")
        termcolor.cprint('1) Show projects', "green")
        termcolor.cprint('2) Back to menu', "green")

        option = prompt_toolkit.prompt("Put a option: ")
        option = int(option)

        if option == 1:
            termcolor.cprint('All Projects', "blue")
            self.showProject()
        else:
            render.render()

    
    def show(self):

        self.menu()

        """
        repository_only = self.git.get_user().get_repo('TestClientShopify')
        for index, repo in enumerate(repository, start=1):
            option = str(index) + ") " + repo.full_name;
            print(option)

        print("----------------------------------------------------------------");
        print(repository_only);
        print(repository_only.clone_url);

        branchs = repository_only.get_branches()

        for index, branch in enumerate(branchs, start=1):
            print(branch.name, index)
        
        dirc = "C:/Users/uzcat/Workspace/test-cli"
        
        os.chdir(dirc)

        print("You now are: ", os.getcwd())

        numberBranch = int(prompt_toolkit.prompt("Put your branch: "))
        numberBranch = numberBranch - 1

        selectedBranch = branchs[numberBranch]

        gitUri = repository_only.clone_url.replace("https://", "")

        uriClone = "https://jesusktgdev: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@"+gitUri

        commandClone = "git clone --branch " + selectedBranch.name + " " + uriClone + " ."

        print(commandClone);

        os.system(commandClone)
        """
        

        
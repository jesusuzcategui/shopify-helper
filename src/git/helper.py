from github import Github
import os
import prompt_toolkit

class gitHelper:
    def __init__(self):
        self.git = Github("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")
    
    def show(self):
        repository = self.git.get_user().get_repos()
        repository_only = self.git.get_user().get_repo('TestClientShopify')
        #for repo in repository:
           #print(repo.full_name)
        
        print("----------------------------------------------------------------");
        print(repository_only);
        print(repository_only.clone_url);

        branchs = repository_only.get_branches()

        for index, branch in enumerate(branchs, start=1):
            print(branch.name, index)
        
        dirc = "C:/Users/uzcat/Workspace/proyecto-nuevo-cli"
        
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

        

        
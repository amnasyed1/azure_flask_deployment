# azure_flask_deployment


## Guide on How to Set Up and Deploy Your Application

1) Create a flask application on Google Cloud Shell with required files such as app.py, requirements.txt file, .html files with code corresponding to the contents that will be displayed on the application (ex: about.html, base.html, data.html, and random.html)
2) After the completion of creating the files, run the app by typing ```python app.py``` in the terminal, to ensure you are satisfied with the functionality and aesthetics of the app
3) To start the process of deploying your application, you need to install Azure CLI, in the terminal on Cloud Shell, input this command ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash ``` and hit enter
4) After that, type ```az``` in the terminal and hit enter, this will test that azure was installed
5) Then type ```az login --use-device-code``` to login, once you hit enter it will provide you with a link and your unique authentication code. Click the link, sign in with your email, and provide the authentication code that was presented in the terminal. 
6) Go back into the terminal on Cloud Shell and redeem your azure student subscription ID by the command ```az account list --output table ``` and hit enter. You will see a table in the terminal with a few categories, next to "Azure for Students", find your specific "SubscriptionId", everyone has their own unique subscription ID that is linked to only your account. 
7) To change into the subscription id, use the command ```az account set --subscription <type your subscriptionid that you obtained above> ``` 
8) Next, go into the Azure web portal, in the search bar type "resource groups" to create a new resource group. When creating a new resource group, make sure under "Project details" the subscription is 'Azure for Students'; in addition, when choosing a name make sure it's a unique name, there are no special characters , or white spaces.
9) Go back to Cloud Shell, in the terminal type the command, ```az webapp --resource-group <groupname> --name <app-name> --runtime <PYTHON : 3.9 > --sku <B1> ```
10) Make sure you are in the right directory, for instance, the directory I worked from was "azure_flask_deployment", if you are not in the right directory, type 'cd' followed by 'the desired directory name/' and hit enter. 
11) Then to push the updates, (deploy the app) type ```az webapp up```
12) Ensure all your updates are backed up by pushing your work from your Cloud Shell into GitHub, by utilizing the commands ```git add . ``` then ```git commit -m 'type a brief description of what you did' ``` and then lastly ```git push```


## Deployed URL of my flask application
https://amna-504-flask.azurewebsites.net/ 

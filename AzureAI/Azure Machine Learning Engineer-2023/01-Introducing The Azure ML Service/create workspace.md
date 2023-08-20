
The ML extension need Azure CLI > 2.15.0
```
az version

# remove old ML extension
az extension remove -n azure-cli-ml
az extension remove -n ml

# install new ML extension
az extension add -n ml -y

az login
az account set --subscription xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx


# create resource group
az group create --name aml-dev-rg  --location eastus2

# create workspace
az ml workspace create -n aml-ws -g aml-dev-rg -l eastus2
```


## Creating an AMLS workspace with ARM templates

```
az group create --name rg_name --location eastus2

az deployment group create 
    --name "exampledeployment" 
    --resource-group "rg_name" 
    --template-file "azuredeploy.json" 
    --parameters name="uniquename" 
    environment="dev" 
    location="eastus2"
```

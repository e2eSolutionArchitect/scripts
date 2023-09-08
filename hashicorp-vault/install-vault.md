# Install HashiCorp Vault

Please refer: https://www.hashicorp.com/official-packaging-guide

```
sudo apt update && sudo apt install gpg -y

## Add hashicorp GPG key
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

## Verify finger print
gpg --no-default-keyring --keyring /usr/share/keyrings

## Hashicorp Repo
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update && sudo apt install vault -y 


vault -version

```

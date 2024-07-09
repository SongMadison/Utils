# install a new git compatible with GCM
sudo apt-get install software-properties-common -y 
add-apt-repository ppa:git-core/ppa
apt update; apt install git -y

# install Credential management
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.5.0/gcm-linux_amd64.2.5.0.deb
sudo dpkg -i gcm-linux_amd64.2.5.0.deb
git-credential-manager configure

git config --global credential.azreposCredentialType oauth
git config --global credential.msauthFlow devicecode
git config --global user.name "Song Wang"
git config --global user.email "sonwang@microsoft.com"
cat ~/.gitconfig

# git
# warning: cannot persist Microsoft authentication token cache securely!
# warning: using plain-text fallback token cache
# git clone "https"

git clone https://msazure.visualstudio.com/DefaultCollection/Cognitive%20Services/_git/Language-Research

git clone https://msazure.visualstudio.com/DefaultCollection/Cognitive%20Services/_git/Language-Summarization

git clone https://msazure.visualstudio.com/DefaultCollection/Cognitive%20Services/_git/Language-ZCodePlusPlus

# enable PEP 660 support
pip3 install --upgrade pip  
git clone https://github.com/lm-sys/FastChat.git && cd FastChat && pip install -e ".[model_worker,webui]" && cd ..
pip3 install datasets flash-attn 
# [WARNING] - `flash-attention` package not found, consider installing for better performance: No module named 'flash_attn'.
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs


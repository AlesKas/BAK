if [ -x "$(command -v docker)" ]; then
    echo "Docker already installed."
else
    echo "Installing docker"
    curl -fsSL get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
fi
echo "Installing docker-compose"
pip3 install docker-compose

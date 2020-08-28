Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", :privileged => false, inline: <<-SHELL
    sudo apt-get update
	
	# Install pyenv prerequisites
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
	
	# Install pyenv
    git clone https://github.com/pyenv/pyenv.git /home/vagrant/.pyenv
	
	# Define environment variable PYENV_ROOT to point to the path where pyenv repo is cloned and add $PYENV_ROOT/bin to your $PATH for access to the pyenv command-line utility
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /home/vagrant/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vagrant/.profile
    
	# Add pyenv init to your shell to enable shims and autocompletion
	echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> /home/vagrant/.profile
    
	# Restart your shell so the path changes take effect. You can now begin using pyenv.
	exec "$SHELL"
  SHELL
  
  config.vm.provision "shell", :privileged => false, inline: <<-SHELL
    # Use pyenv to install a custom Python version
	pyenv install 3.8.5
	
	# Use pyenv global <version> to make your new Python version the default one
    pyenv global 3.8.5
    
	# Download and install poetry 
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
  SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privileged: false, inline: "
    cd /vagrant
    poetry install
    nohup poetry run flask run --host 0.0.0.0 > applogs.txt 2>&1 &
    "}
  end

  config.vm.network "forwarded_port", guest: 5000, host: 5000
end
"""
using homebrew
--------------
brew install pyenv
pyenv install 3.8.0

enable in shell ~/.bash_profile or ~/.zshrc
-------------------------------------------
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# check versions and set global
-------------------------------
pyenv versions
pyenv global 3.8.0
python --version
"""
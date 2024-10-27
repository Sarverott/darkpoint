

# python check
if ! command -v python 2>&1 >/dev/null
then
    echo "PYTHON 3 could not be found"
    echo "installing python..."
    sudo apt install python3 -y
fi
# pip check
if ! command -v pip 2>&1 >/dev/null
then
    echo "python's PIP could not be found"
    echo "installing pip..."
    sudo apt install python3-pip -y
fi

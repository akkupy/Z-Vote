#!/bin/bash


function error {
  echo -e "\\e[91m$1\\e[39m"
  exit 1
}


echo "Cloning The Project..."
sudo git clone -b production https://github.com/akkupy/Z-Vote.git || error "Failed Clone the project!"
cd Z-Vote || error "Failed to Change Directory!"
echo "Done !"
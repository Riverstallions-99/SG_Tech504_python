#!/bin/bash

# Script to deploy an AppImage into a lovely, logo'd app shortcut
# Pre-requisits:
# Must be deployed in ~/Applications/
# AppImage file is presumed to be in ~/Downloads/
# AppImage file is presumed to be in the format: $1.AppImage
# App "logo" to use is also presumed to be in ~/Downloads/
# App "logo" is presumed to be in the format: $2-logo.png

# -------------------------------------------------------
# Usage: ./deploy-AppImage.sh <app-image-file> <app-name>
if [ $# -lt 1 ]
then
  echo "Usage: $0 file app-name"
  exit 1
fi
# -------------------------------------------------------

echo "Move AppImage into app folder in Applications directory"
mkdir $2
mv ../Downloads/$1 $2
echo "Move AppImage logo into app folder in App directory"
mv ../Downloads/$2-logo.png $2

# Make file <app-name>.desktop in local applications directory
cat > ~/.local/share/applications/$2.desktop << EOF
[Desktop Entry]
Name=$2
Exec=/home/becky/Applications/$2/$1
Icon=/home/becky/Applications/$2/$2-logo.png
Type=Application
StartupNotify=true
Terminal=false
EOF

chmod +x ~/Applications/$2/$1



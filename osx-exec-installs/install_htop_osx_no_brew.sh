## setup _________________________________

HTOP_VER=2.2.0
TEMP_COMPILE=htop-temp-compile
COMMON_INSTALL_PREFIX=/opt
SYMLINK=/usr/local/bin/htop

## _______________________________________

echo
echo ">>> Creating and using temporary dir ${TEMP_COMPILE} for downloading and compiling htop ..."
echo

mkdir ${TEMP_COMPILE}
cd ${TEMP_COMPILE}

echo
echo ">>> Downloading the releases ..."
echo

curl -OL http://hisham.hm/htop/releases/${HTOP_VER}/htop-${HTOP_VER}.tar.gz

echo
echo ">>> Extracting tmux ${HTOP_VER} ..."
echo

tar xzf htop-${HTOP_VER}.tar.gz

echo
echo ">>> Compiling htop ..."
echo

cd htop-${HTOP_VER}
./configure && make
echo
echo ">>> Installing htop in ${COMMON_INSTALL_PREFIX}/bin ..."
echo

sudo make install

echo
echo ">>> Symlink to it from ${SYMLINK} ..."
sudo ln -s ${COMMON_INSTALL_PREFIX}/bin/htop ${SYMLINK}

echo
echo ">>> Cleaning up by removing the temporary dir ${TEMP_COMPILE} ..."
echo

cd ..
sudo rm -rf ${TEMP_COMPILE}

sudo apt-get -y install git cmake build-essential libusb-1.0 libpulse-dev libx11-dev libxext-dev libxi-dev x11proto-input-dev
sudo apt-get install cmake pkg-config libmp3lame-dev libshout3-dev libconfig++-dev libconfig-dev -y

sudo apt-get install pulseaudio

cd ~/Downloads/
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash

# Fetch and compile rtl-sdr source
cd ~/Downloads/
git clone git://git.osmocom.org/rtl-sdr.git
cd rtl-sdr && mkdir build && cd build
cmake ../ -DINSTALL_UDEV_RULES=ON
make
sudo make install
sudo ldconfig

Blacklist The Following:

sudo nano /etc/modprobe.d/blacklist-rtl.conf

Copy and paste the following 3 lines

blacklist dvb_usb_rtl28xxu
blacklist rtl2832
blacklist rtl2830

# Fetch and compile multimonNG    
cd ~/Downloads/
sudo git clone https://github.com/EliasOenal/multimonNG.git
cd multimonNG && sudo mkdir build && cd build
sudo cmake ..
sudo make install
sudo ldconfig




instaling RTL-AIR with FM demodulator  (https://github.com/szpajder/RTLSDR-Airband) look for latest release and adapt numbers)
sudo apt-get install libfftw3-dev
apt-get install librtlsdr-dev

cd ~/Downloads/
wget -O RTLSDR-Airband-4.0.3.tar.gz https://github.com/szpajder/RTLSDR-Airband/archive/v4.0.3.tar.gz
tar xvfz RTLSDR-Airband-4.0.3.tar.gz
cd RTLSDR-Airband-4.0.3
mkdir build && cd build
cmake -DPLATFORM=armv8-generic -DNFM=ON -DPULSEAUDIO=ON -DMIRISDR=OFF -DSOAPYSDR=OFF ../
make
sudo make install

make file air.py and paste
#!/usr/bin/python

import subprocess
x = subprocess.run(['sudo /usr/local/bin/rtl_airband -f -c /usr/local/etc/rtl_airband_dl.conf'], shell=True)
print(x)
print(x.args)
print(x.returncode)
print(x.stdout)
print(x.stderr)

sudo chmod +x air.py

right click on the desktop and create new file with “desktop” extension, e.g. MyApp.desktop.
Once you’ve created the file, open it in text editor and add the following content

[Desktop Entry]
Name=RTL_Air (dl)
Comment=Scanner DL
Icon=/usr/share/pixmaps/openbox.xpm
Exec=/usr/bin/python /home/pi/Desktop/air.py
Type=Application
Encoding=UTF-8
StartUpNotify=true
Terminal=true

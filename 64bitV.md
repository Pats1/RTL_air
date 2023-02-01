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

#test 
rtl_test -t
rtl_fm -M wbfm -f 89.0M | play -r 32k -t raw -e s -b 16 -c 1 -V1 -
rtl_fm -f 89.0M -M fm -s 170k -A fast -r 32k -l 0 -E deemp | play -r 32k ...
rtl_fm -M fm -f 154.42M -f 154.75M -f 154.89M -s 12k -g 50 -l 70 | play -r 12k -t raw -e s -b 16 -c 1 -V1 -
rtl_fm -M am -f 118M:137M:25k -s 12k -g 50 -l 280 | play -r 12k -t raw -e s -b 16 -c 1 -V1 -

rtl_fm -f 169.625M -s 22050 | multimon-ng -t raw -a POCSAG2400 -e -n -f alpha --timestamp /dev/stdin



rtl_test -t
rtl_fm -f 169.625M -s 22050 | multimon-ng -t raw -a POCSAG2400 -n -e -f auto -b 0 -C BE --timestamp /dev/stdin
rtl_fm -f 169.625M -s 22050 | multimon-ng -t raw -a POCSAG2400 -e -n --timestamp /dev/stdin
rtl_fm -f 169.625M -s 22050 | multimon-ng -t raw -e -a POCSAG2400 -f alpha /dev/stdin > /var/www/pager/Pager.txt | tail -f /var/www/pager/Pager.txt
run in dir where multimon & rtl is 
./rtl_fm -f 169.625M -s 22050 -g 48 - | ./multimon-ng -a POCSAG2400 -A -t raw -
./rtl_fm -f 169.625M -s 22050 | ./multimon-ng -a POCSAG2400 -t raw - > pagers.txt

rtl_fm -f 169.625M -s 22050 | multimon-ng -t raw -e -a POCSAG2400 -f alpha /dev/stdin > /var/www/pager/Pager.txt | tail -f /var/www/pager/Pager.txt

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

https://github.com/charlie-foxtrot/RTLSDR-Airband
sudo nano /usr/local/etc/rtl_airband.conf
Paste In The Following, Starting With devices:
Remember To Update The Password For Icecast2:

this works
devices:
({
  type = "rtlsdr";
  index = 0;
  gain = 39.0;
  mode = "scan";
  sample_rate = 2.4;
  buffers = 10;
  correction = 0;
  serial = "00000001";
  channels: (
    {
      squelch_threshold = -25;
      freqs = ( 424888000, 424890000, 424710000, 424750000, 424925000, 424950000, 424960500, 424962500);
      modulations = ( "nfm", "nfm", "nfm", "nfm", "nfm", "nfm", "nfm", "nfm");
      labels = ( "dl1", "dl2", "dl3", "dl4", "dl5", "dl6", "dl7", "dl8");
      outputs: (
  {
    type = "icecast";
    server = "192.168.1.35";
    port = 8000;
    mountpoint = "dl.mp3";
    name = "DL scanner";
    username = "source";
    password = "VH@leenek";
    description = "Pats SDR DL";
    genre = "SDR trafic"
 }
);
    }
  );
});

devices:
({
type = "rtlsdr";
index = 0;    #RTL-SDR Number
gain = 30;    #Gain Setting
correction = 0;
mode = "scan";
channels:
(
{
freqs = ( 118.25, 118.6 );        #Add Freq's Here
#labels = ( "Tower A", "Tower B", "Tower Control"); #Label Update
outputs: (
  {
    type = "icecast";
    server = "192.168.1.35";
    port = 8000;
    mountpoint = "dl.mp3";
    name = "DL scanner";
    username = "source";
    password = "VH@leenek";
    send_scan_freq_tags = true;
 }
);
}
);
}
);
Start RTL_AirBand In Terminal:

sudo rtl_airband -f

rtl_airband -f -c /home/pats/Downloads/RTLSDR-Airband-4.0.3/config/delijn.conf


Open Up A Browser To Listen And Use The IP Of The Pi With 192.168.1.35:8000/stream.mp3


rtl_tcp -d 1 -p 2200 -a 192.168.1.35       "Remember To Change The IP To Match The Pi"
rtl_tcp -d 1 -p 2201 -a 192.168.1.35


sudo apt install rtl-sdr
sudo rtl_eeprom -d 2 - s 00000002 -d is divice index - s is new serial
after replug check sudo rtl_eeprom -d 2


cd ~/Downloads/
mkdir patssdr
cd patssdr

wget -O server1.py https://github.com/Pats1/RTL_air/blob/main/server1.py
sudo chmod +x server1.py
wget -O server1.png https://github.com/Pats1/RTL_air/blob/main/server1.png
wget -O server2.png https://github.com/Pats1/RTL_air/blob/main/server2.png
cd /home/pats/Desktop
wget -O SDR_TCP_SERVER_1.desktop https://github.com/Pats1/RTL_air/blob/main/SDR_TCP_SERVER_1.desktop
server2.png


wget https://github.com/x20mar/darkice-with-mp3-for-raspberry-pi/blob/master/darkice_1.0.1-999~mp3+1_armhf.deb?raw=true
mv darkice_1.0.1-999~mp3+1_armhf.deb?raw=true darkice_1.0.1-999~mp3+1_armhf.deb
sudo apt-get install libmp3lame0 libtwolame0
sudo dpkg -i darkice_1.0.1-999~mp3+1_armhf.deb
sudo apt-get install icecast2

https://circuitdigest.com/microcontroller-projects/raspberry-pi-internet-radio-and-streaming-station

ICECAST


sudo cp /etc/icecast2/icecast.xml /etc/icecast2/icecast.xml.backup
sudo nano /etc/icecast2/icecast.xml
<sources> ==> 3 
<burst-size> ==> 12288
<burst-on-connect> ==> 0
<source-password> ==> VH@....
<relay-password> ==> VH@...
Add following code before final “</icecast>” row:

    <mount type="normal">
        <mount-name>/example.ogg</mount-name>
        <username>pats</username>
        <password>VH@leenek</password>
        <max-listeners>3</max-listeners>
        <dump-file>/tmp/dump-example.ogg</dump-file>
        <burst-size>65536</burst-size>
        <hidden>1</hidden>
        <public>1</public>
        <on-connect>/home/icecast/bin/stream-start</on-connect>
        <on-disconnect>/home/icecast/bin/stream-stop</on-disconnect>
    </mount>
    
Close and save your file. Restart icecast to make changes running:

sudo systemctl restart icecast2.service
You can also check if new configuration file worked with Status command:

sudo systemctl status icecast2.service
  
  https://peppe8o.com/open-source-web-radio-with-icecast-and-raspberry-pi/
  
  OPENWEBRX
  All commands must be run as root. If you're using sudo, please use sudo su - before executing the commands below.
  wget -O - https://repo.openwebrx.de/debian/key.gpg.txt | gpg --dearmor -o /usr/share/keyrings/openwebrx.gpg
echo "deb [signed-by=/usr/share/keyrings/openwebrx.gpg] https://repo.openwebrx.de/debian/ bullseye main" > /etc/apt/sources.list.d/openwebrx.list
apt-get update
apt-get install openwebrx
  
sudo systemctl enable openwebrx enables automatic startup of the receiver at boot
sudo systemctl disable openwebrx disables it again
sudo systemctl start openwebrx starts the service manually
sudo systemctl stop openwebrx stops the service manually
sudo systemctl restart openwebrx restarts the service. This is very useful after changing configuration.
  http://192.168.1.35:8073/

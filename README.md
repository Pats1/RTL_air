# RTL_air setup and configure RTL_air for AM and FM
https://github.com/szpajder/RTLSDR-Airband/wiki

	sudo apt install libconfig-dev
	sudo apt-get install build-essential cmake pkg-config libmp3lame-dev libshout3-dev libconfig++-dev

## wget -O RTLSDR-Airband-4.0.2.tar.gz https://github.com/szpajder/RTLSDR-Airband/archive/v4.0.3.tar.gz
## tar xvfz RTLSDR-Airband-4.0.3.tar.gz
## cd RTLSDR-Airband-4.0.3
Let's Make A Build Dir And cd Into: 

mkdir build && cd build
cmake -DPLATFORM=armv8-generic -DSOAPYSDR=ON -DNFM=ON -DPULSEAUDIO=ON ../          pi4
cmake -DPLATFORM=native -DSOAPYSDR=ON -DNFM=ON -DPULSEAUDIO=ON ../                 laptop
cmake ../
make
sudo make install


sudo nano /usr/local/etc/rtl_airband.conf (or below) // template

sudo cp /usr/local/etc/rtl_airband.conf /usr/local/etc/rtl_airband_dl.conf
sudo nano /usr/local/etc/rtl_airband_dl.conf
sudo /usr/local/bin/rtl_airband -f -c /usr/local/etc/rtl_airband_dl.conf

sudo cp /usr/local/etc/rtl_airband.conf /usr/local/etc/rtl_airband_air.conf
sudo nano /usr/local/etc/rtl_airband_air.conf
sudo /usr/local/bin/rtl_airband -f -c /usr/local/etc/rtl_airband_air.conf



devices = ( { type = "rtlsdr"; index = 0; gain = 39; mode = "scan"; sample_rate = 2.4; buffers = 10; correction = 0; channels = ( { squelch_threshold = -30; freqs = (424963000 , 424975000, 424825500 ); modulations = ( "nfm", "nfm", "nfm"); labels = ( "Tower", "S-Approach", "dl"); outputs = ( { disable = false; type = "icecast"; server = "192.168.1.35"; port = 8000; mountpoint = "ATC.mp3"; username = "source"; password = "sdr"; name = "Example scan mode feed"; send_scan_freq_tags = false; description = "Local IceCast Server"; genre = "ATC"; } ); } ); } )


devices:
({
  type = "rtlsdr";
  index = 0;
  gain = 39.0;
  mode = "scan";
  sample_rate = 2.4;
  buffers = 10;correction = 0;
  channels: (
    {
      squelch_threshold = -25;
      freqs = ( 424825500, 424925500, 424750500);
      modulations = ( "nfm", "nfm", "nfm" );
      labels = ( "dl1", "dl2", "dl3");
#     afc = 0;
#     notch = 100.0;
#     notch_q = 10.0;
#     bandwidth = 8000;
      outputs: (
  {
    type = "pulse";
#   server = "192.168.11.10";
#   sink = ... /* default sink */
#   stream_name = "Utility channels";
#   continuous = false;
  }
);
    }
  );
});



right click on the desktop and create new file with “desktop” extension, e.g. MyApp.desktop.

Once you’ve created the file, open it in text editor and add the following content

[Desktop Entry]
Name=RTL_Air (dl)
Comment=Scanner DL
Icon=/usr/share/pixmaps/openbox.xpm
Exec=/usr/bin/python /home/pi/Desktop/test.py
Type=Application
Encoding=UTF-8
StartUpNotify=true
Terminal=true

#!/usr/bin/python

import subprocess
x = subprocess.run(['sudo /usr/local/bin/rtl_airband -f -c /usr/local/etc/rtl_airband_dl.conf'], shell=True)
print(x)
print(x.args)
print(x.returncode)
print(x.stdout)
print(x.stderr)

sudo chmod +x test.py

import subprocess

with open('list.txt', 'w') as f:
    subprocess.run(['ls','-la'], stdout=f)
   



# RTL_air
setup and configure RTL_air for AM and FM


wget -O RTLSDR-Airband-4.0.2.tar.gz https://github.com/szpajder/RTLSDR-Airband/archive/v4.0.2.tar.gz
tar xvfz RTLSDR-Airband-4.0.2.tar.gz
cd RTLSDR-Airband-4.0.2
Let's Make A Build Dir And cd Into: 

mkdir build
cd build
cmake -DPLATFORM=armv8-generic -DSOAPYSDR=ON -DNFM=ON -DPULSEAUDIO=ON ../
sudo nano /usr/local/etc/rtl_airband.conf

echo Please enter the number of accounts to setup
read loops
clear
echo Please Enter Your License:
read key 
clear
for i in $(seq 1 $loops)
do
cd /etc/systemd/system && printf "[Unit]\nDescription=Rise_Selfbot_${i}\nAfter=syslog.target\nAfter=network.target\n\n[Service]\nType=forking\nUser=root\nWorkingDirectory=/home/Rise_Linux_${i}\nRestart=always\nExecStart=/usr/bin/screen -L -dmS Rise_Selfbot_${i} ./Rise_Selfbot\n\n[Install]\nWantedBy=multi-user.target" > ./Rise_Linux_$i.service && cd /home && wget https://riseselfbot.xyz/we/Rise_Linux.zip && unzip Rise_Linux.zip -d /home/Rise_Linux_$i && mv /home/Rise_Linux_$i/Rise_Linux/* /home/Rise_Linux_$i && rmdir /home/Rise_Linux_$i/Rise_Linux && clear && chmod -R 777 /home/Rise_Linux_$i && rm Rise_Linux.zip && cd /home/Rise_Linux_$i && jq --arg variable "$key" '.license = $variable' license.json > "tmp" && mv "tmp" license.json && clear && echo Please Enter Your Token For Account \#$i: && read tkn && jq --arg variable "$tkn" '.token = $variable' config.json > "tmp" && mv "tmp" config.json && jq '.skip_menu = true' config.json > "tmp" && mv "tmp" config.json && systemctl enable Rise_Linux_$i && service Rise_Linux_$i start && clear
done
echo Rise Is Setup, Enjoy!
echo please run \'reboot\' to finish setup
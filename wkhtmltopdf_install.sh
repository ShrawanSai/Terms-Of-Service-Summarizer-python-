echo -e "\n---- Install WkHtmlToPdf 0.12.1 ----"
sudo wget -P Downloads http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
cd Downloads
sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb
cd /usr/local/bin
sudo cp wkhtmltoimage /usr/bin/wkhtmltoimage
sudo cp wkhtmltopdf /usr/bin/wkhtmltopdf
echo -e "Wkhtmltopdf is installed!"


pip install--proxy http://127.0.0.1:10080

Method 3: Configuring pip Configuration File
You can also configure pip to use a proxy by modifying the pip configuration file.

Locate the pip Configuration File:

The pip configuration file can be located at %APPDATA%\pip\pip.ini on Windows.

Edit or Create pip.ini:

Open the pip.ini file in a text editor. If it doesn't exist, create a new file named pip.ini.

Add Proxy Configuration:

Add the following lines to the pip.ini file:

[global]
proxy = http://username:password@proxyserver:port
Replace http://username:password@proxyserver:port with your proxy details.

Save and Close:

Save the pip.ini file and close the text editor.

example:

If your proxy server is proxy.example.com on port 8080, and it does not require authentication, your commands might look like this:

Command Line Argument:

pip install requests --proxy http://proxy.example.com:8080
Environment Variables:

For Command Prompt:

set HTTP_PROXY=http://proxy.example.com:8080
set HTTPS_PROXY=http://proxy.example.com:8080
For PowerShell:

$env:HTTP_PROXY="http://proxy.example.com:8080"
$env:HTTPS_PROXY="http://proxy.example.com:8080"


pip.ini Configuration:

[global]
proxy = http://proxy.example.com:8080
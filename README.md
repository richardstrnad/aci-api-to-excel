# Create an Excel file from ACI API Data
This project is a simple example that shows how you can get ACI API data and
then put it into Excel.

## Usage
### Create a venv and activate it
This is opinionated, feel free to handle this in another way if you have a preference!
```
python3 -m venv env
source env/bin/activate
```

Then install the requirements
```
pip install -r requirements.txt
```

### ACI Credentials
Define the credentials. I recommend doing this via a .env file. So, just put
the following in a file called .env in the same folder as the script.

If you prefer, you can set these env vars in any other way you like.

```
APIC=10.0.0.1
APIC_USER=admin
APIC_PASSWORD=pw
```

**Important** if you want to use the non default Login Domain, you need to
specify it in the format of `apic#LOGINDOMAIN\\admin`

### Script

Now change the CLASS, FILTER & ATTRIBUTES at the top of the moquery.py script.
Then let it run and enjoy your Excel :)

```
...

CLASS = 'ethpmFcot'
FILTER = 'ne(ethpmFcot.guiCiscoPID,"")'
ATTRIBUTES = ['dn', 'guiCiscoPID', 'guiSN']

...
```

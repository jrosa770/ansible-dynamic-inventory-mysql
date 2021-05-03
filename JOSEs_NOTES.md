# JOSE'S NOTES

> All Python Scripts require Python Version =>3.5

> Clone Repository

```sh
git clone https://github.com/jrosa770/ansible-dynamic-inventory-mysql.git
```

> Add a MySQL User (You can lock the GRANTS further if needed)

```sh
mysql -u root -proot_pass
```

```sql
CREATE USER 'myadmin'@'localhost' IDENTIFIED BY 'My_P@55-@dmin';
CREATE USER 'myadmin'@'%' IDENTIFIED BY 'My_P@55-@dmin';
GRANT ALL ON *.* TO 'myadmin'@'localhost';
GRANT ALL ON *.* TO 'myadmin'@'%';
flush privileges;
```

> Edit `tables.sql` if needed

```sql
-- CREATE DATABASE
--- Change if needed and update mysql.ini
DROP DATABASE IF EXISTS ansible_inventory;

CREATE DATABASE ansible_inventory;

USE ansible_inventory;
```

> Edit `mysql.ini`

```ini
[server]
# host = localhost or IP if remote.
host = localhost
user = myadmin
passwd = My_P@55-@dmin
db = ansible_inventory
port = 3306
```

```sh
# Build and Install Packages
python ansible-dynamic-inventory-mysql/setup.py build
python ansible-dynamic-inventory-mysql/setup.py install

# CD Into Cloned Directory
cd ansible-dynamic-inventory-mysql

# Install Dtabase
mysql -u myadmin -pMy_P@55-@dmin ansible_inventory < tables.sql 

# Add Parent Group
python3 inventoryctl.py group -n cisco -e 1
# Add Child Groups
python3 inventoryctl.py group -n ios -p cisco -v ansible_network_os ios -e 1
python3 inventoryctl.py group -n nxos -p cisco -v ansible_network_os nxos -e 1
python3 inventoryctl.py group -n iosxr -p cisco -v ansible_network_os iosxr -e 1

# Add Hosts
python3 inventoryctl.py host -n rtr0 -H rtr0.example.com -v ansible_host 10.0.255.255 -g iosxr -e 1
python3 inventoryctl.py host -n rtr1 -H rtr1 -v ansible_host 1.1.1.1 -g ios -e 1
python3 inventoryctl.py host -n swt1 -H swt1 -v ansible_host 2.2.2.2 -g nxos -e 1

python3 inventory.py --list

```

> Output from `inventory.py --list`

```json
{
  "_meta": {
    "hostvars": {
      "rtr0.example.com": {
        "ansible_host": "10.0.255.255",
        "inventory_hostname": "rtr0"
      },
      "rtr1": {
        "ansible_host": "1.1.1.1",
        "inventory_hostname": "rtr1"
      },
      "swt1": {
        "ansible_host": "2.2.2.2",
        "inventory_hostname": "swt1"
      }
    }
  },
  "cisco": {
    "children": [
      "ios",
      "nxos",
      "iosxr"
    ]
  },
  "ios": {
    "hosts": [
      "rtr1"
    ],
    "vars": {
      "ansible_network_os": "ios"
    }
  },
  "iosxr": {
    "hosts": [
      "rtr0.example.com"
    ],
    "vars": {
      "ansible_network_os": "iosxr"
    }
  },
  "nxos": {
    "hosts": [
      "swt1"
    ],
    "vars": {
      "ansible_network_os": "nxos"
    }
  }
}
```

>Adding to `ansible.cfg`

```cfg
[defaults]
inventory      = /<local_path>/ansible-dynamic-inventory-mysql/inventory.py
```
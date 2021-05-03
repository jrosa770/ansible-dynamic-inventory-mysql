# JOSE'S NOTES

> All Python Scripts require Python Version =>3.5

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
python ansible-dynamic-inventory-mysql/setup.py build
python ansible-dynamic-inventory-mysql/setup.py install

cd ansible-dynamic-inventory-mysql

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
# Ansible Dynamic Inventory for MySQL

This is a [Dynamic Inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html) for [Ansible](https://github.com/ansible/ansible) to be used together with MySQL.

It was written because we maintain a lot of servers and static inventory files did not meet our demand, and we like MySQL.

## Usage
### Work with ansible and ansible-playbook
Simply call the script like the following

```
ansible-playbook -i inventory.py
# or
ansible -i inventory.py
```

Limitations also work

```
ansible-playbook -i inventory.py --limit foo.bar.com
ansible-playbook -i inventory.py --limit groupFoo
```

### Manager inventory Database 
#### Add host
Add a new host 
- -H: set host dns `my.host.domain`, can also set ip address
- [-g]: set group name is `my`, otherwise host will add to group called `ungrouped` 
- [-v key val]: 2 sets of variables { var0:val0, var1:val1 }
- See details: `python inventoryctl.py host -h` 
```
$ python inventoryctl.py host -H my.host.domain -g my -v var0 val0 -v var1 val1
Command: host
{'enabled': 1, 'variables': None, 'id': 1, 'name': 'my'}
```

#### Update host 
- -H: which host will be update
- -U: enter update mode, otherwise only view the host
- See details: `python inventoryctl.py host -h` 
```
$ python inventoryctl.py host -H my.host.domain -U -v var2 val2
Command: host
Update mode
set variables to {"var1": "val1", "var0": "val0", "var2": "val2"}
Update my.host.domain affected rows: 1
```

## Setup
I won't explain the process of installing a database or creating the tables, see `tables.sql` for the required MySQL structure.

Once setup rename `mysql.ini.dist` to `mysql.ini` to suit your needs, if you don't want to use caching just put it on 0.

### Groups
In the table `group` you create the groups you need and their variables,

### Hosts
In the table `host` under `host` you place the IP/DNS for the system.

#### Facts
Under `hostname` you can fill in a value, this will be presented as a variable `inventory_hostname` during the play.
You can modify the name of this Fact variable by changing the `facts_hostname_var` variable in my `mysql.ini`.

### Relation between Hosts and Groups
The table `hostgroups` maps the relation between `host` and `group` using two `FOREIGN KEYS`.

#### Children
Groups can have other groups as children, use the table `childgroups`.

### Note on Variables
This applies to `host` and `group` respectively.
If no variables are needed either NULL it (actual MySQL `NULL` not the `string`) or use `{}`.


## LICENSE

As it was fork from [productsupcom/ansible-dyninv-mysql](https://github.com/productsupcom/ansible-dyninv-mysql),
the same license, the GPL-3 applies.


The [GPL-3](http://www.gnu.org/licenses/gpl-3.0.en.html) can be found under the link.

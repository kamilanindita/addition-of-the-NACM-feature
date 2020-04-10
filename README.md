<h1 align="center">Addition of the NACM feature</h1>

Addition Fitur NACM:
- **Routing Static IPv6**: For Mikrotik device
- **Routing OSPFv3**: For Mikrotik device
- **Monitoring Resource NACM Server**: For Linux Server

___


# Instalasi
## Requirement
    python 3.5+
    virtualenv
    
## Quick start
    sudo su
    git clone https://github.com/rhezaaw/new-nacm-production.git
    cd new-nacm-production
    virtualenv -p python3 env
    source env/bin/activate
    pip3 install -r requirements.txt
    cd nacm
    python3 manage.py runserver 0.0.0.0:8000
    akses via browser <ip:8000>
    
___

#### 1. Main Page
![Image of index](https://drive.google.com/uc?export=view&id=1amb9qXStcDtTMD7m5bR4qF641OBTo5vd)

#### 2. Routing
![Image of routing](https://drive.google.com/uc?export=view&id=13R-27aBNIoTrQzTVfyAMYRbrCXbx4SP9)

#### 3. Backup
![Image of backup](https://drive.google.com/uc?export=view&id=1D3I5AnDnBeAHYkGX59mRVp4L7BydjmPa)

#### 4. Restore
![Image of vlan](https://drive.google.com/uc?export=view&id=1zVi9I7bCvJ6f4NUe3ooFPqNfoSLfh3we)

___


## Addition Feature

#### 1. Edit Menu Navigation
Edit file navigation.html (/website/templates/navigation.html)
![Image of index](https://drive.google.com/uc?export=view&id=1MfO2Mq8UG9LxT7MAkJWYdsDWabPc3hl-)

#### 2. Add URL
Edit file urls.py (/website/urls.py)
![Image of Add URL](https://drive.google.com/uc?export=view&id=16TPVqu_gaSze6_0I6OYkT3WDHtC0RCZ3)

#### 3. Import File Configuration
Import new file configuration in __init__.py (website/views/__init__.py)
![Image of Import File Config](https://drive.google.com/uc?export=view&id=1E_a5pogEtCmlXb2rHzdQb_55J8p8JPiQ)

#### 4. Add New File Configuration
Add file routing_conf_ipv6.py (website/views/routing_conf_ipv6.py)
![Image of Add file Config](https://drive.google.com/uc?export=view&id=1j63UEiTBL3JC1D96F6BNeMcqGhgHncM2)

#### 5. Add New Template
Add file routing_dynamic_ipv6.html and routing_static_ipv6.html (website/templates/config/)
![Image of Add template](https://drive.google.com/uc?export=view&id=1ugbXsUDdt3pb8Wp5IkA_-ZKjDdBxm8Wt)

#### 6. Edit ModelForm
Edit file forms.py (website/forms.py)
![Image of Edit ModelForm](https://drive.google.com/uc?export=view&id=1hDxKDxW9exG-kfjgcZI6KVCZ8aMPbPsc)

![Image of Edit ModelForm widget](https://drive.google.com/uc?export=view&id=1-eqxdVBlv2saiVPc_oqkoJqbEX3BcCW9)

#### 7. Migration to Update structure database
![Image of Makemigration](https://drive.google.com/uc?export=view&id=1lp2qtF7j4sxf280Sovx5iEYG8MwX8TXP)

![Image of Migrate](https://drive.google.com/uc?export=view&id=1ZotCMTvLCxgo0s4wJyuYkBubsQR2iYrx)

#### 8. Edit File Settings for add setting configuration device 
Edit file add.html and edit.html (website/templates/setting/)
![Image of Edit file setting](https://drive.google.com/uc?export=view&id=1WonihNw1I0UqL3d_iHNzhYEiewk8Rw8X)

![Image of Edit file setting](https://drive.google.com/uc?export=view&id=1JMzVKdjaNOvNzhgvspkwXn-ki60HApSQ)


___

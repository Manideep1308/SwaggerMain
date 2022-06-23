from flask import Flask, request
from flasgger import Swagger
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)
 
@app.route('/vpc', methods=['POST'])          ####################VPC

def with_parameters():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stacknumber
        in: query
        type: string
        required: false
      - name: vpcname
        in: query
        type: string
        required: true        
      - name: vpcaddress
        in: query
        type: string
        required: true    
      - name: max_azs
        in: query
        type: string
        required: false
      - name: nat_gateway
        in: query
        type: string
        required: false       
      - name: subnet1name
        in: query
        type: string
        required: true     
      - name: subnet1address
        in: query
        type: string
        required: true
      - name: subnet_type1
        in: query
        type: string
        required: false  
      - name: subnet2name
        in: query
        type: string
        required: true 
      - name: subnet2address
        in: query
        type: string
        required: true 
      - name: subnet_type2
        in: query
        type: string
        required: false
      - name: cloudenv
        in: query
        type: string
        required: true  
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

    stacknumber = request.args.get('stacknumber')
    vpcname = request.args.get('vpcname')
    vpcaddress = request.args.get('vpcaddress')   
    max_azs = request.args.get('max_azs')
    nat_gateway = request.args.get('nat_gateway')
    subnet1name = request.args.get('subnet1name')
    subnet1address = request.args.get('subnet1address')
    subnet_type1 = request.args.get('subnet_type1')
    subnet2name = request.args.get('subnet2name')
    subnet2address = request.args.get('subnet2address')
    subnet_type2 = request.args.get('subnet_type2')
    cloudenv = request.args.get('cloudenv')
   
   
    vpc_aws = (
        "from aws_cdk import (Stack, aws_ec2 as ec2)\n"
        "from constructs import Construct\n"
        "class CdkEc2Stack" + str(stacknumber) + "(Stack):\n"
        "   def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n"
        "       super().__init__(scope, construct_id, **kwargs)\n" 
        "       vpc = ec2.Vpc(\n"
        "           self, '"  + str(vpcname)  + "',\n"
        "           cidr = '" + str(vpcaddress) + "',\n"
        "           max_azs=" + str(max_azs) + ",\n" 
        "           nat_gateways= " + str(nat_gateway) + ",\n"
        "           subnet_configuration=[\n"
        "                   ec2.SubnetConfiguration(name='" + str(subnet1name) + "', cidr_mask=" + str(subnet1address) + ", subnet_type=ec2.SubnetType. " + str(subnet_type1) + "),\n"
        "                   ec2.SubnetConfiguration(name='" + str(subnet2name) + "', cidr_mask=" + str(subnet2address) + ", subnet_type=ec2.SubnetType. " + str(subnet_type2) + ")])\n"
            

    )

    vpc_azure= (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n'
'      "vnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "'+ str(vpcname)+ '",\n'
'        "metadata": {\n'
'          "description": "VNet name"\n'
'        }\n'
'      },\n'
'      "vnetAddressPrefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(vpcaddress) + '",\n'
'        "metadata": {\n'
'          "description": "Address prefix"\n'
'        }\n'
'      },\n'
'      "subnet1Prefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet1address) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Prefix"\n'
'        }\n'
'      },\n'
'      "subnet1Name": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet1name) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Name"\n'
'        }\n'
'      },\n'
'      "subnet2Prefix": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet2address) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 2 Prefix"\n'
'        }\n'
'      },\n'
'      "subnet2Name": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnet2name) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 2 Name"\n'
'        }\n'
'      },\n'
'      "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "resources": [\n'
'      {\n'
'        "type": "Microsoft.Network/virtualNetworks",\n'
'        "apiVersion": "2020-06-01",\n'
'        "name": "[parameters(''\'vnetName\''')]",\n'
'        "location": "[parameters(''\'location\''')]",\n'
'        "properties": {\n'
'          "addressSpace": {\n'
'            "addressPrefixes": [\n'
'              "[parameters(''\'vnetAddressPrefix\''')]"\n'
'            ]\n'
'          },\n'
'          "subnets": [\n'
'            {\n'
'              "name": "[parameters(''\'subnet1Name\''')]",\n'
'              "properties": {\n'
'                "addressPrefix": "[parameters(''\'subnet1Prefix\''')]"\n'
'              }\n'
'            },\n'
'            {\n'
'              "name": "[parameters(''\'subnet2Name\''')]",\n'
'              "properties": {\n'
'                "addressPrefix": "[parameters(''\'subnet2Prefix\''')]"\n'
'              }\n'
'            }\n'
'          ]\n'
'        }\n'
'      }\n'
'    ]\n'
' }\n'
    )

    if(str(cloudenv) =='aws'):
        with open('vpc_template.py', 'w') as f:
            print(vpc_aws, file=f)

        return vpc_aws

    if(str(cloudenv) == 'azure'):
        with open('vpc_template.json', 'w') as f:
            print(vpc_azure, file=f)

        return vpc_azure

    else:
        return 'not matched'

@app.route('/secgroup', methods=['POST'])                      #########################SEC
def fun5():

  """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stacknumber
        in: query
        type: string
        required: false
      - name: vpcname
        in: query
        type: string
        required: false        
      - name: securitygroupname
        in: query
        type: string
        required: true    
      - name: rulename
        in: query
        type: string
        required: false
      - name: protocol
        in: query
        type: string
        required: true       
      - name: priority
        in: query
        type: string
        required: false     
      - name: direction
        in: query
        type: string
        required: false
      - name: ipaddress
        in: query
        type: string
        required: true  
      - name: port
        in: query
        type: string
        required: true 
      - name: cloudenv
        in: query
        type: string
        required: true  
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """  
  cloudenv = request.args.get('cloudenv') 
  securitygroupname = request.args.get('securitygroupname') 
  rulename = request.args.get('rulename')          
  protocol = request.args.get('protocol')
  priority = request.args.get('priority')
  direction = request.args.get('direction')
  ipaddress = request.args.get('ipaddress')
  port = request.args.get('port')
  stacknumber = request.args.get('stacknumber')                       
  vpcname = request.args.get('vpcname')
  
  



  sec_azure = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n'
'      "networkSecurityGroupName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(securitygroupname) + '",\n'
'      "metadata": {\n'
'        "description": "Name of the Network Security Group"\n'
'      }\n'
'    },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "resources": [\n'
'      {\n'
'      "type": "Microsoft.Network/networkSecurityGroups",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[parameters(''\'networkSecurityGroupName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "securityRules": [\n'
'          {\n'
'            "name": "' + str(rulename) + '",\n'
'            "properties": {\n'
'              "priority": ' + str(priority) + ',\n'
'            "protocol": "' + str(protocol) + '",\n'
'              "access": "Allow",\n'
'              "direction": "' + str(direction) + '",\n'
'              "sourceAddressPrefix": "' + str(ipaddress) + '",\n'
'              "sourcePortRange": "*",\n'
'              "destinationAddressPrefix": "*",\n'
'              "destinationPortRange": "' + str(port) + '"\n'
'            }\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  ]\n'
'}\n'
  )

  sec_aws = (

'from aws_cdk import (\n'
'    aws_ec2 as ec2, aws_iam as iam, Stack\n'

')\n'

'from constructs import Construct\n'

'\n'
'class CdkEc2Stack' + str(stacknumber) + '(Stack):\n'
'\n'
'    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n'
'        super().__init__(scope, construct_id,  **kwargs)\n'
'\n'
'        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="' + str(vpcname) + '")\n'
'\n'
'        sec_group1 = ec2.SecurityGroup(self, "iac_sg1",\n'
'            vpc=vpc, security_group_name="' + str(securitygroupname) + '",\n'
'           allow_all_outbound=True,\n'
'            )\n'
        
'      # add a new ingress rule to allow port 22 to internal hosts\n'
'        sec_group1.add_ingress_rule(\n'
'            peer=ec2.Peer.ipv4("' + str(ipaddress) + '"),\n'
'            description="Allow SSH connection", \n'
'            connection=ec2.Port.' + str(protocol) + '(' + str(port) + ')\n'
'            )'


    )
  
  if(str(cloudenv) =='aws'):
   with open('sec_template.py', 'w') as f:
        print(sec_aws, file=f)

   return (
            '{\n'
            '        "stacknumber": "' + str(stacknumber) + '",\n'
            '        "vpcname": "' + str(vpcname) + '",\n'
            '        "securitygroupname": "' + str(securitygroupname) + '",\n'
            '        "rulename": "' + str(rulename) + '",\n'
            '        "protocol": "' + str(protocol) + '",\n'
            '        "priority": "' + str(priority) + '",\n'
            '        "direction": "' + str(direction) + '",\n'
            '        "port": "' + str(port) + '",\n'
            '        "ipaddress": "' + str(ipaddress) + '",\n'
            '        "cloudenv": "' + str(cloudenv) + '"\n'

            '}\n'
        )


  if(str(cloudenv) =='azure'):
   with open('secgroup_template.json','w') as f:
      print(sec_azure, file=f)


   return sec_azure

 
@app.route('/ip', methods=['POST'])                   #########################IP

def ip():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: publicipname
        in: query
        type: string
        required: true
      - name: dnslabelname
        in: query
        type: string
        required: true        
      - name: publicIPAllocationMethod
        in: query
        type: string
        required: true    
      - name: publicIPAddressVersion
        in: query
        type: string
        required: true
      - name: idleTimeoutInMinutes
        in: query
        type: string
        required: true       
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    dnslabelname = request.args.get('dnslabelname')
    publicipname = request.args.get('publicipname')
    publicIPAllocationMethod =request.args.get('publicIPAllocationMethod')
    publicIPAddressVersion = request.args.get('publicIPAddressVersion')
    idleTimeoutInMinutes = request.args.get('idleTimeoutInMinutes')


    ip_zure = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n' 
'    "parameters": {\n' 
'    "dnsLabelPrefix": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(dnslabelname) + '",\n'
'      "metadata": {\n'
'        "description": "Unique DNS Name for the Public IP used to access the Virtual Machine."\n'
'      }\n'
'   },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'  
'    "variables": {\n'
'    "publicIPAddressName": "' + str(publicipname) + '"\n'

'     },\n'
'    "resources": [\n'

'            {\n'
'      "type": "Microsoft.Network/publicIPAddresses",\n'   #pubicIp
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'publicIPAddressName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "sku": {\n'
'        "name": "Basic"\n'
'      },\n'
'      "properties": {\n'
'        "publicIPAllocationMethod": "' + str(publicIPAllocationMethod) + '",\n'
'        "publicIPAddressVersion": "' + str(publicIPAddressVersion) + '",\n'
'        "dnsSettings": {\n'
'          "domainNameLabel": "[parameters(''\'dnsLabelPrefix\''')]"\n'
'        },\n'
'        "idleTimeoutInMinutes":' +str(idleTimeoutInMinutes) + '\n'
'      }\n'
'    }\n' 
'   ]\n'
'  }\n'    

    )


    with open('publicip_template.json','w') as f:
      print(ip_zure, file=f)


    return ip_zure   
@app.route('/nic', methods=['POST'])                      #########################NIC

def nic():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: nicname
        in: query
        type: string
        required: true
      - name: vpcname
        in: query
        type: string
        required: true        
      - name: securitygroupname
        in: query
        type: string
        required: true    
      - name: subnetname
        in: query
        type: string
        required: true
      - name: publicIpname
        in: query
        type: string
        required: true       
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    vpcname = request.args.get('vpcname')
    securitygroupname = request.args.get('securitygroupname')
    subnetname = request.args.get('subnetname')
    publicIpname = request.args.get('publicIpname')
    nicname = request.args.get('nicname')

    nic_az = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n' 
'      "vnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "'+ str(vpcname)+ '",\n'
'        "metadata": {\n'
'          "description": "VNet name"\n'
'        }\n'
'      },\n'
'      "subnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnetname) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Name"\n'
'        }\n'
'      },\n'
'      "networkSecurityGroupName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(securitygroupname) + '",\n'
'      "metadata": {\n'
'        "description": "Name of the Network Security Group"\n'
'      }\n'
'    },\n'        
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "variables": {\n'
'    "publicIPAddressName": "' + str(publicIpname) + '",\n'
'     "networkInterfaceName": "' + str(nicname) + '"\n'
'     },\n'
'    "resources": [\n'
'        {\n'
'      "type": "Microsoft.Network/networkInterfaces",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'networkInterfaceName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "ipConfigurations": [\n'
'          {\n'
'            "name": "ipconfig1",\n'
'            "properties": {\n'
'              "subnet": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/virtualNetworks/subnets\', parameters(''\'vnetName\'''), parameters(''\'subnetName\'''))]"\n'
'              },\n'
'              "privateIPAllocationMethod": "Dynamic",\n'
'              "publicIPAddress": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/publicIPAddresses\', variables(''\'publicIPAddressName\'''))]"\n'
'             }\n'
'            }\n'
'          }\n'
'        ],\n'
'        "networkSecurityGroup": {\n'
'          "id": "[resourceId(''\'Microsoft.Network/networkSecurityGroups\', parameters(''\'networkSecurityGroupName\'''))]"\n'
'        }\n'
'      }\n'
'    }\n'
'  ]\n'
'}\n'
    )


    with open('nic_template.json','w') as f:
      print(nic_az, file=f)


    return nic_az

@app.route('/vm', methods=['POST'])     ###################VM

def vm():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stacknumber
        in: query
        type: string
        required: false
      - name: vpcname
        in: query
        type: string
        required: false        
      - name: securitygroupname
        in: query
        type: string
        required: false    
      - name: instancename
        in: query
        type: string
        required: true
      - name: instancetype
        in: query
        type: string
        required: true       
      - name: authenticationType
        in: query
        type: string
        required: false     
      - name: instancevolume
        in: query
        type: string
        required: true
      - name: nicname
        in: query
        type: string
        required: false  
      - name: keyname
        in: query
        type: string
        required: false 
      - name: cloudenv
        in: query
        type: string
        required: true  
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """  

    cloudenv = request.args.get('cloudenv')
    instancename = request.args.get('instancename')
    instancetype = request.args.get('instancetype')
    instancevolume = request.args.get('instancevolume')                          
    authenticationType = request.args.get('authenticationType')
    nicname = request.args.get('nicname')
    stacknumber = request.args.get('stacknumber')   
    vpcname = request.args.get('vpcname')
    securitygroupname = request.args.get('securitygroupname')  
    keyname = request.args.get('keyname')


   
    vm_az = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n' 

'    "vmName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(instancename) + '",\n'
'      "metadata": {\n'
'        "description": "The name of you Virtual Machine."\n'
'      }\n'
'    },\n'
'    "adminUsername": {\n'
'      "type": "string",\n'
'      "defaultValue": "testuser",\n'
'      "metadata": {\n'
'        "description": "Username for the Virtual Machine."\n'
'      }\n'
'    },\n'
'    "authenticationType": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(authenticationType) + '",\n'
'      "allowedValues": [\n'
'        "sshPublicKey",\n'
'        "password"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "Type of authentication to use on the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'
'    "adminPasswordOrKey": {\n'
'      "type": "secureString",\n'
'      "defaultValue": "Open2022$",\n'
'      "metadata": {\n'
'        "description": "SSH Key or password for the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'

'    "ubuntuOSVersion": {\n'
'      "type": "string",\n'
'      "defaultValue": "18.04-LTS",\n'
'      "allowedValues": [\n'
'        "12.04.5-LTS",\n'
'        "14.04.5-LTS",\n'
'        "16.04.0-LTS",\n'
'        "18.04-LTS",\n'
'        "20.04-LTS"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version."\n'
'      }\n'
'    },\n'  
'    "vmSize": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(instancetype) + '",\n'
'      "metadata": {\n'
'        "description": "The size of the VM"\n'
'      }\n'
'    },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "variables": {\n'

'     "networkInterfaceName": "' + str(nicname) + '",\n'
'    "osDiskType": "' + str(instancevolume) + '",\n'
'    "linuxConfiguration": {\n'
'      "disablePasswordAuthentication": true,\n'
'      "ssh": {\n'
'        "publicKeys": [\n'
'          {\n'
'            "path": "[format(''\'/home/{0}/.ssh/authorized_keys\', parameters(''\'adminUsername\'''))]",\n'
'            "keyData": "[parameters(''\'adminPasswordOrKey\''')]"\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  },\n'
'    "resources": [\n'

'        {\n'
'      "type": "Microsoft.Compute/virtualMachines",\n'      #virtualmachine
'      "apiVersion": "2021-11-01",\n'
'      "name": "[parameters(''\'vmName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "hardwareProfile": {\n'
'          "vmSize": "[parameters(''\'vmSize\''')]"\n'
'        },\n'
'        "storageProfile": {\n'
'          "osDisk": {\n'
'            "createOption": "FromImage",\n'
'            "managedDisk": {\n'
'              "storageAccountType": "[variables(''\'osDiskType\''')]"\n'
'            }\n'
'          },\n'
'          "imageReference": {\n'
'            "publisher": "Canonical",\n'
'            "offer": "UbuntuServer",\n'
'            "sku": "[parameters(''\'ubuntuOSVersion\''')]",\n'
'            "version": "latest"\n'
'          }\n'
'        },\n'
'         "networkProfile": {\n'
'          "networkInterfaces": [\n'
'            {\n'
'              "id": "[resourceId(''\'Microsoft.Network/networkInterfaces\', variables(''\'networkInterfaceName\'''))]"\n'
'            }\n'
'          ]\n'
'        },\n'
'        "osProfile": {\n'
'          "computerName": "[parameters(''\'vmName\''')]",\n'
'          "adminUsername": "[parameters(''\'adminUsername\''')]",\n'
'          "adminPassword": "[parameters(''\'adminPasswordOrKey\''')]",\n'
'          "linuxConfiguration": "[if(equals(parameters(''\'authenticationType\'''), ''\'password\'''), null(), variables(''\'linuxConfiguration\'''))]"\n'
'        }\n'
'       }\n'        
'      }\n'
'  ]\n'
'}\n'
 )

    vm_aws=(

'from aws_cdk import (\n'
'    aws_ec2 as ec2, aws_iam as iam, Stack\n'

')\n'

'from constructs import Construct\n'

'\n'
'class CdkEc2Stack' + str(stacknumber) + '(Stack):\n'
'\n'
'    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n'
'        super().__init__(scope, construct_id,  **kwargs)\n'
'\n'
'        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="' + str(vpcname) + '")\n'
'\n'
'        sec_group1 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg1", vpc=vpc, security_group_name="' + str(securitygroupname) + '")\n'
        
                
'        # Instance Role and SSM Managed Policy\n'
'        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))\n'
'        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))\n'


'        # ubuntu image\n'
'        ub_image = ec2.MachineImage.from_ssm_parameter("/aws/service/canonical/ubuntu/server/focal/stable/current/amd64/hvm/ebs-gp2/ami-id")\n'

'        # Instance1\n'
'        instance = ec2.Instance(self, "IaCInstance1", instance_name="' + str(instancename) + '",\n'
'            instance_type=ec2.InstanceType("' + str(instancetype) + '"),\n'
'            machine_image=ub_image,\n'
'            block_devices=[\n'
'                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(' + str(instancevolume) + '))\n'
'            ],\n'
'            vpc = vpc,\n'            
'            vpc_subnets=ec2.SubnetSelection(\n'
'                subnet_type=ec2.SubnetType.PUBLIC\n'
'             ),\n'
'            role=role,\n'
'            security_group=sec_group1,\n'
'            key_name = "' + str(keyname) + '"\n'
'            )\n'
    


    )
   


    if(str(cloudenv) =='aws'):
     with open('ec2_template.py', 'w') as f:
        print(vm_aws, file=f)

     return (
            '{\n'
            '        "stacknumber": "' + str(stacknumber) + '",\n'
            '        "vpcname": "' + str(vpcname) + '",\n'
            '        "securitygroupname": "' + str(securitygroupname) + '",\n'
            '        "instancename": "' + str(instancename) + '",\n'
            '        "instancetype": "' + str(instancetype) + '",\n'
            '        "authenticationType": "' + str(authenticationType) + '",\n'
            '        "instancevolume": "' + str(instancevolume) + '",\n'
            '        "nicname": "' + str(nicname) + '",\n'
            '        "keyname": "' + str(keyname) + '",\n'
            '        "cloudenv": "' + str(cloudenv) + '"\n'

            '}\n'
        )

         

    if(str(cloudenv) =='azure'):
     with open('vmnetworkinterface_template.json','w') as f:
        print(vm_az, file=f)
 

     return vm_az    

app.run(port=6001, host='0.0.0.0')           
from flask import Flask, request
import subprocess
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route("/vnet")
def vnet():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: vnetname
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
    resourcegroup =request.args.get('resourcegroup')
    vnetname =request.args.get('vnetname')  
    # cmd = (["az", "network", "vnet", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "vnet", "show", "--name", str(vnetname), "--resource-group", str(resourcegroup) ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/vnetdeployment")

def vnetdeploydex():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "vpc_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/nsg")
def nsg():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: nsgname
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
    resourcegroup =request.args.get('resourcegroup')
    nsgname =request.args.get('nsgname')   
    # cmd = (["az", "network", "nsg", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "nsg", "show", "--name", str(nsgname), "--resource-group", str(resourcegroup) ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/nsgdeployment")

def nsg2():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "secgroup_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out  

@app.route("/publicip")
def ip():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: publicipname
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
    resourcegroup =request.args.get('resourcegroup') 
    publicipname =request.args.get('publicipname')  
    # cmd = (["az", "network", "public-ip", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "public-ip", "show", "--name", str(publicipname), "--resource-group", str(resourcegroup) ]) 
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/publicipdeployment")

def ip2():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "publicip_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out     

@app.route("/nic")
def nic():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: nicname
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
    resourcegroup =request.args.get('resourcegroup')
    nicname = request.args.get('nicname')   
    # cmd = (["az", "network", "nic", "list", "--resource-group", str(resourcegroup) ])
    cmd = (["az", "network", "nic", "show","--name", str(nicname), "--resource-group", str(resourcegroup) ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/nicdeployment")

def index():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "nic_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out 

@app.route("/vm")
def vm():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
        in: query
        type: string
        required: true
      - name: vmname
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
    resourcegroup =request.args.get('resourcegroup')  
    vmname=request.args.get('vmname') 
    # cmd = (["az", "vm", "list", "--resource-group", str(resourcegroup) , "--show-details" ])
    cmd = (["az", "vm",  "show", "--name", str(vmname), "--resource-group", str(resourcegroup), "--show-details" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out

@app.route("/vmdeployment")

def vm1():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: resourcegroup
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
    resourcegroup =request.args.get('resourcegroup')   
    cmd = (["az", "deployment", "operation", "group", "list", "--resource-group", str(resourcegroup), "--name", "vmnetworkinterface_template" ])
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
                       
    out, err = p.communicate()
    return out 

app.run(port=6005, host='0.0.0.0')               
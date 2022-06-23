from flask import Flask, request
import boto3
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)

@app.route('/vpc_check')
def vpc():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: vpcname
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
    ec2 = boto3.client('ec2')

               
    response = ec2.describe_vpcs(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                 str(vpcname)
            ]
        }
   
    ]
) 

    return (response)

@app.route('/subnet_check')
def subnet():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stackname
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

    stackname =request.args.get('stackname')
   
    ec2 = boto3.client('ec2')
    response = ec2.describe_subnets(
        Filters=[
        # {
        #     'Name': 'tag:aws-cdk:subnet-name',
        #     'Values': [
        #         str(subnetname)
        #     ]
        # },
        {"Name":"tag:aws:cloudformation:stack-name", "Values":[str(stackname)]}
        
    ]
)

    return (response) 
@app.route('/sg_check')
def sg():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: securitygroupname
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
    securitygroupname =request.args.get('securitygroupname')
   
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups(
           Filters=[
      
          {
            'Name': 'group-name',
            'Values': [
                str(securitygroupname)
            
            ]
        }
        
    ]
)
    return (response)
@app.route('/instance_check')
def instance():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: instancename
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
    instancename=request.args.get('instancename')
    ec2 = boto3.client('ec2')

               
    response1 = ec2.describe_instances(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                str(instancename)
            ]
        }
            
    ]
) 

    return (response1)
@app.route('/resource_check')
def resource():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: stackname
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
    stackname =request.args.get('stackname')

    client = boto3.client('cloudformation')                     

    list = client.list_stack_resources(StackName = str(stackname)) 
    # list.mimetype = 'application/json'
    # if (client.list_stack_resources(StackName = str(stackname))):
    return (list)
    
    
app.run(port=6004, host='0.0.0.0')       
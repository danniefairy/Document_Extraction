set AWSCLI="C:\\Program Files\\Amazon\\AWSCLIV2\\aws.exe"
%AWSCLI% configure set aws_access_key_id MY_ACCESS_KEY
%AWSCLI% configure set aws_secret_access_key MY_SECRET_KEY
%AWSCLI% configure set region us-east-2
%AWSCLI% ec2 create-key-pair --key-name KeyExample --query 'KeyMaterial' --output text > key-example.pem
%AWSCLI% cloudformation create-stack --stack-name exampleStack --template-body file://scripts\\aws_deploy\\template.json --parameters ParameterKey=KeyExample,ParameterValue=KeyExample
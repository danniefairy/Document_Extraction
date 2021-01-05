#!/bin/bash

aws cloudformation create-stack --stack-name exampleStack --template-body file://template.json --parameters ParameterKey=KeyExample,ParameterValue=KeyExample
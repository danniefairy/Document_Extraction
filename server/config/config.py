import subprocess

CONFIG = {
    "local": {
        "endpoint": "localhost",
        "port": 5000
    },
    "aws": {
        "endpoint": "AWS Endpoint",
        "port": "AWS Port"
    }
}


def configuration(env):
    if env == "aws":
        CONFIG["aws"]["endpoint"] = get_aws_instance_ip()
        CONFIG["aws"]["port"] = 80
        return CONFIG["aws"]
    return CONFIG["local"]


def get_aws_instance_ip():
    outputs = subprocess.check_output(['curl', 'wgetip.com'])
    return outputs.decode("utf-8")

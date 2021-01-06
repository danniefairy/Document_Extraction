import subprocess

CONFIG = {
    "local": {
        "endpoint": "localhost",
        "port": 5000
    },
    "aws": {
        "endpoint": "",
        "port": 80
    }
}


def configuration(env):
    if env == "local":
        return CONFIG[env]
    CONFIG[env]["endpoint"] = get_aws_instance_ip()
    return CONFIG[env]


def get_aws_instance_ip():
    outputs = subprocess.check_output(['curl', 'wgetip.com'])
    return outputs.decode("utf-8")

import subprocess
import config

# Run a local command
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out=out.decode("utf-8") 
    if out == "":
        ret = process.returncode
        if ret == 0:
            return "OK"
        else:
            return f"Failed? (returned {ret})"
    else:
        return str(out)

# Run a remote command on ssh
def remote_command(command, timeout=config.timeout):
    return run_command( f"timeout {timeout} ssh {config.host} {command}".split(" "))

# command handlers
def wol():
    return run_command(["wakeonlan", config.mac_address])
def suspend():
    return remote_command("sudo systemctl suspend")
def halt():
    return remote_command("sudo poweroff")
def ping():
    return run_command(["ping","-c5",config.address])
def uptime():
    return remote_command("uptime")


def update_environment(line):
    """ Loads specified modules and updates environment """
    import sys, os
    import subprocess
    import random
    import string
    import json

    def get_environment_from_batch_command(env_cmd, initial=None):
        """
        Take a command (either a single command or list of arguments)
        and return the environment created after running that command.

        If initial is supplied, it is used as the initial environment passed
        to the child process.
        """
        if not isinstance(env_cmd, (list, tuple)):
            cmd = [env_cmd]
        sep = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
        cmd = cmd + ['echo \'%s\'' % sep, 'python -c "import os, json; print(json.dumps(dict(os.environ)))"']
        cmdline = '; '.join(cmd) + ';'

        # launch the process
        proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE, env=initial, shell=True)
        # parse the output sent to stdout
        lines = proc.stdout

        cmd_output = []
        env_output = {}
        cmd_output_finished = False
        sep = sep.encode('utf-8')
        for l in lines:
            s = l.rstrip()
            if s != sep:
                if not cmd_output_finished:
                    cmd_output.append(s)
                else:
                    env_output = json.loads(s)
            else:
                cmd_output_finished = True            
        # let the process finish
        proc.communicate()
        return env_output

    os.environ.update(get_environment_from_batch_command(line))

def load_ipython_extension(ipython):
    ipython.register_magic_function(update_environment, 'line')

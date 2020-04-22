import subprocess


def run_script(script_path):
    try:
        process = subprocess.run(script_path, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout
    except Exception:
        print(f'exception in running script - {script_path}')
        raise

    return output


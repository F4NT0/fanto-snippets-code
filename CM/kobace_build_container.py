import os
import sys
import subprocess
from subprocess import run, CalledProcessError, Popen, PIPE
from devops_k8s_cli.functions.k8s_login import k8s_kobace_login
from devops_k8s_cli.functions.kobace_operations import string_formatting
def kobace_build_container(logger,kobace_manifest_file):
    k8s_kobace_login(logger)
    mf_file_path = os.getenv('KOBACE_MANIFEST_FILE')
    namespace = os.getenv('NAMESPACE')
    logger.info(f'Building image for {mf_file_path}')
    build_image_cmd = ['kob', 'build-image', '-f', f'{mf_file_path}', '-n', f'{namespace}']
    try:
        #result = subprocess.Popen(f'/usr/bin/kob build-image -f {mf_file_path} -n {namespace}', stdout=subprocess.PIPE, stderr=sys.stdout)
        result = Popen(build_image_cmd, stdout=subprocess.PIPE, stderr=PIPE)
        if result.returncode != 0 and result.returncode is not None:
            logger.error('Failed to build image', result.returncode)
            sys.exit(result.returncode)
        for line in result.stdout:
            print(line.decode('utf-8'), end='')
            prev_line = None
            if 'harbor.dell.com' in line.decode('utf-8'):
                if os.getenv('DEPLOY_ENVIRONMENT'):
                    os.environ['KOBACE_IMAGE_FILE_NAME'] = f'kob-build-container-{os.getenv("DEPLOY_ENVIRONMENT")}.txt'
                else:
                    os.environ['KOBACE_IMAGE_FILE_NAME'] = 'kob-build-container.txt'
                with open(f'{os.getenv("KOBACE_IMAGE_FILE_NAME")}', 'w') as f:
                    f.write(string_formatting(line.decode('utf-8').split('|')[1]).strip())
            elif prev_line and  "Cleanup local atifacts" in prev_line and any(word in line.decode('utf-8').lower() for word in ['error', 'failed']):
                logger.error(f"Failed to build image {line.decode('utf-8')}")
                exit(1)
            prev_line = line.decode('utf-8')
        
        #Check if file exists and then write into the file
        file_name = os.getenv('KOBACE_IMAGE_FILE_NAME')
        if os.path.isfile(file_name):
            logger.info(f'Successfully built image for {mf_file_path}')
        else:
            logger.error(f'Failed to build image for {mf_file_path}')
            sys.exit(1)
    except CalledProcessError as e:
        logger.error(f'Failed to build image for {mf_file_path}')
        logger.debug(e.stderr.decode('utf-8'))
        sys.exit(1)
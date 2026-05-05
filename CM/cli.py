import sys
import click
import os
from devops_k8s_cli.core import CommonMethods
from devops_k8s_cli.commands.validate import k8s_validate
from devops_k8s_cli.commands.deploy import k8s_deploy
from devops_k8s_cli.utils.fetch_secrets import fetch_secrets
from devops_k8s_cli.commands.switch_route import k8s_switch_route
from devops_k8s_cli.commands.build_docker import build_and_push_docker_image
from devops_k8s_cli.commands.build_helm import build_and_push_helm_package
from devops_k8s_cli.functions.k8s_login import k8s_login
from devops_k8s_cli.commands.kobace_deployment import k8s_kobace
from devops_k8s_cli.commands.kobace_build_container import kobace_build_container
from devops_k8s_cli.commands.rollback import helm_rollback
from devops_k8s_cli.commands.kobace_switch_route import k8s_kobace_sr
from devops_k8s_cli.commands.kobace_cleanup import k8s_kobace_cleanup


@click.group()
@click.version_option(package_name='devops-k8s-cli')
@click.option('-l', '--log_level', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
              help='Log level to be set', default='DEBUG')
@click.option('--log_file', type=str, help='Log file to be used', default='logs/devops-k8s-cli-logs.log')
@click.pass_context
def cli(ctx, log_level, log_file):
    """
    DevOps K8s CLI helps in performing deployment and validation of kubernetes/PKS , KOB, Helm apps.
    """
    ctx.obj = CommonMethods(log_level, log_file)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('-f', '--file-paths', type=str, required=False, help='Comma separated list of the k8s object '
                                                                   'file path. File paths should be in format of '
                                                                   'SECRET_FILE, CONFIG_FILE, DEPLOYMENT_FILE, '
                                                                   'SERVICE_FILE, INGRESS FILE')
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def deploy(devops_k8s_cli_obj, secret_path, file_paths, prod, non_prod):
    """
    deploy command will help in deploying app to k8s using kubectl or helm package manager
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    try:
        if file_paths:
            target_k8s_objects = [path.strip() for path in file_paths.split(',')]
        else:
            target_k8s_objects = []
    except Exception as e:
        logger.error(f'Error in parsing file paths: {e}')
        sys.exit(1)

    if prod:
        logger.info('## Deploying to production')
        k8s_deploy(logger, target_k8s_objects)
    else:
        logger.info('## Deploying to non-production')
        k8s_deploy(logger, target_k8s_objects)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
# @click.option('-f', '--file-paths', type=str, required=False, help='Provide Path of manifest file')
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def k8s_kobace_deploy(devops_k8s_cli_obj, secret_path, prod, non_prod):
    """
    deploy command will help in deploying app to k8s using kubectl or helm package manager
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    # try:
    #     if file_paths:
    #         target_k8s_objects = [path.strip() for path in file_paths.split(',')]
    #     else:
    #         target_k8s_objects = []
    # except Exception as e:
    #     logger.error(f'Error in parsing file paths: {e}')
    #     sys.exit(1)

    if prod:
        logger.info('## Deploying to production')
        k8s_kobace(logger)
    else:
        logger.info('## Deploying to non-production')
        k8s_kobace(logger)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def k8s_kobace_switch_route(devops_k8s_cli_obj, secret_path, prod, non_prod):
    """
    switch_route command will help in switching route in case of blue-green deployment
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    if prod:
        logger.info('## Deploying to production')
        k8s_kobace_sr(logger)
    else:
        logger.info('## Deploying to non-production')
        k8s_kobace_sr(logger)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def k8s_kobace_cleanup_action(devops_k8s_cli_obj, secret_path, prod, non_prod):
    """
    delete command will helps to delete application in the KOB namespace
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    if prod:
        logger.info('## Deploying to production')
        k8s_kobace_cleanup(logger)
    else:
        logger.info('## Deploying to non-production')
        k8s_kobace_cleanup(logger)



# @cli.command()
# @click.option('-s', '--secret-path', required=True, type=str,
#               help='Pass Vault secret path to fetch secrets from Vault')
# @click.option('-f', '--file-paths', type=str, required=False, help='Provide Path of the manifest object')
# @click.pass_obj
# def kob_build_container(devops_k8s_cli_obj, secret_path, file_paths):
#     """
#     Kob build image command will help in building image in case of kobace deployment
#     """

#     logger = devops_k8s_cli_obj.common_method()
#     fetch_secrets(logger, secret_path, "ENV")

#     try:
#         if file_paths:
#             kobace_manifest_file = [path.strip() for path in file_paths.split(',')]
#         else:
#             kobace_manifest_file = []
#     except Exception as e:
#         logger.error(f'Error in parsing file paths: {e}')
#         sys.exit(1)

#     logger.info('## KOB Building image to build container')
#     kobace_build_container(logger,kobace_manifest_file)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('-f', '--file-paths', type=str, required=False, help='Comma separated list of the k8s object '
                                                                   'file path. File paths should be in format of '
                                                                   'SECRET_FILE, CONFIG_FILE, DEPLOYMENT_FILE, '
                                                                   'SERVICE_FILE, INGRESS FILE')
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def switch_route(devops_k8s_cli_obj, secret_path, file_paths, prod, non_prod):
    """
    switch_route command will help in switching route in case of blue-green deployment
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    try:
        if file_paths:
            target_k8s_objects = [path.strip() for path in file_paths.split(',')]
        else:
            target_k8s_objects = []
    except Exception as e:
        logger.error(f'Error in parsing file paths: {e}')
        sys.exit(1)

    if prod:
        logger.info('## Switching Route - production')
        k8s_switch_route(logger, target_k8s_objects)
    else:
        logger.info('## Switching Route - non-production')
        k8s_switch_route(logger, target_k8s_objects)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('--prod', is_flag=True, help='This decides if deployment is production')
@click.option('--non-prod', is_flag=True, help='This decides if deployment is non-production')
@click.pass_obj
def rollback(devops_k8s_cli_obj, secret_path, prod, non_prod):
    """
    switch_route command will help in switching route in case of blue-green deployment
    """
    if prod and non_prod:
        raise click.UsageError('Flags --prod and --non-prod cannot be used together.')
    elif not prod and not non_prod:
        raise click.UsageError('One of the flags --prod or --non-prod is required.')

    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    if prod:
        logger.info('## Reverting changes in a production environment')
        helm_rollback(logger)
    else:
        logger.info('## Reverting changes in a non-production environment')
        helm_rollback(logger)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.option('-f', '--file-paths', type=str, required=False, help='Comma separated list of the k8s object '
                                                                   'file path. File paths should be in format of '
                                                                   'SECRET_FILE, CONFIG_FILE, DEPLOYMENT_FILE, '
                                                                   'SERVICE_FILE, INGRESS FILE')
@click.pass_obj
def validate(devops_k8s_cli_obj, secret_path, action, file_paths, prod, non_prod):
    """
    validate command will help in validating k8s objects
    """
    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")
    k8s_validate(logger)


@cli.command()
@click.pass_obj
def build_docker(devops_k8s_cli_obj):
    """
    build_docker command will help in building and pushing docker image to Harbor
    """
    logger = devops_k8s_cli_obj.common_method()
    if os.getenv('AKS_SECRET_PATH') is not None:
        secret_path = os.getenv('AKS_SECRET_PATH')
        logger.info('## Building and pushing docker image to ACR')
        logger.info(f'## Using AKS_SECRET_PATH: {secret_path}')
        # fetch_secrets(logger, secret_path, "ENV")
        server_type = "AKS"
    elif os.getenv('VAULT_HARBOR_SECRET_PATH') is not None:
        logger.info('## Building and pushing docker image to Harbor')
        secret_path = os.getenv('VAULT_HARBOR_SECRET_PATH')
        logger.info(f'## Using HARBOR_SECRET_PATH: {secret_path}')
        # fetch_secrets(logger, secret_path, "ENV")
        server_type = "HARBOR"
    build_and_push_docker_image(logger, secret_path, server_type)


@cli.command()
@click.pass_obj
def build_container(devops_k8s_cli_obj):
    """
    build_docker command will help in building and pushing docker image to Harbor
    """
    logger = devops_k8s_cli_obj.common_method()
    if os.getenv('CONTAINER_TOOL').lower() == "kob" and os.getenv('KOBACE_MANIFEST_FILE') is not None:
        logger.info('## Building docker image in KOB cluster and pushing to HARBOR')
        logger.info(f'## Using KOBACE_MANIFEST_FILE: {os.getenv("KOBACE_MANIFEST_FILE")}')
        secret_path = os.getenv('VAULT_CONFIG_PATH')
        fetch_secrets(logger, secret_path, "ENV")
        kobace_manifest_file = os.getenv("KOBACE_MANIFEST_FILE")
        logger.info('## KOB Building image to build container')
        kobace_build_container(logger,kobace_manifest_file)
    elif os.getenv('AKS_SECRET_PATH') is not None:
        secret_path = os.getenv('AKS_SECRET_PATH')
        logger.info('## Building and pushing docker image to ACR')
        logger.info(f'## Using AKS_SECRET_PATH: {secret_path}')
        server_type = "AKS"
        build_and_push_docker_image(logger, secret_path, server_type)

    elif os.getenv('VAULT_HARBOR_SECRET_PATH') is not None:
        logger.info('## Building and pushing docker image to Harbor')
        secret_path = os.getenv('VAULT_HARBOR_SECRET_PATH')
        logger.info(f'## Using HARBOR_SECRET_PATH: {secret_path}')
        server_type = "HARBOR"
        build_and_push_docker_image(logger, secret_path, server_type)


@cli.command()
@click.pass_obj
def build_helm(devops_k8s_cli_obj):
    """
    Build_Helm command will help in building and pushing Helm chart package zip file to Harbor
    """
    logger = devops_k8s_cli_obj.common_method()
    if 'VAULT_HARBOR_HELM_SECRET' in os.environ:
        logger.info('## Building and pushing Helm chart package zip file to Harbor')
        secret_path = os.getenv('VAULT_HARBOR_HELM_SECRET')
        logger.info(f'## Using VAULT_HARBOR_HELM_SECRET: {secret_path}')
        fetch_secrets(logger, secret_path, "ENV")
        server_type = "HARBOR"
    elif 'VAULT_ARTIFACT_HELM_SECRET' in os.environ:
        secret_path = os.getenv('VAULT_ARTIFACT_HELM_SECRET')
        logger.info('## Building and pushing Helm chart package zip file to Artifactory')
        logger.info(f'## Using VAULT_ARTIFACT_HELM_SECRET: {secret_path}')
        fetch_secrets(logger, secret_path, "ENV")
        server_type = "ARTIFACTORY"
    else:
        logger.error('## Please provide variable either VAULT_HARBOR_HELM_SECRET or VAULT_ARTIFACT_HELM_SECRET')
        sys.exit(1)
    build_and_push_helm_package(logger, server_type)


@cli.command()
@click.option('-s', '--secret-path', required=True, type=str,
              help='Pass Vault secret path to fetch secrets from Vault', )
@click.pass_obj
def login(devops_k8s_cli_obj, secret_path):
    """
    deploy command will help in deploying app to k8s using kubectl or helm package manager
    """
    logger = devops_k8s_cli_obj.common_method()
    fetch_secrets(logger, secret_path, "ENV")

    k8s_login(logger)


@cli.command()
@click.pass_obj
def logout(devops_k8s_cli_obj):
    """
    logout command will help in logging out from k8s cluster
    """
    logger = devops_k8s_cli_obj.common_method()
    logger.info('## logged out of k8s cluster is not supported yet')


if __name__ == '__main__':
    cli()  # Ensure obj is initialized

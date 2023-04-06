import argparse
import subprocess

parser = argparse.ArgumentParser(description="This can be used to build/build/push/deploy/test a docker image.\n \
                                You can use it in the following ways:            \
                                python pipeline.py BUILD --dockerFilePath=<arg1> --imageName=<arg2> --imageTag=<arg3>;            \
                                python pipeline.py DEPLOY --flavour=[docker/kubernetes] --imageName=<arg2> --imageTag=<arg3>            \
                                python pipeline.py PUSH --containerRegistryUsername=<arg1> --imageName=<arg2> --imageTag=<arg3>            \
                                python pipeline.py TEST --endpoint=<URL> \
                                 ")

parser.add_argument('command', choices=['build', 'push', 'deploy', 'test'], help='command to execute')
#arguments without -- are always required and they're called positionals. the ones with -- are called optionals.


#Build arguments
parser.add_argument('--dockerFilePath', required=False, default='.', help="Path to Dockerfile. By default it's going to be the current folder.")
parser.add_argument('--imageName', required=False, help="Name of the Docker image. If you don't specify it, it's going to be something random.")
parser.add_argument('--imageTag', required=False, help="Tag of the Docker image. It's going to be 'latest' if you don't specify it")

#Push arguments
parser.add_argument('--containerRegistryUsername', required=False, help=' Username for the dockerhub account where you want this uploaded.')

#Deploy arguments
parser.add_argument('--flavour', required=False, choices=['docker', 'kubernetes'], help='Containers or clusters?')

#Test arguments
parser.add_argument('--endpoint', required=False, help='URL of the endpoint to test using CURL.')

args = parser.parse_args()

if args.command == 'build':
    dockerfile_path = args.dockerFilePath
    image_name = args.imageName
    image_tag = args.imageTag
    subprocess.run(['docker', 'build', '-t', f"{image_name}:{image_tag}", dockerfile_path])

elif args.command == 'push':
    container_registry_username = args.containerRegistryUsername
    image_name = args.imageName
    image_tag = args.imageTag
    subprocess.run(['docker', 'login', '-u', container_registry_username])
    subprocess.run(['docker', 'push', f"{image_name}:{image_tag}"])

elif args.command == 'deploy':
    flavour = args.flavour
    image_name = args.imageName
    image_tag = args.imageTag
    if flavour == 'docker':
        subprocess.run(['docker', 'run', '-d', '-p', '5050:5000', f"{image_name}:{image_tag}"])
    elif flavour == 'kubernetes':
        # TBD
        pass

elif args.command == 'test':
    endpoint = args.endpoint
    response = subprocess.run(['curl', '-I', endpoint])
    print(response)

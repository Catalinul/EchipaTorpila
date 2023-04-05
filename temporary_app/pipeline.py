import argparse
import subprocess

parser = argparse.ArgumentParser(description='This can be used to build/build/push/deploy/test a docker image.')

parser.add_argument('command', choices=['build', 'push', 'deploy', 'test'], help='command to execute')
#argumentele care nu au "--" in fata sunt required always si se numesc positionals. daca ii puneam -- in fata, 
#atunci era un argument de tipul optional, precum flag-uri/options

# Build arguments
parser.add_argument('--dockerFilePath', required=False, default='.', help='path to Dockerfile')
parser.add_argument('--imageName', required=False, help='name of the Docker image')
parser.add_argument('--imageTag', required=False, help='tag of the Docker image')

# Push arguments
parser.add_argument('--containerRegistryUsername', required=False, help='username for the container registry')

# Deploy arguments
parser.add_argument('--flavour', required=False, choices=['docker', 'kubernetes'], help='deployment flavour')

# Test arguments
parser.add_argument('--endpoint', required=False, help='URL of the endpoint to test')

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
        subprocess.run(['docker', 'run', '-d', '-p', '5000:5000', f"{image_name}:{image_tag}"])
    elif flavour == 'kubernetes':
        # TBD
        pass

elif args.command == 'test':
    endpoint = args.endpoint
    response = subprocess.run(['curl', '-I', endpoint])
    print(response)

import sys
# Read in the file
with open('argocd-app-config/' + sys.argv[1] + '/kubernetes.yml', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('jenkins', 'nbglink')

# Write the file out again
with open('argocd-app-config/' + sys.argv[1] + '/kubernetes.yml', 'w') as file:
  file.write(filedata)

import re

file_path = "DemoAppApplication.java"
new_value = sys.argv[1]  # Replace "new-value" with the value that you want to use

with open(file_path, 'r') as file:
    data = file.read()

old_value_pattern = r'@DockerBuild\(image\s*=\s*"[^"]+"\)'
new_data = re.sub(old_value_pattern, '@DockerBuild(image="' + new_value + '")', data)

with open(file_path, 'w') as file:
    file.write(new_data)
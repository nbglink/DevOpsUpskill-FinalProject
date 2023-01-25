import sys
# Read in the file
with open('argocd-app-config/' + sys.argv[1] + '/kubernetes.yml', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('jenkins', 'nbglink')

# Write the file out again
with open('argocd-app-config/' + sys.argv[1] + '/kubernetes.yml', 'w') as file:
  file.write(filedata)
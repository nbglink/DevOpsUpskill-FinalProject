import sys
import re
import xml.etree.ElementTree as ET

#Replace the image name value in DemoAppApplication.java with Jenkins environment variable/s

file_path = "./src/main/java/com/devopskills/demoapp/DemoAppApplication.java"
new_value = sys.argv[1]  # Replace "new-value" with the value that you want to use

with open(file_path, 'r') as file:
    data = file.read()

old_value_pattern = r'@DockerBuild\(image\s*=\s*"[^"]+"\)'
new_data = re.sub(old_value_pattern, '@DockerBuild(image="' + new_value + '")', data)

with open(file_path, 'w') as file:
    file.write(new_data)

#Replace the name and version values in Dockerfile with Jenkins environment variable/s

file_path = "Dockerfile"
new_value = sys.argv[2]+ "-" + sys.argv[3] # Replace "new-value" with the value that you want to use

with open(file_path, 'r') as file:
    data = file.read()

old_value_pattern = re.compile(r'(?<=COPY \./target/).+?(?=.jar)')
new_data = re.sub(old_value_pattern, new_value, data, count=1)

old_value_pattern = re.compile(r'(?<=ENTRYPOINT \["java", "-jar", ").+?(?=.jar)')
new_data = re.sub(old_value_pattern, new_value, new_data, count=1)

with open(file_path, 'w') as file:
    file.write(new_data)

#Replace the groupId, version and name values in pom.xml with Jenkins environment variable/s

# specify the file path
file_path = "pom.xml"

ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
# parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

# define the namespace
ns = {"pom": "http://maven.apache.org/POM/4.0.0"}

# update the values of the tags
artifact_id = root.findall("./pom:artifactId", ns)[0]
artifact_id.text = sys.argv[2]

version = root.findall("./pom:version", ns)[0]
version.text = sys.argv[3]

name = root.findall("./pom:name", ns)[0]
name.text = sys.argv[2]

# write the updated XML to the file
tree.write(file_path)
import sys
import re

file_path = "../src/main/java/com/devopskills/demoapp/DemoAppApplication.java"
new_value = sys.argv[1]  # Replace "new-value" with the value that you want to use

with open(file_path, 'r') as file:
    data = file.read()

old_value_pattern = r'@DockerBuild\(image\s*=\s*"[^"]+"\)'
new_data = re.sub(old_value_pattern, '@DockerBuild(image="' + new_value + '")', data)

with open(file_path, 'w') as file:
    file.write(new_data)
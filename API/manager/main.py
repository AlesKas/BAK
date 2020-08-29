import yaml
import connexion

with open('manager.specs.yaml', 'r') as specsfile:
    SPECS = yaml.safe_load(specsfile)

print("Hello World")
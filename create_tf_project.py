import os

TERRAFORM_FILE = ["main.tf", "variables.tf", "outputs.tf", "versions.tf", "providers.tf", "backend.tf", "terraform.tfvars"]

current_path = os.getcwd()
for tf_file in TERRAFORM_FILE:
	file_path = os.path.join(current_path, tf_file)
	if not os.path.exists(file_path):
		f = open(file_path, 'x')
		f.close

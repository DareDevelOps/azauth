import az_auth

sub_id = az_auth.sub_id
client = az_auth.client

group_list = client.resource_groups.list()

column_width = 29
print("Resource Group".ljust(column_width) + "Location".ljust(column_width) + "state".ljust(column_width))
print("-" * (column_width * 3))

for group in group_list:
    
    print(f"{group.name:<{column_width}}{group.location:<{column_width}} {group.properties.provisioning_state:<{column_width}}")

print("-" * (column_width * 3))
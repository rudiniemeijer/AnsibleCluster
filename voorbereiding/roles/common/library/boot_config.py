#!/usr/bin/python

def updateKey(name, value, state, data):
    changed = False
    name_found = False
    new_file=[]
    if state == "absent":
        new_line = "#{}={}\n".format(name,value)
    else:
        new_line = "{}={}\n".format(name,value)

    for line in data:
        if line.strip().startswith(name + "="):
            name_found = True
            if line != new_line:
                line = new_line
                changed = True
        new_file.append(line)
    if not name_found:
        new_file.append(new_line)
        changed = True
    
    return changed, new_file

def updateDtParam( value, state, data):
    changed = False
    found = False
    new_file=[]

    if state == "absent":
        new_line = "#dtparam={}\n".format(value)
    else:
        new_line = "dtparam={}\n".format(value)

    for line in data:
        if line.strip().startswith("dtparam=") or line.strip().startswith("#dtparam="):
            index = line.index('=')
            line_value = line[index+1:]
            if value.strip() == line_value.strip():
                found = True
                if line != new_line:
                    line = new_line
                    changed = True
        new_file.append(line)

    if not found:
        new_file.append(new_line)
        changed = True
    
    return changed, new_file

def main():
    module = AnsibleModule(
        argument_spec=dict(
            state       = dict(default='present', choices=['present', 'absent']),
            name     = dict(required=True),
            value     = dict(required=True),
        ),
        supports_check_mode=True,
    )

    name =  module.params['name']
    value =  module.params['value']
    state =  module.params['state']

    config_file='/boot/config.txt'
    try:
        with open(config_file, 'r') as myfile:
            data=myfile.readlines()
    except IOError:
        module.fail_json(msg='Failed to read the config file from {}'.format(config_file))

    if name == "dtparam":
        changed, new_file = updateDtParam(value, state, data)
    else:
        changed, new_file = updateKey(name, value, state, data)

    if not module.check_mode and changed:
        try:
            with open(config_file, 'w') as myfile:
                myfile.writelines(new_file)
        except IOError:
            module.fail_json(msg='Failed to write to config file from {}'.format(config_file))

    module.exit_json(changed=changed)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
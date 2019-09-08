#!/usr/bin/python
import glob

def main():
    module = AnsibleModule(
        argument_spec=dict(
            device_name     = dict(default='mmcblk0'),
        ),
        supports_check_mode=True,
    )

    device_name =  module.params['device_name']
    device_full_path = '/sys/block/{}/size'.format(device_name)
    try:
        with open(device_full_path, 'r') as myfile:
            data=myfile.read()
    except IOError:
        module.fail_json(msg='Failed to read the SD card size from {}'.format(device_full_path))

    result = {}
    result['device_name'] = device_name
    result['size'] = int(data.strip())

    parts = glob.glob('/sys/block/{0}/{0}*'.format(device_name))
    used = 0

    for part in parts:
        try:
            with open(part + '/size' , 'r') as myfile:
                data=myfile.read()
        except IOError:
            module.fail_json(msg='Failed to read the SD card size from {}'.format(device_full_path))
        part_size=int(data.strip())
        used += part_size

    result['used'] = used
    result['per_used'] = int((used * 100) / result['size'])

    changed = False
    if result['per_used'] > 95:
        result['message'] = 'No expand needed, {}% is already used'.format(result['per_used'])
    else:
        changed = True
        if not module.check_mode:
            raspiconfig_result = module.run_command(['/usr/bin/raspi-config', '--expand-rootfs'])
            if raspiconfig_result[0] != 0:
                module.fail_json(msg='raspi-config command returned non-0 exit {}, the output was {}'.format(raspiconfig_result[0], 
                                                                                                raspiconfig_result[1]))
            else:
                result['raspiconfig_result'] = raspiconfig_result[1]

    module.exit_json(changed=changed, result=result)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
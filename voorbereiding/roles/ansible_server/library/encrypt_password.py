#!/usr/bin/python
import crypt

def main():
    module = AnsibleModule(
        argument_spec=dict(
            pwd = dict(no_log=True),
        ),
        supports_check_mode=True,
    )

    result = {}
    result['enc_pwd'] = crypt.crypt(module.params['pwd'], "$1$mySalt$")
    changed=False
    module.exit_json(changed=changed, result=result)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
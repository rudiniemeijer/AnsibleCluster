#!/usr/bin/python
from passlib.hash import sha512_crypt

def main():
    module = AnsibleModule(
        argument_spec=dict(
            pwd     = dict(no_log=True),
        ),
        supports_check_mode=True,
    )

    pwd =  module.params['pwd']

    result = {}
    result['enc_pwd'] = sha512_crypt.using(rounds=5000).hash(pwd)
    changed=True
    module.exit_json(changed=changed, result=result)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
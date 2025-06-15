#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    m = AnsibleModule(argument_spec={'name': {'type': 'str', 'required': True}})
    m.exit_json(changed=False, message=f"Hello, {m.params['name']}!")

if __name__ == '__main__':
    main()
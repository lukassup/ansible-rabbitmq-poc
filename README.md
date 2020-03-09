# RabbitMQ

## Contents

- `playbook.yml` the Ansible playbook itself
- `group_vars` contains playbook values and secrets for Ansible Vault
- `roles/base_setup` role to install some handy utils, such as `git` which is used to clone this repo on target host
- `roles/rabbitmq` role to install and setup RabbitMQ
- `scripts` consumer and producer scripts for testing RabbitMQ

```text
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── ansible.cfg
├── group_vars
│   └── all.yml
├── playbook.yml
├── requirements.dev.txt
├── requirements.txt
├── roles
│   ├── base_setup
│   │   └── tasks
│   │       └── main.yml
│   └── rabbitmq
│       ├── files
│       │   ├── erlang.preferences
│       │   └── rabbitmq.preferences
│       ├── handlers
│       │   └── main.yml
│       ├── tasks
│       │   └── main.yml
│       └── templates
│           └── limits.conf.j2
└── scripts
    ├── consumer.py
    └── producer.py
```

## Setup: Ansible

Run commands in terminal:

1. Install dependencies:

    ```sh
    pip3 install -r requirements.txt -r requirements.dev.txt
    ```

2. Setup `hosts` file for Ansible:

    ```sh
    echo '[all]' > hosts
    echo 'THE_IP_ADDRESS_OF_TARGET_HOST' >> hosts
    ```

3. Run Ansible and provide password for Ansible Vault (the password is: `password`):

    ```sh
    ansible-playbook playbook.yml --ask-vault-pass
    ```

## Setup: test client

Run commands in terminal:

1. Connect to target host:

    ```sh
    ssh TARGET_IP
    ```

2. Clone this repository:

    ```sh
    git clone https://github.com/lukassup/ansible-demo
    cd ansible-demo
    ```

3. Install dependencies for Python client:

    ```sh
    pip3 install -r requirements.txt
    ```

4. Run the consumer script:

    ```sh
    python3 scripts/consumer.py
    ```

5. In another terminal run the producer script:

    ```sh
    python3 scripts/producer.py
    ```

6. Upon successful message delivery producer should read:

    ```text
    root@host:~/ansible-demo# python3 scripts/producer.py
    [x] Sent 'info: Hello World!'
    ```

7. Upon successful message delivery consumer should read:

    ```text
    root@host:~/ansible-demo# python3 scripts/consumer.py
    [*] Waiting for logs. To exit press CTRL+C
    [x] b'info: Hello World!'
    ```

8. Press `Ctrl` + `C` to stop the consumer.

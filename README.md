# Ansible Collection - eingram23.containers

Collection for managing container deployments using Podman and Docker

## Installation

To install this collection:

```bash
ansible-galaxy collection install https://github.com/eingram23/ansible-col-containers.git
```

## Requirements

- Ansible 2.9+
- Podman (or Docker for some roles) installed on target hosts
- systemd for service management

## Roles

### common
Shared tasks for container management:
- Environment setup
- Service configuration
- Container lifecycle management
- Upgrade procedures

### calibre
Deploy Calibre-web e-book server:
- Digital library management
- E-book format conversion
- Web-based reader interface

### dbeaver
Deploy DBeaver database tool:
- Database connection management
- SQL development environment
- Schema browsing and editing

### diversionforum
Deploy Discourse forum platform:
- Community discussion platform
- User management
- Content moderation tools

### prometheus
Deploy and configure Prometheus monitoring server:
- Time series database setup
- Metrics collection
- Alert management configuration

### grafana
Deploy Grafana visualization platform:
- Dashboard management
- Data source configuration
- User authentication setup

### node_exporter
Deploy Prometheus Node Exporter:
- System metrics collection
- Performance monitoring
- Hardware statistics

### alertmanager
Deploy Prometheus Alertmanager:
- Alert routing
- Notification management
- Silencing and inhibition rules

## Usage

### Basic Role Execution

```yaml
- name: Deploy container
  hosts: "{{ hostvar | default([]) }}"
  gather_facts: false
  become: false

  tasks:
    - name: Run role
      ansible.builtin.import_role:
        name: eingram23.containers.{{ role }}
        tasks_from: "{{ task }}"
```

### Configuration Variables

Common variables (may vary by role):
```yaml
# Container settings
app_name: "application"
image: "docker.io/image"
user_account: "poduser"
upgrade: "no"

# Network configuration
fw_port:
  - "port/tcp"
publish_port:
  - "host:container"
```

## Contributing

Contributions are welcome! Please submit pull requests to the project repository.

## License

MIT

## Author

Edward Ingram

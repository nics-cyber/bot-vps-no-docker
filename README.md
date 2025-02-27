

# Discord VPS Management Bot

This bot allows you to manage VPS instances from within Discord. You can create, delete, list, and manage the deployment of services on VPS instances via SSH. The bot uses `paramiko` to execute SSH commands and integrates with Discord using `discord.py`.

## Features
- Create a VPS instance with specified RAM and OS.
- Delete a VPS instance.
- List all VPS instances and their status.
- Deploy services on a VPS.
- Manage services (start, stop, restart) on a VPS.
- Deploy SSH access using `tmate` or `serveo`.
- Renew VPS instances for a specified number of days.

## Requirements
- Python 3.8 or higher
- `discord.py` library
- `paramiko` library
- A VPS with SSH access

## Setup Guide

### 1. Clone the repository (or copy the script)
If this is a standalone script, you can directly copy the code to your project directory.

### 2. Install the required dependencies

To install the required dependencies, run the following command:

```bash
pip install discord.py paramiko
```

### 3. Configure the bot

#### Discord Bot Token:
- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
- Under the "Bot" section, create a bot and copy the `TOKEN`.
- Replace `YOUR_DISCORD_BOT_TOKEN` with your token in the code.

#### SSH Credentials:
- You will need a VPS to manage.
- Replace the following variables with your SSH credentials:
  - `SSH_HOST`: Your VPS's host or IP address.
  - `SSH_PORT`: The SSH port (default is 22).
  - `SSH_USER`: Your SSH username (usually `root` or another user).
  - `SSH_PASSWORD`: Your SSH password for the VPS.

```python
# SSH credentials for the VPS
SSH_HOST = 'your.vps.host'
SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = 'your_password'
```

### 4. Run the bot

To start the bot, simply run the Python script:

```bash
python bot_script.py
```

Replace `bot_script.py` with the filename of your script.

### 5. Invite the Bot to Your Discord Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your application and navigate to the "OAuth2" tab.
3. Under "OAuth2", go to the "URL Generator".
4. Select the `bot` scope and assign necessary permissions (like `Administrator` or specific permissions based on your requirements).
5. Copy the generated URL and visit it to invite the bot to your server.

---

## Usage

Once the bot is running, you can use the following commands in your Discord server:

### **Create a new VPS**
`/create_vps <ram> <os>`
- Example: `/create_vps 4GB Ubuntu`

### **Delete a VPS**
`/delete_vps <vps_id>`
- Example: `/delete_vps vps_1`

### **List all VPS instances**
`/list_vps`

### **Deploy a service on a VPS**
`/deploy_service <vps_id> <service>`
- Example: `/deploy_service vps_1 apache2`

### **Manage a service (start, stop, restart)**
`/manage_service <vps_id> <service> <action>`
- Example: `/manage_service vps_1 apache2 start`

### **Deploy SSH access using tmate or serveo**
`/deploy_ssh <vps_id> <method>`
- Example: `/deploy_ssh vps_1 tmate`
- Example: `/deploy_ssh vps_1 serveo`

### **Renew a VPS**
`/renew_vps <vps_id> <days>`
- Example: `/renew_vps vps_1 30`

---

## Troubleshooting

- **Bot not responding**: Ensure that the bot is correctly added to the server and that your token and permissions are set properly.
- **SSH connection issues**: Double-check that the VPS's IP, SSH port, username, and password are correct.
- **Missing dependencies**: If you see errors about missing libraries, make sure you've installed all required packages using `pip`.

---

## License

This project is open-source and available under the MIT License.

---


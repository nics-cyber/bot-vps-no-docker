

---

### **Step 1: Running the Bot**

1. **Install Dependencies**:
   - Ensure you have Python 3.x installed.
   - Install the required Python libraries:
     ```bash
     pip install discord.py paramiko
     ```

2. **Set Up the Bot**:
   - Replace the placeholders in the script with your actual credentials:
     - `YOUR_DISCORD_BOT_TOKEN`: Your Discord bot token.
     - `your.vps.host`: The hostname or IP address of your VPS.
     - `root`: The SSH username.
     - `your_password`: The SSH password.

3. **Run the Bot**:
   - Save the script as `discord_vps_bot.py`.
   - Run the bot using Python:
     ```bash
     python3 discord_vps_bot.py
     ```

4. **Invite the Bot to Your Server**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Select your bot and generate an invite link with the `applications.commands` and `bot` scopes.
   - Use the link to invite the bot to your server.

---

### **Step 2: Creating a `README.md` File**

A `README.md` file is essential for documenting your project. Below is a template you can use:

```markdown
# Discord VPS Creator Bot

A Discord bot for managing VPS instances, deploying Docker containers, and providing SSH access via tmate or Serveo.

---

## Features

- **VPS Management**:
  - Create, delete, list, start, stop, and restart VPS instances.
  - Customize RAM and OS (supports Debian 12 and Ubuntu 22.04).
- **Docker Deployment**:
  - Deploy Docker containers on VPS instances.
- **SSH Access**:
  - Choose between `tmate` or `serveo.net` for instant SSH access.
- **Renew and Expire System**:
  - Track expiration dates and allow renewals.
- **Slash Commands**:
  - Enhanced user experience with Discord slash commands.

---

## Requirements

- Python 3.x
- Discord bot token
- SSH access to a VPS
- Docker (optional, for container deployment)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/discord-vps-creator.git
   cd discord-vps-creator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Replace placeholders in `discord_vps_bot.py` with your credentials.

4. Run the bot:
   ```bash
   python3 discord_vps_bot.py
   ```

---

## Usage

### Slash Commands

- **Create a VPS**:
  ```
  /create_vps ram:4GB os:ubuntu22.04
  ```

- **Delete a VPS**:
  ```
  /delete_vps vps_id:vps_1
  ```

- **List VPS Instances**:
  ```
  /list_vps
  ```

- **Deploy Docker Container**:
  ```
  /deploy_docker vps_id:vps_1 image:nginx
  ```

- **Manage VPS**:
  ```
  /manage_vps vps_id:vps_1 action:start
  ```

- **Deploy SSH Access**:
  ```
  /deploy_ssh vps_id:vps_1 method:tmate
  ```

- **Renew VPS**:
  ```
  /renew_vps vps_id:vps_1 days:30
  ```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
```

---

### **Step 3: Adding a `requirements.txt` File**

Create a `requirements.txt` file to list the dependencies for your project:

```plaintext
discord.py
paramiko
```

---

### **Step 4: Organizing Your Project**

Your project structure should look like this:

```
discord-vps-creator/
├── discord_vps_bot.py
├── README.md
├── requirements.txt
└── LICENSE (optional)
```

---

### **Step 5: Publishing to GitHub**

1. Create a new repository on GitHub.
2. Push your code to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/discord-vps-creator.git
   git push -u origin main
   ```

3. Share the repository link with others!

---

### **Step 6: Running the Bot in the Background**

To keep the bot running 24/7, you can use a process manager like `pm2` or `systemd`.

#### Using `pm2`:
1. Install `pm2`:
   ```bash
   npm install -g pm2
   ```

2. Start the bot with `pm2`:
   ```bash
   pm2 start discord_vps_bot.py --interpreter python3
   ```

3. Save the process list:
   ```bash
   pm2 save
   ```

#### Using `systemd`:
1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/discord-vps-bot.service
   ```

2. Add the following content:
   ```ini
   [Unit]
   Description=Discord VPS Bot
   After=network.target

   [Service]
   User=your-username
   WorkingDirectory=/path/to/discord-vps-creator
   ExecStart=/usr/bin/python3 /path/to/discord-vps-creator/discord_vps_bot.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable discord-vps-bot
   sudo systemctl start discord-vps-bot
   ```

---

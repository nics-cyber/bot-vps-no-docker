import discord
import paramiko
import asyncio
from datetime import datetime, timedelta
from discord.ext import commands

# Discord bot token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# SSH credentials for the VPS
SSH_HOST = 'your.vps.host'
SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = 'your_password'

# Initialize Discord bot with slash commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to store VPS instances and their details
vps_instances = {}

# Function to execute SSH commands
def execute_ssh_command(command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASSWORD)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Error: {str(e)}"

# Slash command to create a VPS
@bot.tree.command(name="create_vps", description="Create a new VPS instance")
async def create_vps(interaction: discord.Interaction, ram: str, os: str):
    vps_id = f"vps_{len(vps_instances) + 1}"
    vps_instances[vps_id] = {
        "ram": ram,
        "os": os,
        "status": "running",
        "expiration": datetime.now() + timedelta(days=30),  # Default expiration: 30 days
    }
    await interaction.response.send_message(f"VPS {vps_id} created with {ram} RAM and {os} OS.")

# Slash command to delete a VPS
@bot.tree.command(name="delete_vps", description="Delete a VPS instance")
async def delete_vps(interaction: discord.Interaction, vps_id: str):
    if vps_id in vps_instances:
        del vps_instances[vps_id]
        await interaction.response.send_message(f"VPS {vps_id} deleted.")
    else:
        await interaction.response.send_message(f"VPS {vps_id} not found.")

# Slash command to list VPS instances
@bot.tree.command(name="list_vps", description="List all VPS instances")
async def list_vps(interaction: discord.Interaction):
    if vps_instances:
        response = "VPS Instances:\n"
        for vps_id, details in vps_instances.items():
            response += f"{vps_id}: {details['ram']} RAM, {details['os']} OS, Status: {details['status']}, Expires: {details['expiration']}\n"
        await interaction.response.send_message(response)
    else:
        await interaction.response.send_message("No VPS instances found.")

# Slash command to deploy a service
@bot.tree.command(name="deploy_service", description="Deploy a service on a VPS")
async def deploy_service(interaction: discord.Interaction, vps_id: str, service: str):
    if vps_id in vps_instances:
        command = f"nohup {service} &"  # Run the service in the background
        output = execute_ssh_command(command)
        await interaction.response.send_message(f"Service deployed on {vps_id}:\n{output}")
    else:
        await interaction.response.send_message(f"VPS {vps_id} not found.")

# Slash command to start/stop/restart a service
@bot.tree.command(name="manage_service", description="Start, stop, or restart a service")
async def manage_service(interaction: discord.Interaction, vps_id: str, service: str, action: str):
    if vps_id in vps_instances:
        if action in ["start", "stop", "restart"]:
            if action == "stop":
                command = f"pkill -f '{service}'"  # Stop the service
            else:
                command = f"nohup {service} &"  # Start or restart the service
            output = execute_ssh_command(command)
            await interaction.response.send_message(f"Service {service} {action}ed on {vps_id}:\n{output}")
        else:
            await interaction.response.send_message("Invalid action. Use 'start', 'stop', or 'restart'.")
    else:
        await interaction.response.send_message(f"VPS {vps_id} not found.")

# Slash command to deploy SSH access (tmate or serveo)
@bot.tree.command(name="deploy_ssh", description="Deploy SSH access using tmate or serveo")
async def deploy_ssh(interaction: discord.Interaction, vps_id: str, method: str):
    if vps_id in vps_instances:
        if method == "tmate":
            command = "tmate"
            output = execute_ssh_command(command)
            await interaction.response.send_message(f"tmate session started on {vps_id}:\n{output}")
        elif method == "serveo":
            command = "ssh -R $HOSTNAME:22:localhost:22 serveo.net"
            output = execute_ssh_command(command)
            await interaction.response.send_message(f"Serveo session started on {vps_id}:\n{output}")
        else:
            await interaction.response.send_message("Invalid method. Use 'tmate' or 'serveo'.")
    else:
        await interaction.response.send_message(f"VPS {vps_id} not found.")

# Slash command to renew VPS
@bot.tree.command(name="renew_vps", description="Renew a VPS instance")
async def renew_vps(interaction: discord.Interaction, vps_id: str, days: int):
    if vps_id in vps_instances:
        vps_instances[vps_id]["expiration"] = datetime.now() + timedelta(days=days)
        await interaction.response.send_message(f"VPS {vps_id} renewed for {days} days.")
    else:
        await interaction.response.send_message(f"VPS {vps_id} not found.")

# Run the bot
bot.run(TOKEN)
# Run the bot
bot.run(TOKEN)

#!/usr/bin/python3
"""
Module loading variables from config file
"""
import configparser

CONFIG_PATH = "config"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)
#path configurations
MotPath = config["PATH"]["motpath"]
LogPath = config["PATH"]["logpath"]
#discord configurations
SuccessLink = config["DISCORD"]["successlink"]
ErrorLink = config["DISCORD"]["errorlink"]
discord_enabled = config["DISCORD"]["enabled"]
#base settings
FidelityLink = config["SETTINGS"]["FidelityLink"]
embeds = config["SETTINGS"]["embeds"] == "True" #print new point value in an embed
Headless = config["SETTINGS"]["headless"] == "True"
#proxy settings
proxy_enabled = config["PROXY"]["enabled"] == "True"
proxy_address = config["PROXY"]["url"]
proxy_port = config["PROXY"]["port"]
#MySQL settings
sql_enabled = config["SQL"]["enabled"] == "True"
sql_usr = config["SQL"]["usr"]
sql_pwd = config["SQL"]["pwd"]
sql_host = config["SQL"]["host"]
sql_database = config["SQL"]["database"]
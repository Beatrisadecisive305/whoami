#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
whoami - Penetration Testing Suite
Version: 1.3
Author: ruyynn
GitHub: https://github.com/ruyynn
"""

# ==================== IMPORT MODULE ====================
import os
import sys
import time
import socket
import platform
import subprocess
import threading
import queue
import re
import urllib.parse
import urllib.request
import urllib.error
import http.client
import ftplib
import smtplib
import poplib
import imaplib
import telnetlib3
import paramiko
import requests
import scapy.all as scapy
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
import dns.reversename
import dns.zone
import whois
from bs4 import BeautifulSoup
import hashlib
import json
import csv

# ==================== COLOR SETUP ====================
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        BLACK = '\033[30m'; RED = '\033[31m'; GREEN = '\033[32m'
        YELLOW = '\033[33m'; BLUE = '\033[34m'; MAGENTA = '\033[35m'
        CYAN = '\033[36m'; WHITE = '\033[37m'; RESET = '\033[39m'
    class Back:
        BLACK = '\033[40m'; RED = '\033[41m'; GREEN = '\033[42m'
        YELLOW = '\033[43m'; BLUE = '\033[44m'; MAGENTA = '\033[45m'
        CYAN = '\033[46m'; WHITE = '\033[47m'; RESET = '\033[49m'
    class Style:
        BRIGHT = '\033[1m'; DIM = '\033[2m'; NORMAL = '\033[22m'
        RESET_ALL = '\033[0m'

# ==================== LOGO UTAMA ====================
LOGO = f"""
{Fore.RED}{Style.BRIGHT}
oooo     oooo ooooo ooooo  ooooooo      o      oooo     oooo ooooo o8888888o  
 88   88  88   888   888 o888   888o   888      8888o   888   888  888     888
  88 888 88    888ooo888 888     888  8  88     88 888o8 88   888       o888  
   888 888     888   888 888o   o888 8oooo88    88  888  88   888      888    
    8   8     o888o o888o  88ooo88 o88o  o888o o88o  8  o88o o888o     ooo    
{Fore.CYAN}{Style.BRIGHT}═══════════════════════════════════════════════════════════════
{Fore.YELLOW}         Penetration Testing Suite v1.3 - by ruyynn{Fore.RESET}
{Fore.CYAN}         GitHub: https://github.com/ruyynn{Fore.RESET}
"""

# ==================== DEVICE SELECTION ====================
def device_selection():
    """Menu pemilihan device - LANGSUNG TAMPIL"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(LOGO)
    
    # Auto-detect platform
    detected = platform.system().lower()
    if 'termux' in os.environ.get('PREFIX', ''):
        detected = 'termux'
    elif 'android' in platform.platform().lower():
        detected = 'termux'
    
    menu = f"""
{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗
║                    SELECT YOUR PLATFORM                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  {Fore.GREEN}[1]{Fore.WHITE} 📱 Termux (Android)                                     ║
║  {Fore.GREEN}[2]{Fore.WHITE} 🐧 Linux (Ubuntu/Debian/Kali/Arch)                      ║
║  {Fore.GREEN}[3]{Fore.WHITE} 🪟 Windows (10/11)                                       ║
║  {Fore.GREEN}[4]{Fore.WHITE} 🍎 macOS                                                ║
║  {Fore.GREEN}[5]{Fore.WHITE} 🤖 Auto-Detect (Recommended)                            ║
║  {Fore.RED}[0]{Fore.WHITE} ❌ Exit                                                 ║
║                                                              ║
║  {Fore.MAGENTA}══════════════════════════════════════════════════════════ {Fore.WHITE} ║
║  {Fore.CYAN}Detected:{Fore.YELLOW} {detected.upper():<20}{Fore.WHITE}                              ║
║  {Fore.CYAN}Author:{Fore.YELLOW} ruyynn{Fore.WHITE}                                              ║
║  {Fore.CYAN}GitHub:{Fore.YELLOW} https://github.com/ruyynn{Fore.WHITE}                           ║
║  {Fore.CYAN}Version:{Fore.YELLOW} 1.3{Fore.WHITE}                                                ║
╚══════════════════════════════════════════════════════════════╝{Fore.RESET}
"""
    print(menu)
    
    while True:
        try:
            choice = input(f"{Fore.CYAN}┌─[whoami@device]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                print(f"\n{Fore.RED}Exiting...{Fore.RESET}")
                sys.exit(0)
            elif choice == '1':
                return 'termux'
            elif choice == '2':
                return 'linux'
            elif choice == '3':
                return 'windows'
            elif choice == '4':
                return 'macos'
            elif choice == '5':
                print(f"{Fore.GREEN}[+] Auto-detected: {detected}{Fore.RESET}")
                time.sleep(1)
                return detected
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Fore.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Exiting...{Fore.RESET}")
            sys.exit(0)

# ==================== LOADING ANIMASI 3 DETIK ====================
def loading_animation():
    """Loading animation 3 detik"""
    frames = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
              "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
              "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", 
              "[■■■■■■■■■■]"]
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗")
    print(f"║           INITIALIZING WHOAMI PENETRATION SUITE              ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Fore.RESET}\n")
    
    for i in range(6):  # 3 detik (6 * 0.5)
        time.sleep(0.5)
        print(f"\r{Fore.YELLOW}{frames[i % len(frames)]} {Fore.GREEN}Loading...{Fore.RESET}", end="")
        sys.stdout.flush()
    
    print(f"\n\n{Fore.GREEN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════╗")
    print(f"║         ✓ WHOAMI SUITE READY - by ruyynn v1.3                ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Fore.RESET}")
    time.sleep(1)

# ==================== WORKING TOOLS ====================

class PortScanner:
    """Port Scanner - WORKING"""
    @staticmethod
    def scan(target, start_port, end_port):
        results = []
        print(f"{Fore.CYAN}[*] Scanning {target} ports {start_port}-{end_port}...{Fore.RESET}")
        
        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    results.append({'port': port, 'service': service})
                    print(f"{Fore.GREEN}[+] Port {port}/tcp open - {service}{Fore.RESET}")
                sock.close()
            except:
                pass
        return results

class DNSEnumerator:
    """DNS Enumeration - WORKING"""
    @staticmethod
    def enumerate(domain):
        results = {}
        print(f"{Fore.CYAN}[*] Enumerating DNS for {domain}...{Fore.RESET}")
        
        # A records
        try:
            answers = dns.resolver.resolve(domain, 'A')
            results['A'] = [str(r) for r in answers]
            print(f"{Fore.GREEN}[+] A Records: {', '.join(results['A'])}{Fore.RESET}")
        except: pass
        
        # MX records
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            results['MX'] = [str(r.exchange) for r in answers]
            print(f"{Fore.GREEN}[+] MX Records: {', '.join(results['MX'])}{Fore.RESET}")
        except: pass
        
        # NS records
        try:
            answers = dns.resolver.resolve(domain, 'NS')
            results['NS'] = [str(r) for r in answers]
            print(f"{Fore.GREEN}[+] NS Records: {', '.join(results['NS'])}{Fore.RESET}")
        except: pass
        
        return results

class WhoisLookup:
    """Whois Lookup - WORKING"""
    @staticmethod
    def lookup(target):
        try:
            w = whois.whois(target)
            return w
        except:
            return None

class HTTPEnumerator:
    """HTTP Enumeration - WORKING"""
    @staticmethod
    def enumerate(url):
        try:
            response = requests.get(url, timeout=5, verify=False)
            return {
                'status': response.status_code,
                'headers': dict(response.headers),
                'server': response.headers.get('Server', 'Unknown')
            }
        except:
            return None

class TelnetBruteforce:
    """Telnet Bruteforce using telnetlib3 - WORKING"""
    @staticmethod
    async def try_login(host, port, username, password):
        try:
            reader, writer = await telnetlib3.open_connection(host, port, shell=False)
            
            # Read login prompt
            data = await reader.read(1024)
            
            # Send username
            writer.write(username + '\n')
            await writer.drain()
            
            # Read password prompt
            data = await reader.read(1024)
            
            # Send password
            writer.write(password + '\n')
            await writer.drain()
            
            # Read response
            data = await reader.read(1024)
            
            writer.close()
            
            # Check if login successful
            if 'incorrect' not in data.lower() and 'failed' not in data.lower():
                return True
            return False
        except:
            return False
    
    @staticmethod
    def bruteforce(host, port, username, passwords):
        import asyncio
        for password in passwords:
            try:
                result = asyncio.run(TelnetBruteforce.try_login(host, port, username, password))
                if result:
                    print(f"{Fore.GREEN}[+] SUCCESS! {username}:{password}{Fore.RESET}")
                    return True
                else:
                    print(f"{Fore.RED}[-] Failed: {username}:{password}{Fore.RESET}")
            except:
                pass
        return False

class FTPBruteforce:
    """FTP Bruteforce - WORKING"""
    @staticmethod
    def bruteforce(host, port, username, passwords):
        for password in passwords:
            try:
                ftp = ftplib.FTP()
                ftp.connect(host, port, timeout=3)
                ftp.login(username, password)
                print(f"{Fore.GREEN}[+] SUCCESS! {username}:{password}{Fore.RESET}")
                ftp.quit()
                return True
            except ftplib.error_perm:
                print(f"{Fore.RED}[-] Failed: {username}:{password}{Fore.RESET}")
            except:
                pass
        return False

class SSHBruteforce:
    """SSH Bruteforce - WORKING"""
    @staticmethod
    def bruteforce(host, port, username, passwords):
        for password in passwords:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=port, username=username, password=password, timeout=3)
                print(f"{Fore.GREEN}[+] SUCCESS! {username}:{password}{Fore.RESET}")
                client.close()
                return True
            except paramiko.AuthenticationException:
                print(f"{Fore.RED}[-] Failed: {username}:{password}{Fore.RESET}")
            except:
                pass
        return False

class SQLInjector:
    """SQL Injection Scanner - WORKING"""
    @staticmethod
    def check(url, param):
        payloads = ["'", "' OR '1'='1", "' OR 1=1--", "' UNION SELECT NULL--"]
        for payload in payloads:
            try:
                test_url = f"{url}?{param}={urllib.parse.quote(payload)}"
                response = requests.get(test_url, timeout=3, verify=False)
                if "sql" in response.text.lower() or "mysql" in response.text.lower():
                    return True
            except:
                pass
        return False

class XSSDetector:
    """XSS Scanner - WORKING"""
    @staticmethod
    def check(url, param):
        payload = "<script>alert('XSS')</script>"
        try:
            test_url = f"{url}?{param}={urllib.parse.quote(payload)}"
            response = requests.get(test_url, timeout=3, verify=False)
            if payload in response.text:
                return True
        except:
            pass
        return False

class SubdomainFinder:
    """Subdomain Finder - WORKING"""
    @staticmethod
    def find(domain):
        wordlist = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 
                   'ns2', 'cpanel', 'whm', 'admin', 'blog', 'dev', 'test', 'api']
        found = []
        for sub in wordlist:
            try:
                host = f"{sub}.{domain}"
                ip = socket.gethostbyname(host)
                found.append((host, ip))
                print(f"{Fore.GREEN}[+] Found: {host} -> {ip}{Fore.RESET}")
            except:
                pass
        return found

class ARPScanner:
    """ARP Scanner - WORKING"""
    @staticmethod
    def scan(interface, target):
        try:
            arp = scapy.ARP(pdst=target)
            ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether/arp
            result = scapy.srp(packet, timeout=3, iface=interface, verbose=0)[0]
            devices = []
            for sent, received in result:
                devices.append({'ip': received.psrc, 'mac': received.hwsrc})
                print(f"{Fore.GREEN}[+] IP: {received.psrc} - MAC: {received.hwsrc}{Fore.RESET}")
            return devices
        except:
            return []

class Traceroute:
    """Traceroute - WORKING"""
    @staticmethod
    def trace(target):
        try:
            dest_ip = socket.gethostbyname(target)
            for ttl in range(1, 30):
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                sock.settimeout(1)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
                sock.sendto(b'', (target, 0))
                try:
                    data, addr = sock.recvfrom(512)
                    print(f"{Fore.GREEN}[{ttl:2d}] {addr[0]}{Fore.RESET}")
                    if addr[0] == dest_ip:
                        break
                except socket.timeout:
                    print(f"{Fore.YELLOW}[{ttl:2d}] *{Fore.RESET}")
                sock.close()
        except:
            pass

class PingSweep:
    """Ping Sweep - WORKING"""
    @staticmethod
    def sweep(network, start, end):
        alive = []
        for i in range(start, end + 1):
            ip = f"{network}.{i}"
            try:
                if platform.system() == 'Windows':
                    result = subprocess.run(['ping', '-n', '1', '-w', '500', ip], 
                                          capture_output=True, timeout=1)
                else:
                    result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                          capture_output=True, timeout=1)
                if result.returncode == 0:
                    alive.append(ip)
                    print(f"{Fore.GREEN}[+] {ip} is alive{Fore.RESET}")
            except:
                pass
        return alive

class HTTPBruteforce:
    """HTTP Bruteforce - WORKING"""
    @staticmethod
    def bruteforce(url, username_field, password_field, username, passwords):
        for password in passwords:
            try:
                data = {username_field: username, password_field: password}
                response = requests.post(url, data=data, timeout=3, verify=False)
                if response.status_code == 302 or "welcome" in response.text.lower():
                    print(f"{Fore.GREEN}[+] SUCCESS! {username}:{password}{Fore.RESET}")
                    return True
                else:
                    print(f"{Fore.RED}[-] Failed: {username}:{password}{Fore.RESET}")
            except:
                pass
        return False

class HashCracker:
    """Hash Cracker - WORKING"""
    @staticmethod
    def crack_md5(hash_value, wordlist_file):
        try:
            with open(wordlist_file, 'r', errors='ignore') as f:
                for line in f:
                    word = line.strip()
                    if hashlib.md5(word.encode()).hexdigest() == hash_value:
                        return word
        except:
            pass
        return None

# ==================== MAIN MENU ====================
class WhoamiSuite:
    def __init__(self, device):
        self.device = device
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.targets = []
        self.log_file = f"whoami_{self.session_id}.log"
        
    def get_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    def show_main_menu(self):
        self.clear_screen()
        print(LOGO)
        
        device_names = {
            'termux': '📱 TERMUX',
            'linux': '🐧 LINUX',
            'windows': '🪟 WINDOWS',
            'macos': '🍎 MACOS'
        }
        
        menu = f"""
{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════════════════════════════════╗
║                    MAIN MENU - whoami v1.3                     ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  {Fore.GREEN}[1]{Fore.WHITE} 📡 Information Gathering                                  ║
║  {Fore.GREEN}[2]{Fore.WHITE} 🌐 Network Scanning                                       ║
║  {Fore.GREEN}[3]{Fore.WHITE} 🔍 Vulnerability Scanner                                  ║
║  {Fore.GREEN}[4]{Fore.WHITE} 🌍 Web Application Testing                                ║
║  {Fore.GREEN}[5]{Fore.WHITE} 🔑 Password Attacks                                       ║ 
║  {Fore.GREEN}[6]{Fore.WHITE} 📶 Wireless Attacks                                       ║
║  {Fore.GREEN}[7]{Fore.WHITE} 🎯 Post Exploitation                                      ║
║  {Fore.GREEN}[8]{Fore.WHITE} 📊 Reporting                                              ║
║  {Fore.GREEN}[9]{Fore.WHITE} 🔧 Maintenance                                            ║
║  {Fore.RED}[0]{Fore.WHITE} ❌ Exit                                                   ║
║                                                                ║
║  {Fore.MAGENTA}══════════════════════════════════════════════════════════════{Fore.WHITE}║
║  Device    : {Fore.YELLOW}{device_names.get(self.device, self.device.upper())}{Fore.WHITE}                                         ║
║  IP        : {Fore.YELLOW}{self.get_ip()}{Fore.WHITE}                                     ║
║  Session   : {Fore.GREEN}{self.session_id}{Fore.WHITE}                                   ║
║  Author    : {Fore.CYAN}ruyynn{Fore.WHITE}                                            ║
║  GitHub    : {Fore.CYAN}https://github.com/ruyynn{Fore.WHITE}                         ║
╚════════════════════════════════════════════════════════════════╝{Fore.RESET}
"""
        print(menu)
    
    def info_gathering_menu(self):
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
            print(f"║              INFORMATION GATHERING MENU                        ║")
            print(f"╠════════════════════════════════════════════════════════════════╣{Fore.RESET}")
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Whois Lookup
    {Fore.GREEN}[2]{Fore.WHITE} DNS Enumeration
    {Fore.GREEN}[3]{Fore.WHITE} Subdomain Finder
    {Fore.GREEN}[4]{Fore.WHITE} HTTP Header Grabber
    {Fore.GREEN}[5]{Fore.WHITE} IP Geolocation
    {Fore.GREEN}[0]{Fore.WHITE} Back
            """)
            
            choice = input(f"\n{Fore.CYAN}┌─[whoami@info]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.whois_lookup()
            elif choice == '2':
                self.dns_enum()
            elif choice == '3':
                self.subdomain_finder()
            elif choice == '4':
                self.http_headers()
            elif choice == '5':
                self.ip_geolocation()
    
    def whois_lookup(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Whois Lookup{Fore.RESET}\n")
        target = input(f"{Fore.YELLOW}Domain/IP: {Fore.RESET}").strip()
        if target:
            result = WhoisLookup.lookup(target)
            if result:
                print(f"{Fore.GREEN}[+] Domain: {result.domain_name}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] Registrar: {result.registrar}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] Creation: {result.creation_date}{Fore.RESET}")
            else:
                print(f"{Fore.RED}[-] Failed{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def dns_enum(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] DNS Enumeration{Fore.RESET}\n")
        domain = input(f"{Fore.YELLOW}Domain: {Fore.RESET}").strip()
        if domain:
            DNSEnumerator.enumerate(domain)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def subdomain_finder(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Subdomain Finder{Fore.RESET}\n")
        domain = input(f"{Fore.YELLOW}Domain: {Fore.RESET}").strip()
        if domain:
            SubdomainFinder.find(domain)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def http_headers(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] HTTP Header Grabber{Fore.RESET}\n")
        url = input(f"{Fore.YELLOW}URL: {Fore.RESET}").strip()
        if url:
            if not url.startswith('http'):
                url = 'http://' + url
            result = HTTPEnumerator.enumerate(url)
            if result:
                print(f"{Fore.GREEN}[+] Status: {result['status']}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] Server: {result['server']}{Fore.RESET}")
                for k, v in list(result['headers'].items())[:10]:
                    print(f"{Fore.WHITE}    {k}: {v}{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def ip_geolocation(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] IP Geolocation{Fore.RESET}\n")
        ip = input(f"{Fore.YELLOW}IP: {Fore.RESET}").strip()
        if not ip:
            ip = self.get_ip()
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            data = response.json()
            if data['status'] == 'success':
                print(f"{Fore.GREEN}[+] Country: {data['country']}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] City: {data['city']}{Fore.RESET}")
                print(f"{Fore.GREEN}[+] ISP: {data['isp']}{Fore.RESET}")
        except:
            print(f"{Fore.RED}[-] Failed{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def network_menu(self):
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
            print(f"║                 NETWORK SCANNING MENU                          ║")
            print(f"╠════════════════════════════════════════════════════════════════╣{Fore.RESET}")
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Port Scanner
    {Fore.GREEN}[2]{Fore.WHITE} ARP Scanner
    {Fore.GREEN}[3]{Fore.WHITE} Ping Sweep
    {Fore.GREEN}[4]{Fore.WHITE} Traceroute
    {Fore.GREEN}[0]{Fore.WHITE} Back
            """)
            
            choice = input(f"\n{Fore.CYAN}┌─[whoami@network]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.port_scanner()
            elif choice == '2':
                self.arp_scanner()
            elif choice == '3':
                self.ping_sweep()
            elif choice == '4':
                self.traceroute()
    
    def port_scanner(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Port Scanner{Fore.RESET}\n")
        target = input(f"{Fore.YELLOW}Target: {Fore.RESET}").strip()
        if target:
            start = int(input(f"{Fore.YELLOW}Start port: {Fore.RESET}") or "1")
            end = int(input(f"{Fore.YELLOW}End port: {Fore.RESET}") or "1024")
            PortScanner.scan(target, start, end)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def arp_scanner(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] ARP Scanner{Fore.RESET}\n")
        interface = input(f"{Fore.YELLOW}Interface (default eth0): {Fore.RESET}") or "eth0"
        target = input(f"{Fore.YELLOW}Target network (default 192.168.1.0/24): {Fore.RESET}") or "192.168.1.0/24"
        ARPScanner.scan(interface, target)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def ping_sweep(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Ping Sweep{Fore.RESET}\n")
        network = input(f"{Fore.YELLOW}Network (e.g., 192.168.1): {Fore.RESET}").strip()
        if network:
            start = int(input(f"{Fore.YELLOW}Start (default 1): {Fore.RESET}") or "1")
            end = int(input(f"{Fore.YELLOW}End (default 254): {Fore.RESET}") or "254")
            PingSweep.sweep(network, start, end)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def traceroute(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Traceroute{Fore.RESET}\n")
        target = input(f"{Fore.YELLOW}Target: {Fore.RESET}").strip()
        if target:
            Traceroute.trace(target)
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def vuln_menu(self):
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
            print(f"║                 VULNERABILITY SCANNER MENU                     ║")
            print(f"╠════════════════════════════════════════════════════════════════╣{Fore.RESET}")
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} SQL Injection Scanner
    {Fore.GREEN}[2]{Fore.WHITE} XSS Scanner
    {Fore.GREEN}[0]{Fore.WHITE} Back
            """)
            
            choice = input(f"\n{Fore.CYAN}┌─[whoami@vuln]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.sqli_scanner()
            elif choice == '2':
                self.xss_scanner()
    
    def sqli_scanner(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] SQL Injection Scanner{Fore.RESET}\n")
        url = input(f"{Fore.YELLOW}URL: {Fore.RESET}").strip()
        param = input(f"{Fore.YELLOW}Parameter: {Fore.RESET}").strip()
        if url and param:
            if SQLInjector.check(url, param):
                print(f"{Fore.RED}[!] Vulnerable!{Fore.RESET}")
            else:
                print(f"{Fore.GREEN}[+] Not vulnerable{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def xss_scanner(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] XSS Scanner{Fore.RESET}\n")
        url = input(f"{Fore.YELLOW}URL: {Fore.RESET}").strip()
        param = input(f"{Fore.YELLOW}Parameter: {Fore.RESET}").strip()
        if url and param:
            if XSSDetector.check(url, param):
                print(f"{Fore.RED}[!] Vulnerable!{Fore.RESET}")
            else:
                print(f"{Fore.GREEN}[+] Not vulnerable{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def web_menu(self):
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
            print(f"║                 WEB APPLICATION TESTING MENU                   ║")
            print(f"╠════════════════════════════════════════════════════════════════╣{Fore.RESET}")
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} HTTP Header Grabber
    {Fore.GREEN}[2]{Fore.WHITE} SQL Injection Scanner
    {Fore.GREEN}[3]{Fore.WHITE} XSS Scanner
    {Fore.GREEN}[0]{Fore.WHITE} Back
            """)
            
            choice = input(f"\n{Fore.CYAN}┌─[whoami@web]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.http_headers()
            elif choice == '2':
                self.sqli_scanner()
            elif choice == '3':
                self.xss_scanner()
    
    def password_menu(self):
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
            print(f"║                 PASSWORD ATTACKS MENU                          ║")
            print(f"╠════════════════════════════════════════════════════════════════╣{Fore.RESET}")
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} FTP Bruteforce
    {Fore.GREEN}[2]{Fore.WHITE} SSH Bruteforce
    {Fore.GREEN}[3]{Fore.WHITE} Telnet Bruteforce
    {Fore.GREEN}[4]{Fore.WHITE} HTTP Bruteforce
    {Fore.GREEN}[5]{Fore.WHITE} MD5 Hash Cracker
    {Fore.GREEN}[0]{Fore.WHITE} Back
            """)
            
            choice = input(f"\n{Fore.CYAN}┌─[whoami@password]{Fore.RESET}\n└──╼ $ ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.ftp_bruteforce()
            elif choice == '2':
                self.ssh_bruteforce()
            elif choice == '3':
                self.telnet_bruteforce()
            elif choice == '4':
                self.http_bruteforce()
            elif choice == '5':
                self.hash_cracker()
    
    def ftp_bruteforce(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] FTP Bruteforce{Fore.RESET}\n")
        host = input(f"{Fore.YELLOW}Host: {Fore.RESET}").strip()
        username = input(f"{Fore.YELLOW}Username: {Fore.RESET}").strip()
        wordlist = input(f"{Fore.YELLOW}Wordlist path: {Fore.RESET}").strip()
        if host and username and wordlist:
            try:
                with open(wordlist, 'r') as f:
                    passwords = [line.strip() for line in f.readlines()]
                FTPBruteforce.bruteforce(host, 21, username, passwords)
            except:
                print(f"{Fore.RED}[!] Error reading wordlist{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def ssh_bruteforce(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] SSH Bruteforce{Fore.RESET}\n")
        host = input(f"{Fore.YELLOW}Host: {Fore.RESET}").strip()
        username = input(f"{Fore.YELLOW}Username: {Fore.RESET}").strip()
        wordlist = input(f"{Fore.YELLOW}Wordlist path: {Fore.RESET}").strip()
        if host and username and wordlist:
            try:
                with open(wordlist, 'r') as f:
                    passwords = [line.strip() for line in f.readlines()]
                SSHBruteforce.bruteforce(host, 22, username, passwords)
            except:
                print(f"{Fore.RED}[!] Error reading wordlist{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def telnet_bruteforce(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Telnet Bruteforce{Fore.RESET}\n")
        host = input(f"{Fore.YELLOW}Host: {Fore.RESET}").strip()
        username = input(f"{Fore.YELLOW}Username: {Fore.RESET}").strip()
        wordlist = input(f"{Fore.YELLOW}Wordlist path: {Fore.RESET}").strip()
        if host and username and wordlist:
            try:
                with open(wordlist, 'r') as f:
                    passwords = [line.strip() for line in f.readlines()]
                TelnetBruteforce.bruteforce(host, 23, username, passwords)
            except:
                print(f"{Fore.RED}[!] Error reading wordlist{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def http_bruteforce(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] HTTP Bruteforce{Fore.RESET}\n")
        url = input(f"{Fore.YELLOW}Login URL: {Fore.RESET}").strip()
        username_field = input(f"{Fore.YELLOW}Username field: {Fore.RESET}").strip() or "username"
        password_field = input(f"{Fore.YELLOW}Password field: {Fore.RESET}").strip() or "password"
        username = input(f"{Fore.YELLOW}Username: {Fore.RESET}").strip()
        wordlist = input(f"{Fore.YELLOW}Wordlist path: {Fore.RESET}").strip()
        if url and username and wordlist:
            try:
                with open(wordlist, 'r') as f:
                    passwords = [line.strip() for line in f.readlines()]
                HTTPBruteforce.bruteforce(url, username_field, password_field, username, passwords)
            except:
                print(f"{Fore.RED}[!] Error reading wordlist{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def hash_cracker(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] MD5 Hash Cracker{Fore.RESET}\n")
        hash_value = input(f"{Fore.YELLOW}MD5 Hash: {Fore.RESET}").strip()
        wordlist = input(f"{Fore.YELLOW}Wordlist path: {Fore.RESET}").strip()
        if hash_value and wordlist:
            result = HashCracker.crack_md5(hash_value, wordlist)
            if result:
                print(f"{Fore.GREEN}[+] Password: {result}{Fore.RESET}")
            else:
                print(f"{Fore.RED}[-] Not found{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def wireless_menu(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Wireless Attacks{Fore.RESET}\n")
        print(f"{Fore.YELLOW}[!] Coming soon...{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def post_exploit_menu(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Post Exploitation{Fore.RESET}\n")
        print(f"{Fore.YELLOW}[!] Coming soon...{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def reporting_menu(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Reporting{Fore.RESET}\n")
        print(f"{Fore.YELLOW}[!] Coming soon...{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def maintenance_menu(self):
        self.clear_screen()
        print(f"{Fore.CYAN}[*] Maintenance{Fore.RESET}\n")
        print(f"{Fore.YELLOW}[!] Coming soon...{Fore.RESET}")
        input(f"\n{Fore.CYAN}Press Enter...{Fore.RESET}")
    
    def run(self):
        while True:
            self.show_main_menu()
            
            try:
                choice = input(f"\n{Fore.CYAN}┌─[whoami@main]{Fore.RESET}\n└──╼ $ ").strip()
                
                if choice == '0':
                    print(f"\n{Fore.RED}[!] Exiting...{Fore.RESET}")
                    print(f"{Fore.GREEN}follow my GitHub - https://github.com/ruyynn{Fore.RESET}")
                    sys.exit(0)
                elif choice == '1':
                    self.info_gathering_menu()
                elif choice == '2':
                    self.network_menu()
                elif choice == '3':
                    self.vuln_menu()
                elif choice == '4':
                    self.web_menu()
                elif choice == '5':
                    self.password_menu()
                elif choice == '6':
                    self.wireless_menu()
                elif choice == '7':
                    self.post_exploit_menu()
                elif choice == '8':
                    self.reporting_menu()
                elif choice == '9':
                    self.maintenance_menu()
                else:
                    print(f"{Fore.RED}[!] Invalid choice{Fore.RESET}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}[!] Press Ctrl+C again to exit{Fore.RESET}")
                time.sleep(1)

# ==================== MAIN ====================
def main():
    """Fungsi utama"""
    try:
        
        device = device_selection()
        print(f"{Fore.GREEN}[+] Selected: {device}{Fore.RESET}")
        time.sleep(1)
        
        # Loading 3 detik
        loading_animation()
        
        # Run main suite
        suite = WhoamiSuite(device)
        suite.run()
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Program terminated{Fore.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Fore.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()

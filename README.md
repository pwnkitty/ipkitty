# ipkitty
Auto IP Changer with Tor Service

```markdown
# Auto IP Changer with Tor Service Checker

This Python script provides an automated solution for changing your IP address while ensuring the Tor service is running. It utilizes the Tor network via SOCKS5 proxy for IP changes and includes a built-in checker to verify the Tor service status.




## Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pwnkitty/ipkitty
   ```

2. **Navigate to the Directory:**
   ```bash
   cd ipkitty
   ```

3. **Install Dependencies:**
   Ensure you have Python installed. If not, install it using your package manager:
   ```bash
   # For Debian/Ubuntu
   sudo apt-get install python3
   
   # For Arch Linux
   sudo pacman -S python
   
   # For Termux (Android)
   pkg install python
   ```

4. **Run the Script:**
   ```bash
   python3 ipkitty.py
   ```
   Follow the on-screen prompts to set the interval for IP changes.

## Usage

- **Linux:**
  ```bash
  python3 ipkitty.py
  ```

- **Termux (Android):**
  ```bash
  pkg install git python
  git clone https://github.com/pwnkitty/ipkitty
  cd ipkitty
  python3 ipkitty.py
  ```

- **Debian/Ubuntu:**
  ```bash
  sudo apt-get install git python3
  git clone https://github.com/pwnkitty/ipkitty
  cd ipkitty
  python3 ipkitty.py
  ```

- **Arch Linux:**
  ```bash
  sudo pacman -S git python
  git clone https://github.com/pwnkitty/ipkitty
  cd ipkitty
  python3 ipkitty.py
  ```

# Honeypot Project

## Overview
The Honeypot Project is a security tool designed to simulate vulnerable systems and attract malicious activity. It enables monitoring, logging, and analyzing unauthorized access attempts, providing insights into potential threats.

---

## Features
- **Traffic Logging**: Tracks unauthorized login attempts and network activity.
- **Configurable Settings**: Customizable honeypot behavior through the `config.json` file.
- **Response Handling**: Predefined responses to simulate real-world systems.
- **Detailed Logs**: Comprehensive logs stored in `honeypot_log.txt` for analysis.

---

## Folder Structure
```
Honeypot_project/
├── logs/
│   └── honeypot_log.txt          # Log file containing captured activity
├── src/
│   ├── config.json               # Configuration file
│   ├── honeypot.py               # Main honeypot script
│   ├── logger.py                 # Handles logging functionalities
│   └── response_handler.py       # Manages honeypot responses
```

---

## Prerequisites
- Python 3.8 or later
- Basic understanding of network security and Python scripting

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SaiBhargavYenisetti/MyHoneyPot.git
   cd MyHoneyPot
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the honeypot settings in `src/config.json`.

---

## Usage
1. Navigate to the project directory:
   ```bash
   cd src
   ```

2. Run the honeypot script:
   ```bash
   python honeypot.py
   ```

3. Monitor the logs in `logs/honeypot_log.txt`.

---

## Configuration
The `config.json` file allows customization of:
- Listening ports
- Response types
- Logging levels

Example:
```json
{
  "port": 8080,
  "log_level": "INFO",
  "responses": {
    "404": "Not Found",
    "500": "Internal Server Error"
  }
}
```

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer
This tool is for educational purposes only. The creators are not responsible for any misuse of this project.

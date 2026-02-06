# CTI-Lab

A Python-based laboratory for Cyber Threat Intelligence (CTI) tasks. This repo provides simple tools to collect and process threat data, starting with a script to fetch Indicators of Compromise (IOCs) from AlienVault's Open Threat Exchange (OTX).

## Features
- **OTX IOC Fetcher**: Retrieves recent IOCs from subscribed OTX pulses and exports them to a dated CSV file for easy analysis.
- Modular design for easy expansion with additional CTI tools (e.g., future scripts for threat feed integration, analysis, or visualization).
- Lightweight and dependency-minimal: Relies only on standard Python libraries and `requests`.

## Requirements
- Python 3.6+
- `requests` library (install via `pip install requests`)
- An AlienVault OTX API key (free signup at [otx.alienvault.com](https://otx.alienvault.com/))

## Installation
1. Clone the repository:
  git clone https://github.com/tronplex/CTI-Lab.git
  cd CTI-Lab

2. Install dependencies:
   pip install requests

3. Set your OTX API key as an environment variable (for security—never hardcode it):
- On Linux/Mac: Add `export OTX_API_KEY="your-api-key"` to your `~/.bashrc` or `~/.zshrc` and run `source ~/.bashrc`.
- On Windows: Use `set OTX_API_KEY=your-api-key` in Command Prompt, or set it permanently via System Environment Variables.

## Usage
Run the OTX IOC fetcher script to pull data from your subscribed pulses (limited to the first 10 for efficiency):
  python otx_iocs.py


- **Output**: Generates a CSV file like `otx_iocs_YYYYMMDD.csv` in the current directory, containing columns for `IOC`, `Type`, `Threat`, and `Date`.
- **Example Output**:
  IOC,Type,Threat,Date
  example.com,domain,Malicious Domain Pulse,2026-02-05
  192.0.2.1,IPv4,Suspicious IP Activity,2026-02-05

- **Customization**: Edit the script to adjust the pulse limit (e.g., change `[:10]` to fetch more) or add filters for specific indicator types.

If the API key is not set, the script will exit with an error message.

## Contributing
Contributions are welcome! If you'd like to add new CTI tools, improve the existing script, or suggest features:
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/new-tool`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-tool`).
5. Open a Pull Request.

Please follow Python best practices (PEP 8) and include tests if possible.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

(If no LICENSE file exists yet, create one with standard MIT text.)

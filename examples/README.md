# MSFTRecon Examples

This directory contains example scripts and use cases for running msftrecon against various domains.

## Running Against hipotecario.com.ar

To run reconnaissance against the hipotecario.com.ar domain, use the following command:

```bash
./msftrecon.py -d hipotecario.com.ar
```

### With JSON Output

To get structured JSON output for further processing:

```bash
./msftrecon.py -d hipotecario.com.ar -j
```

### Using the Example Script

A pre-configured script is available for convenience:

```bash
cd examples
chmod +x hipotecario_example.sh
./hipotecario_example.sh
```

This script will:
1. Run reconnaissance against hipotecario.com.ar
2. Generate both console and JSON output
3. Save results to `output/hipotecario.com.ar_results.json`

## Expected Information

When running against any domain, msftrecon will attempt to gather:

- Tenant information and ID
- Federation configuration
- Azure AD settings
- Microsoft 365 service usage
- Azure service endpoints
- MDI (Microsoft Defender for Identity) detection
- Authentication methods
- Enterprise applications
- Storage accounts
- Communication services (Teams, Skype)

## Notes

- Some domains may not be configured with Microsoft 365, which will result in an error message
- Results depend on the target domain's configuration and publicly accessible information
- No authentication is required for basic reconnaissance

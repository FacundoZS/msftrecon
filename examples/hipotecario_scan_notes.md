# hipotecario.com.ar Scan

This document describes the execution of msftrecon against the domain hipotecario.com.ar.

## Execution Command

```bash
./msftrecon.py -d hipotecario.com.ar
```

## Expected Behavior

The tool attempts to:
1. Query Microsoft's autodiscover service for the domain
2. Enumerate tenant information
3. Check for Microsoft 365 services
4. Scan for Azure services
5. Detect MDI (Microsoft Defender for Identity) presence

## Possible Results

### If Microsoft 365 is Configured

The tool would provide comprehensive reconnaissance data including:
- Tenant name and ID
- Federation information
- Azure AD configuration
- Microsoft 365 service detection
- Azure service endpoints
- Communication services (Teams, Skype)
- MDI detection

### If Microsoft 365 is Not Configured

The tool may return:
```
[-] Unable to execute request. Wrong domain?
```

This indicates that either:
- The domain is not configured with Microsoft 365 services
- The domain does not use Microsoft's cloud infrastructure
- The domain may not be publicly accessible or resolvable

## JSON Output

When executed with the `-j` flag:
```bash
./msftrecon.py -d hipotecario.com.ar -j
```

The output will be in JSON format, making it easy to parse and integrate with other tools.

## Additional Resources

See the main [README](../README.md) for more information about expected output formats and tool capabilities.

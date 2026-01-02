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

## Result

The domain hipotecario.com.ar returns:
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

Returns:
```json
{
  "error": "Unable to execute request. Wrong domain"
}
```

## Alternative Usage

For domains that are configured with Microsoft 365, the tool would provide comprehensive reconnaissance data including:
- Tenant name and ID
- Federation information
- Azure AD configuration
- Microsoft 365 service detection
- Azure service endpoints
- Communication services (Teams, Skype)
- MDI detection

See the main [README](../README.md) for more information about expected output formats.

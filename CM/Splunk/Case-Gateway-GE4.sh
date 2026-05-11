index=1003412_nprod appName="Case.Gateway" environment="ge4"
| spath appName
| eval Date=strftime(_time, "%m/%d/%Y %H:%M:%S")
| spath logMessage
| sort -Date
| search logMessage="*Insert the correlationId here*"
| spath input=logMessage
| table Date, logMessage

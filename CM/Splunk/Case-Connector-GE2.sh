index=1003412_nprod appName="Case.Connector.Api" environment="ge2"
| spath appName
| eval Date=strftime(_time, "%m/%d/%Y %H:%M:%S")
| spath logMessage
| search logMessage="*Insert the Correlation ID here*"
| spath input=logMessage
| sort -Date
| table appName, Date, logMessage

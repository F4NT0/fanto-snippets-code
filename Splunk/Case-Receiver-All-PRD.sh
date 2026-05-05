index=1003412 appName="Case.Receiver.Api" environment="production"
| spath appName
| eval Date=strftime(_time, "%m/%d/%Y %H:%M:%S")
| spath logMessage
| search logMessage="*- Received message type*"
| sort -Date
| spath input=logMessage
| table Date, logMessage

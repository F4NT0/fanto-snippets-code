index=1003412_nprod appName="Case.Receiver.Api" environment="ge4"
| spath appName
| eval Date=strftime(_time, "%m/%d/%Y %H:%M:%S")
| spath logMessage
| search logMessage="*BB17D90C-21B3-4FBD-A392-TESTNP*"
| sort -Date
| spath input=logMessage
| table Date, logMessage

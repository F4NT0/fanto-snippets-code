index IN (1003496) 
cf_org_name=DFSPrtnPortalOrg
sourcetype="cf_log:DFSPrtnPortalOrg:partnerportal:abstractioncredit-soapgateway"
| spath cf_app_name
| spath msg
| eval Date=strftime(_time, "%m/%d/%Y %H:%M:%S") 
| search msg="*TRSFE0001350329*" 
| sort - timestamp
| spath input=msg
| table Date,ApplicationName,message

import firecloud.api as fapi
import re
from datetime import date

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

r=fapi.list_workspaces()
workspaceList=[]

for workspace in r.json():
    try:
        thedate=(re.sub("-", ",", workspace['workspaceSubmissionStats']['lastSuccessDate']).split("T")[0]).split(",")
        if date(int(thedate[0]), int(thedate[1]), int(thedate[2]))<date(2018, 8, 30):
            continue
    except KeyError:
        continue
    if workspace["public"]==False and workspace["workspace"]["namespace"]=="broadtagteam" and (workspace["accessLevel"]=="OWNER" or workspace["accessLevel"]=="PROJECT_OWNER"):
            workspaceList.append(workspace["workspace"]["name"])

print(workspaceList)
print("Workspace\tBucket Usage\tStorage Cost\tMethod Configs")
for workspace in workspaceList:
    methodList=[]
    for method in fapi.list_workspace_configs("broadtagteam", workspace).json():
        methodList.append(method['name'])
    print(str(workspace)+"\t"+str(sizeof_fmt(fapi.get_bucket_usage("broadtagteam", workspace).json()['usageInBytes']))+"\t"+
          str(fapi.get_storage_cost("broadtagteam", workspace).json()['estimate'])+"\t"+str(methodList))




            
            
        

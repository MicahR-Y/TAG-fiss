import firecloud.api as fapi
from argparse import ArgumentParser

def main(args):
    s=fapi.get_submission("broadtagteam", args.wkspc, args.sid).json()['workflows']
    for wf in s:
        if wf['status']=="Failed":
            getwf=fapi.get_workflow_metadata("broadtagteam",args.wkspc, args.sid, wf['workflowId']).json()
            print(getwf['failures'][0]['causedBy'][0]['message'])
            
if __name__ == "__main__":
    parser = ArgumentParser(description="Find failure messages for workflows in a submission")
    parser.add_argument("wkspc", help="the FireCloud workspace")
    parser.add_argument("sid", help="submission id for the desired submission")
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt: pass

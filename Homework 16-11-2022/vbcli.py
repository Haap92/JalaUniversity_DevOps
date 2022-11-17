import virtualbox;
import sys 

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()

if( sys.argv[1] == "list"):
  print([m.name for m in vbox.machines])
elif sys.argv[1] == "up":
  machine = vbox.find_machine(sys.argv[2])
  progress = machine.launch_vm_process(session, "gui", [])
  progress.wait_for_completion()
elif sys.argv[1] == "state":
  print(session.state)
elif sys.argv[1] == "down":
  session.console.power_down()
elif sys.argv[1] == "create":
  cm = vbox.create_machine('',sys.argv[2],['/'],'','')
  vbox.register_machine(cm)
elif sys.argv[1] == "delete":
  dm = vbox.find_machine(sys.argv[2])
  dm.remove(delete=True)

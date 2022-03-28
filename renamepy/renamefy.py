import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import scan_base_folder

watch_folder = Path("renamepy/files/")

class Watcher():

    def __init__(self, directory= watch_folder, handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nCopie os arquivos que deseja renomear para o diretório {}\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nObservador encerrado!\n")

class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        # print(event)
        if event.event_type == 'created':
            time.sleep(1)
            main()            
        # if event.event_type == 'deletd':
        #     print("Arquivo apagado!")

def main():
    
    scan_base_folder.scan_base_dir(watch_folder)
  
if __name__ == '__main__':
    w = Watcher(watch_folder, MyHandler())
    w.run()
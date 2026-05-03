import os
import requests
import shutil

def download_file(url, directory, fname= None):
    if fname ==None :
        fname = os.path.basename(url)
    new_dl_path = os.path.join(directory,fname)
    # for bigger item to download
    with requests.get(url, stream =True) as r:
        with open(new_dl_path, 'wb') as file_obj:
            shutil.copyfileobj(r.raw,file_obj)
    return new_dl_path


#another way also but its slower
def download_file_slower(url):
    local_filename = url.split('/')[-1]
    with requests.get(url,stream= True) as r:
        r.raise_for_status()
        with open(local_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size =8192):
                if chunk:
                    f.write(chunk)
    return local_filename

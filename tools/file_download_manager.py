import os
from network.canvas_session_manager import CanvasSession

def download(uri: str, course_folder: str, download_path: str, page_session: CanvasSession):



    if not os.path.exists(os.path.join(download_path, course_folder, section_folder)):
        os.makedirs(os.path.join(download_dir, course_folder, section_folder))  # create folder if it does not exist
    if node.file_name is not None:
        filename = node.file_name
    else:
        filename = node.url.split('/')[-1].replace(" ", "_")  # be careful with file names

    filename = clean_filename(filename)

    r = page_session.get(node.url)
    print("NODE URL", node.url)
    if r.ok:
        file_path = os.path.join(download_dir, course_folder, section_folder, filename)
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        return file_path
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
        return None
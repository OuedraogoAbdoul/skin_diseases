from fastai.vision import *

def download_images_urls():
    """Download images form urls in the .csv files.

    Args:
        N/A (): No parameter.

    Returns:
        N/A: The return value. 

    """
    

    folder = 'folder_name'
    file = 'zB5dK0Mk.csv'
    path_test = Path('Stasis dermatitis')
    dest = path_test/folder
    dest.mkdir(parents=True, exist_ok=True)
    download_images(path_test/file, dest, max_pics=1000)

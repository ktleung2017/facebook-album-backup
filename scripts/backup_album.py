# -*- coding: utf-8 -*-

import os
import dotenv
import sys
import logging
import facebook
import pandas as pd
from .utils import create_album_dir, photo_exists, save_photo


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(filename)s:%(lineno)s %(levelname)s: %(message)s')

def get_albums():
    # Load token from .env
    dotenv.load_dotenv('.env')
    access_token = os.environ['FB_ACCESS_TOKEN']
    
    # Create graph
    graph = facebook.GraphAPI(access_token=access_token, version='2.7')
    
    user_id = graph.get_object('me')['id']
    album_list = graph.get_object('{}/albums'.format(user_id))['data']
    
    if not album_list:
        logging.info('No albums can be found for this user')
    else:
        album_df = pd.DataFrame(album_list).sort_values('created_time').reset_index(drop=True)
        
        print(str(album_df))


def backup_album(album_id):
    # Load token from .env
    dotenv.load_dotenv('.env')
    access_token = os.environ['FB_ACCESS_TOKEN']
    
    # Create graph
    graph = facebook.GraphAPI(access_token=access_token, version='2.7')
    
    # Get album data
    album_data = graph.get_object(id='{}/photos'.format(album_id))['data']
    if not album_data:
        logging.info('Album {} does not exists'.format(album_id))
        return None
    
    create_album_dir(album_id)
    photo_df = pd.DataFrame(album_data)
    
    photo_df['created_time'] = pd.to_datetime(photo_df['created_time'], format='%Y-%m-%dT%H:%M:%S+0000')
    
    n_photos = photo_df.shape[0]
    if n_photos:
        logging.info('Saving {} photos from album {}'.format(n_photos, album_id))
        
        for photo_id in photo_df['id']:
            if not photo_exists(album_id, photo_id):
                photo_image = graph.get_object('{}/picture'.format(photo_id))
                save_photo(photo_image['data'], album_id, photo_id)
            else:
                logging.info('Photo {} already exits'.format(photo_id))
    else:
        logging.info('No photos in album {}'.format(album_id))

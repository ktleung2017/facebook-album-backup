# -*- coding: utf-8 -*-

import os
import sys
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(filename)s:%(lineno)s %(levelname)s: %(message)s')

def create_album_dir(album_id):
    logger.info('Creating directory for album {}'.format(album_id))
    
    if os.path.exists(os.path.join('album', str(album_id))):
        logger.info('Album {} already exists'.format(album_id))
    else:
        os.mkdir(os.path.join('album', str(album_id)))


def photo_exists(album_id, photo_id):
    full_path = os.path.join('album', str(album_id), '{}.png'.format(photo_id))
    return os.path.exists(full_path)


def save_photo(byte_string, album_id, photo_id):
    logger.info('Saving photo {}'.format(photo_id))
    
    full_path = os.path.join('album', str(album_id), '{}.png'.format(photo_id))
    with open(full_path, 'wb') as f:
        f.write(byte_string)

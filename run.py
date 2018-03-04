# -*- coding: utf-8 -*-

import click
from scripts.backup_album import backup_album, get_albums


@click.group()
def app():
    pass


@click.command()
def getAlbums():
    get_albums()


@click.command()
@click.argument('album_id')
def backupAlbum(album_id):
    backup_album(album_id)


app.add_command(getAlbums, 'get-albums')
app.add_command(backupAlbum, 'backup-album')

if __name__ == '__main__':
    app()

# Facebook Album Back-up

## Usage

Python CLI for back-up a Facebook album with incremental basis

## Set-up

### Python

This CLI was developed in Python 3.

### User Access Token

Get `user_access_token` in <https://developers.facebook.com/tools/explorer/>.

1. Login with your Facebook account. 
2. Select `Get Token`.
3. Select `Get User Access Token`.
4. Change API version to `2.7` as this is the latest version of API supported by `facebook-sdk` in PyPI.
5. Check the box for `user_photos`. You may leave all the others unchecked.
6. Select `Get Access Token`.

You may copy the `Access Token` now.

This token is NOT permanent. You need to regenerate each time you use this CLI.

### How to use

1. Clone this repo.
2. Change to this directory by `cd facebook-album-backup`.
3. `pip3 install -r requirements.txt`.
4. `cp env.template .env`, then fill in the `user_access_token` generated above.
5. `mkdir album` for storing albums.

Currently this CLI supports 2 commands:

1. `python3 run.py get-albums` to generate list of albums and album_id.
2. `python3 run.py backup-album <album_id>` to download photos from desire album.

## Remarks

For Windows users, to display UTF-8 characters correctly in CMD, use this command:

`chcp 936`

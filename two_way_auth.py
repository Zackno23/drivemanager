from pyicloud import PyiCloudService
import sys
import json


def get_oauth():
    auth = api.devices[3].location()
    return auth


# def deg_to_dms(deg):
#     degree = str(int(deg))
#     minuit = str(int((deg - float(degree)) * 60))
#     second = str(round(((deg - float(degree)) * 60 - float(minuit)) * 60, 5))
#     return f'{degree}度{minuit}分{second}秒'


api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')


def get_gps_from_iphone(api):
    if api.requires_2fa:
        import click

        print("Two-factor authentication required. Your trusted devices are:")

        devices = api.trusted_devices
        for i, device in enumerate(devices):
            print("  %s: %s" % (i, device.get('deviceName',
                                              "SMS to %s" % device.get('phoneNumber'))))

        device = click.prompt('Which device would you like to use?', default=0)
        device = devices[device]
        if not api.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)
    # 緯度経度の表示形式を変換

    auth = str(get_oauth())
    auth = auth.replace("'", '"')
    auth = auth.replace("True", "true")
    auth = auth.replace("False", "false")

    dic = json.loads(auth)
    longitude = round(dic['longitude'], 3)
    latitude = round(dic['latitude'], 3)
    return [latitude, longitude]

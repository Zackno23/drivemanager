from pyicloud import PyiCloudService
import sys
import json

# 以下は接続するicloudのアカウントとパスワードを記載します。
api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

# ここから2段認証を実施する。
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


def get_oauth():
    # デバイスナンバーは、icloudに登録しているデバイスに応じて数が異なる。
    auth = api.devices[3].location()
    return auth


if __name__ == '__main__':
    auth = str(get_oauth())
    auth = auth.replace("'", '"')
    auth = auth.replace("True", "true")
    auth = auth.replace("False", "false")

    dic = json.loads(auth)
    print(f"longitude: {dic['longitude']}")
    print(f"latitude: {dic['latitude']}")




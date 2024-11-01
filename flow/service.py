from django.conf import settings
import os
import django

import qrcode


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'casher.settings')
django.setup()


def generate_h5_qr_code(workflow_id, web_type='c'):
    _dir = settings.BASE_DIR / f"./media/qrcode/h5/{web_type}/"
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    # 如果有查询参数，将其添加到路径
    url = f'http://aidep.cn/web/id={workflow_id}'
    img = qrcode.make(url)
    img.save(_dir / f'{workflow_id}.png')
    return f'http://192.168.10.104:8000/media/qrcode/h5/{web_type}/{workflow_id}.png'


if __name__ == '__main__':
    a = generate_h5_qr_code(123)
    print(a)

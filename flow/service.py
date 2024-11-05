from django.conf import settings
import os

import qrcode


def generate_h5_qr_code(workflow_id, web_type='c'):
    _dir = settings.BASE_DIR / f"./media/qrcode/h5/{web_type}/"
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    # 如果有查询参数，将其添加到路径
    url = f'http://aidep.cn/web/id={workflow_id}'
    img = qrcode.make(url)
    img.save(_dir / f'{workflow_id}.png')
    return f'http://aidep.cn/media/qrcode/h5/{web_type}/{workflow_id}.png'

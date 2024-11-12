from yunzhanghu_sdk.client.api.model.payment import *
from yunzhanghu_sdk.client.api.payment_client import PaymentClient
from yunzhanghu_sdk.config import Config

# 实时支付
if __name__ == "__main__":
    conf = Config(
        # 生产环境请求域名
        # host = "https://api-service.yunzhanghu.com",
        # 沙箱环境请求域名
        # host = "https://api-service.yunzhanghu.com/sandbox",
        # 个体工商户注册请求域名
        # host = "https://api-aic.yunzhanghu.com",
        # host=settings.YUNZHANGHU_HOST,
        host="https://api-service.yunzhanghu.com/sandbox",
        dealer_id="28789345",
        broker_id="27532644",
        sign_type="rsa",
        app_key="nemrX7lEmjBd8O3LiUgK23bbqaSxnHQD",
        des3key="U26yJ75JAyVIs5GmLZd9pX6N",
        dealer_private_key="""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+twZemyIMH+/B
tnXn6SrMTuINP0WfaMQktPqlGUoG6HoeQlT/e0zNjF9SjVBiuR80Kc7Kxjylry6f
SmUPqaPAibic9SATzHUngo2cE1ISEPC1N9x3Bl2Q1kIGZXii4PD3oJslLRio4Dxq
JyyVDXsb4Eho8ciSTODl5PPZNLuLzaDa+5dmH+yPsUae4s1TNTi+1wLQT4LsDRM0
zH0FRcoSZcNYOgm8QSrfeFbXCQ2isHzUcB8VqkxR8pw2uZjN3ySqe1h8hgSx5EJJ
Ser87s0rkI0yu6/EyvKcgRy2EW3+O1RFPsoDr7n3JJD+/ilkLb4h1x6k45V/RQUO
m0fB2NV1AgMBAAECggEATMgA73vDhGAjNbkQ1RJhoamshqrPi/Mw7JpUQr3guNFF
wQLxl337mNGH2wN7tpNTRbwDPk37QrU5rvXTpC+m9rA7vC1QAciR7hs4ifqZUx6w
2jSoNN9CMjqgkFSv8dtgCEIH1DrIr8y/ZflpkITB6KIuZNna51O+Q7AeoHcDfq/S
lLoqeYmP8dzD/YpucOG2BGf/yLhJ5yoHmiXhLmg3uABUOWwh8wORIcwsrYhm24u+
RqA67XWj1zfi8keXOTWvmwStC0/hi4EGrvsF2Kqi55socsw/T28fLFqzcvMKM9U8
9/xtbhJyXDInqK+pxRNnTi1626+HaSP+872tt0+/4QKBgQD4BLe6eonRpt/PtyQ9
0txhMRADpjnO+6t0VjEYAdI+jANyPspCaqtV/gUTbxYaLFxKke8WHdJnCbtLcl9R
nJM6YNlhjzSBtHUoJDoFOpTMpP+pZhO/m+xBbbpovu/CC7y5CSOe52RdLDUmU68j
9CGIuRRig4IMWeOf9MCZ5+bOaQKBgQDE2jdpqFuEUCcIN2NRjsNxtKorN2VYMpd7
OI3WRwjzy57ZMFS+bgcnt4hVHaz+CdbwYtPrAAvPikrptKOdQWnKed7lQkilHpxm
tP3XxW6prSbyqgBu9Gx87iO0BGtP4bH+Hs0ATF8S33rmpidN913U+HnW/Dn301Aa
rQFyH3qFLQKBgQC6AdfFTGeWS7/pKaJNl5neboxjIESUvlzdOFNDfQIwFJP1F7Bb
VWLAcG1gIN0DriddactU2/LTghHsyI9CRtqIWuBNcbhgWnXPMDQvfbrhLBHt+vdu
qcLrYx79tc1cy66zW25Sm5nC4wfNgc+FeG+5+YyXQafEGZpEeawFAU4xmQKBgGWH
z5DVXu5tkNQyDS3hnnilICfOGJ1W6r6JOs7MMJfd6/5FaVAW2+XmSZDtD26vkIbH
0lmg2nae82h63PCc7n2aQhapC2Lu2Og4bby+fgdR4YbDnBmeQ95jzVJp/RdkZzOU
m1OOEHNhhLg19ovGDEVuKxlxWkyyVtyLYvWDuuO5AoGAblKKNGh0DFhADe9ggX9U
ml0M7XRlDvgFF7x5WRq3Uxr5DWO5xgZPqjSMGGSz/5p+5mNNA4r2dAZLnm5l1T9a
MfSsEJJu6RmhifCU+VMxISzomjTJDiI9QJs3Rl5/iIcutnfvTmsgk6JULgItbOxa
I8YpyBPZF5yCAUfmPOyOGes=
-----END PRIVATE KEY-----""",
        yzh_public_key="""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDSCHhZvdWZhJo4nASvxsoW7pMg
ZUvWm0GZleoCFpPSVnQ5zUGAaIAuvNaqG0QsCjvCbnrXMfDvjrEEKVSGAUbB8Azz
guD2Q/iELU4z3Kxb1EXYoS9QkSxQvUYlAcV3/o4i+xrBHDpPuYrxTpWzAPGnUOtc
1sz4bKDdvBF12bjywwIDAQAB
-----END PUBLIC KEY-----""",
        # 自定义超时时间
        timeout=30,
    )
    client = PaymentClient(config=conf)

    # 微信实时支付
    req = CreateWxpayOrderRequest(
        order_id="2020-0901-0016-5620-12981",
        dealer_id=conf.dealer_id,
        broker_id=conf.broker_id,
        real_name="张三",
        openid="020-0901-0016-5620-1298",
        id_card="11010519491231002X",
        phone_no="18834568888",
        pay="1.00",
        pay_remark="",
        notify_url="https://www.example.com",
        wx_app_id="",
        wxpay_mode="transfer",
        project_id="casher",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample12345qweqw"
    try:
        resp = client.create_wxpay_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print(
                "失败返回 ",
                "code："
                + resp.code
                + " message："
                + resp.message
                + " request_id："
                + resp.request_id,
            )
    except Exception as e:
        # 发生异常
        print(e)

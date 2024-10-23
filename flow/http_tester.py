import aiohttp
import json
import os

# 请求的 URL，r 和 techsid 放在 URL 中
r_value = "comfyui.apiv2.upload"
techsid_value = "abc1234"
url = f"http://0.0.0.0:8000/flow/api/upload/?r={r_value}&techsid={techsid_value}"

# JSON 数据
post_data = {
    "r": "comfyui.apiv2.upload",
    "techsid": "",
    "postData": {
        "res_node": "29",
        "mainImages": ["1.jpg"],
        "cs_img_nodes": [{"node": "51", "desc": "\u8bf7\u4e0a\u4f20\u56fe\u7247"}],
        "cs_video_nodes": [],
        "cs_text_nodes": [{"node": "50", "desc": "\u8bf7\u8f93\u5165\u6587\u672c"}],
        "title": "\u4f5c\u54c1\u6807\u9898",
        "gn_desc": "\u4f5c\u54c1\u63cf\u8ff0",
        "sy_desc": "\u4f5c\u54c1\u4f7f\u7528\u8bf4\u660e",
        "fee": 25,
        "free_times": 2,
        "uniqueid": "m28no55f0xwtk9dcwuwcclbwh8",
        "subdomain": "ef28c7ddcc72",
    },
    "version": "2.0.0",
}

# 图片文件路径
image_file_path = "./"


async def upload_task():
    async with aiohttp.ClientSession() as session:
        form_data = aiohttp.FormData()

        # 添加 JSON 数据
        form_data.add_field("json_data", json.dumps(post_data))

        # 添加图片文件
        for img in post_data.get("postData").get("mainImages"):
            if os.path.exists(image_file_path + f"{img}"):
                with open(image_file_path + f"{img}", "rb") as f:
                    file_content = f.read()
                form_data.add_field(
                    "mainImages",
                    file_content,
                    filename="1.png",
                    content_type="application/octet-stream",
                )

        # 发起 POST 请求
        async with session.post(url, data=form_data) as response:
            if response.status == 200:
                response_text = await response.text()
                print("上传成功:", response_text)
            else:
                print("上传失败，状态码:", response.status)


# 运行异步任务
if __name__ == "__main__":
    import asyncio

    asyncio.run(upload_task())

# 用户端接口

## 用户端数据流列表

请求地址: /flow/flows/
请求方法：GET
返回数据：
```json
{
  "status": 200,
  "data": [
    {
        "id": 1,
        "title": "title",
        "gn_desc": "作品功能介绍",
        "sy_desc": "作品使用说明",
        "fee": 10,
        "free_time": 1,
        "uniqueid": "唯一标记",
        "client_id": "客户端id(提交任务时需要带)",
        "created": "2024-10-19 10:00:00",
        "updated": "2024-10-19 10:00:00",
        "images": [
          {
            "id": 1,
            "image": "图片地址"
          }
        ]
      }
  ]
}
```

## 用户端数据流详情

请求地址: /flow/flows/{id}/
请求方法：GET
返回数据：
```json
{
  "status": 200,
  "data": {
    "id": 1,
    "title": "title",
    "gn_desc": "作品功能介绍",
    "sy_desc": "作品使用说明",
    "fee": 10,
    "free_time": 1,
    "uniqueid": "唯一标记",
    "client_id": "客户端id(提交任务时需要带)",
    "created": "2024-10-19 10:00:00",
    "updated": "2024-10-19 10:00:00",
    "images": [
      {
        "id": 1,
        "image": "图片地址"
      }
    ]
  }
}
```

## 用户端数据流图片上传

请求地址: /task/upload/
请求方法：POST
请求数据：
格式：form-data
image: 图片

返回数据：
```json
{
  "status": 200,
  "data": {
    "id": 1,
    "image": "url"
  }
}
```

## 用户端数据流运行
请求地址: /task/prompt/
请求方法：POST
请求数据：
```json

```

返回数据：
```json

```

## 用户端数据流运行结果查询
请求地址: /task/result/
请求方法：POST
请求数据：
```json

```

返回数据：
```json

```

## 用户端数据流运行结果历史记录
请求地址: /task/history/
请求方法：POST
请求数据：
```json

```

返回数据：
```json

```


## 用户端数据流评论列表
请求地址: /flow/flow_comments/
请求方法：GET

返回数据：
```json

```

## 用户端数据流评论添加
请求地址: /flow/flow_comments/
请求方法：POST
```json

```

返回数据：
```json

```

## 用户端付款
***
import{g as t,O as e,h as a,P as s,p as o,l as n,k as r,s as p,m as i}from"./index-Cq5DkhQ_.js";const c=(t,e)=>{const a=t.__vccOpts||t;for(const[s,o]of e)a[s]=o;return a},l={cappsList:"/capps",templatesList:"/capps/templates",gpusList:"/capps/gpus",createCapp:"/capps/create",startCapp:"/capps/start/",stopCapp:"/capps/stop/",delCapp:"/capps/",userInfo:"/users/me",durationType:"/powers/duration-types",durationPrice:"/powers/clculate-duration-price",clculatePrice:"/powers/clculate-price",transactionsList:"/transactions",flowsList:"/flow/flows/",promptStart:"/task/prompt/",imgResult:"/task/view/",imgHistory:"/task/history/",mplogin:"/wxapp/login/",qrcodeLogin:"/accounts/weixin/login_url/",googleLogin:"/accounts/google/login_url/",uploadUrl:"/task/upload/",depositPay:"/payment/create-payment/",wechatPay:"/payment/create-wechatpay/",wechatPayResult:"/payment/wechat-check/",getPower:"/payment/user-hashrate/",powersOptions:"/payment/hashrate-template/",pricePowers:"/payment/hashrate-convert/",commentsPop:"/flow/comments/",banner:"/flow/banner/",imgInfo:"/task/history/detail/",delimg:"/task/history/delete/",workInfo:"/task/view/"};function u(t){return h.httpRequest({url:l.googleLogin,method:"GET"},t)}function g(t){return h.httpRequest({url:l.qrcodeLogin,method:"GET"},t)}const h={baseUrl:"https://aidep.cn",httpRequest:(c,u)=>{let g=t("token"),d=t("language"),m={url:"https://aidep.cn"+c.url,data:u,method:c.method,header:"get"==c.method?{languageStr:d,authorization:"bearer "+g,"X-Requested-With":"XMLHttpRequest",Accept:"application/json","Content-Type":"application/json; charset=UTF-8"}:{languageStr:d,authorization:"bearer "+g,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/json; charset=UTF-8"},dataType:"json"};return new Promise((function(c,u){e(m).then((e=>{switch(e.data.status){case 401:if(s("token"),"mp-weixin"===t("uniPlatform"))n({success(t){if(t.code){r({title:"加载中",mask:!0});var e=t.code;uni.getUserInfo({lang:"zh_CN",success:t=>{let s={};var o;s.code=e,s.rawData=t.rawData,s.signature=t.signature,s.encryptedData=t.encryptedData,s.iv=t.iv,(o=s,h.httpRequest({url:l.mplogin,method:"POST"},o)).then((t=>{if(200!=t.status)return a({icon:"none",title:t.data.msg});p("token",t.data.token),a({icon:"success",title:"登录成功"}),i()}))},fail:t=>(i(),a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:t=>a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else o({url:"/pages/toc/toc02Login"});case 200:break;default:a({icon:"none",title:e.data.message})}c(e.data)})).catch((t=>{u(t)}))}))}};export{c as _,l as c,u as g,g as q,h as r};

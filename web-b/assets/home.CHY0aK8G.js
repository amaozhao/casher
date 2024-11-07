import{a as t,J as e,d as a,K as o,r as n,l as s,c as i,s as c,h as r,L as p,M as l,n as d}from"./index-A2NG4DAs.js";const u=(t,e)=>{const a=t.__vccOpts||t;for(const[o,n]of e)a[o]=n;return a};function h(t,e){return"string"==typeof t?e:t}const m={cappsList:"/capps",templatesList:"/capps/templates",gpusList:"/capps/gpus",createCapp:"/capps/create",startCapp:"/capps/start/",stopCapp:"/capps/stop/",delCapp:"/capps/",userInfo:"/users/me",durationType:"/powers/duration-types",durationPrice:"/powers/clculate-duration-price",clculatePrice:"/powers/clculate-price",transactionsList:"/transactions",flowsList:"/flow/b_flows/",promptStart:"/task/prompt/",imgResult:"/task/view/",imgHistory:"/task/history/",mplogin:"/wxappb/login/",qrcodeLogin:"/accounts/weixin/login_url/",googleLogin:"/accounts/google/login_url/",uploadUrl:"/task/upload/",depositPay:"/payment/create-payment/",wechatPay:"/payment/create-wechatpay/",wechatPayResult:"/payment/wechat-check/",getPower:"/payment/user-hashrate/",powersOptions:"/payment/hashrate-template/",pricePowers:"/payment/hashrate-convert/"};const g="https://aidep.cn:8601";const w={httpRequest:(p,l)=>{let d=t("token"),u=t("language"),h={url:g+p.url,data:l,method:p.method,header:"get"==p.method?{languageStr:u,authorization:"bearer "+d,"X-Requested-With":"XMLHttpRequest",Accept:"application/json","Content-Type":"application/json; charset=UTF-8"}:{languageStr:u,authorization:"bearer "+d,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/json; charset=UTF-8"},dataType:"json"};return new Promise((function(p,l){e(h).then((e=>{switch(e.data.code){case 10004:if(o("token"),"mp-weixin"===t("uniPlatform"))s({success(t){if(t.code){i({title:"加载中",mask:!0});var e=t.code;uni.getUserInfo({lang:"zh_CN",success:t=>{let o={};var n;o.code=e,o.rawData=t.rawData,o.signature=t.signature,o.encryptedData=t.encryptedData,o.iv=t.iv,(n=o,w.httpRequest({url:m.mplogin,method:"POST"},n)).then((t=>{if(2e4!=t.code)return a({icon:"none",title:t.data.msg});c("token",t.data.token),a({icon:"success",title:"登录成功"}),r()}))},fail:t=>(r(),a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:t=>a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else n({url:"/pages/web/web02GpuLogin"});break;case 2e4:break;default:console.log(e.data.code),a({icon:"none",title:e.data.message})}p(e.data)})).catch((t=>{l(t)}))}))},httpTokenRequest:(a,n)=>{let s,i="";s=t("token"),i=t("tempAuthorization");let c={url:g+a.url,data:n,method:a.method,header:"get"==a.method?{authorization:"bearer "+s,tempAuthorization:i,"X-Requested-With":"XMLHttpRequest",Accept:"application/json","Content-Type":"application/json; charset=UTF-8"}:{authorization:"bearer "+s,tempAuthorization:i,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},dataType:"json"};return new Promise((function(t,a){e(c).then((e=>{if(403===e[1].data.code)o("token"),p({url:"../home/home"}),l({confirmText:"前往登录",content:"登录已失效，请重新登录",showCancel:!1});t(e[1])})).catch((t=>{a(t)}))}))},post:function(t,n){return new Promise(((s,i)=>{e({url:g+t,data:n,method:"POST",header:{"X-Requested-With":"XMLHttpRequest",Accept:"application/json","Content-Type":"application/json; charset=UTF-8"},dataType:"json",success(t){console.log("http",t),0==t.data.code?s(t.data):(i(t.data),403==t.data.code?(console.log("触发403"),a({title:"登录已失效,请重新登录",icon:"none"}),o("token")):t.data.code)},fail(t){i(t)}})}))},get:async function(n,s){let i=await new Promise(((e,a)=>{const o=t("token");console.log("token",o),o?e(o):(setTimeout((()=>{d({url:"/pages/index/index"})}),1e3),a("登录过期"))}));return new Promise(((t,c)=>{e({url:g+n,data:s,method:"GET",header:{authorization:"bearer "+i,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},dataType:"json",success(e){console.log("http",e),0==e.data.code?t(e.data):(c(e.data),403==e.data.code?(console.log("触发403"),a({title:"登录已失效,请重新登录",icon:"none"}),o("token")):"401"==e.data.code||a({title:e.data.msg,icon:"none"}))},fail(t){c(t)}})}))}},f="data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M6.36025%2012.9744H13.0683V6.4359C13.0683%205.15385%2012.0745%204%2010.7081%204H6.36025C4.99379%204%204%205.15385%204%206.4359V10.6667C4%2011.9487%204.99379%2012.9744%206.36025%2012.9744ZM23.8758%2010.6667V6.4359C23.8758%205.15385%2022.882%204%2021.5155%204H17.1677C15.9255%204%2014.8075%205.02564%2014.8075%206.4359V13.1026H21.5155C22.882%2012.9744%2023.8758%2011.9487%2023.8758%2010.6667ZM17.2919%2024H21.764C23.0062%2024%2024%2022.9744%2024%2021.5641V17.3333C24%2016.0513%2023.0062%2014.8974%2021.6398%2014.8974H14.9317V21.5641C14.9317%2022.8462%2015.9255%2024%2017.2919%2024ZM6.36025%2024H10.7081C11.9503%2024%2013.0683%2022.9744%2013.0683%2021.5641V15.0256H6.36025C5.11801%2015.0256%204%2016.0513%204%2017.4615V21.6923C4%2022.8462%204.99379%2024%206.36025%2024Z'%20fill='white'/%3e%3c/svg%3e";export{u as _,h as a,f as b,m as c,w as r};

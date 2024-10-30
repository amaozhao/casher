import{e,f as t,b as o,w as l,u as i,o as n,v as s,d as a,a as g,t as d,A as c,z as r}from"./index-PECudOet.js";import{r as C,c as h}from"./http.BIclu_Zt.js";import{_}from"./_plugin-vue_export-helper.BCo6x5W8.js";const u="data:image/svg+xml,%3csvg%20width='28'%20height='29'%20viewBox='0%200%2028%2029'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M6.28523%2011.6527C7.39816%208.28037%2010.5673%205.85837%2014.3212%205.85837C16.339%205.85837%2018.1616%206.57439%2019.5937%207.74607L23.7596%203.58011C21.221%201.36695%2017.9664%200%2014.3212%200C8.67659%200%203.8168%203.22007%201.48047%207.93595L6.28523%2011.6527Z'%20fill='%23EA4335'/%3e%3cpath%20d='M19.1424%2021.4954C17.8418%2022.3352%2016.1892%2022.7823%2014.3203%2022.7823C10.5808%2022.7823%207.42153%2020.3788%206.29721%2017.0266L1.47656%2020.6868C3.80999%2025.4109%208.66966%2028.6407%2014.3203%2028.6407C17.8202%2028.6407%2021.1647%2027.3964%2023.6694%2025.06L19.1424%2021.4954Z'%20fill='%2334A853'/%3e%3cpath%20d='M23.6694%2025.0601C26.2888%2022.6167%2027.9898%2018.9788%2027.9898%2014.3203C27.9898%2013.4741%2027.8597%2012.5628%2027.6644%2011.7166H14.3203V17.2495H22.0013C21.6223%2019.11%2020.605%2020.5511%2019.1424%2021.4955L23.6694%2025.0601Z'%20fill='%234A90E2'/%3e%3cpath%20d='M6.2974%2017.027C6.0126%2016.1778%205.85837%2015.2678%205.85837%2014.3205C5.85837%2013.3877%206.00795%2012.4909%206.28453%2011.6528L1.47977%207.93604C0.521011%209.85785%200%2012.0238%200%2014.3205C0%2016.6113%200.530789%2018.772%201.47675%2020.6872L6.2974%2017.027Z'%20fill='%23FBBC05'/%3e%3c/svg%3e";const f=_({data:()=>({isGoogleLogin:!e("isChinese"),viewerUrl:""}),onShow:function(){console.log("index Show"),this.isGoogleLogin?this.handleGoogleLogin():(this.getPCwxcode(),this.handleQrcodeLogin())},methods:{getPCwxcode(){const e=document.createElement("script");e.type="text/javascript",e.src="https://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js";const t=document.body.appendChild(e);t.onload=()=>{const e=new WxLogin({state:!0,id:"login_container",appid:"wxe0539f0ed26b91a9",scope:"snsapi_login",redirect_uri:encodeURIComponent("http://www.deploycloud.cn"),state:Math.ceil(1e3*Math.random()),style:"white",href:"data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDIwMHB4O30NCi5pbXBvd2VyQm94IC50aXRsZSB7ZGlzcGxheTogbm9uZTt9DQouaW1wb3dlckJveCAuaW5mbyB7d2lkdGg6IDIwMHB4O30NCi5zdGF0dXNfaWNvbiB7ZGlzcGxheTpub25lfQ0KLmltcG93ZXJCb3ggLnN0YXR1cyB7dGV4dC1hbGlnbjogY2VudGVyO30="});e.on("login",(e=>{console.log("登录成功",e)})),e.on("error",(e=>{console.log("登录出错",e)})),e.on("cancel",(()=>{console.log("用户取消登录")}))}},goHomePage(){t({url:"/pages/index/index"})},goNextPage(){t({url:"/pages/toc/toc27Create"})},changeLoginType(){this.isGoogleLogin=!this.isGoogleLogin,this.isGoogleLogin?this.handleGoogleLogin():this.handleQrcodeLogin()},handleQrcodeLogin(){var e;C.httpRequest({url:h.qrcodeLogin,method:"GET"},e).then((e=>{200===e.status&&(this.viewerUrl=e.data.qr_url,window.open(this.viewerUrl))}))},handleGoogleLogin(){var e;C.httpRequest({url:h.googleLogin,method:"GET"},e).then((e=>{200==e.status&&window.open(e.data.url)}))}}},[["render",function(e,t,C,h,_,f){const m=r,p=i;return n(),o(p,{class:"flex column alignCenter bg_div"},{default:l((()=>[s(p,{class:"flex row justifyBetween alignCenter header_div",style:g("margin-top:"+e.appStatusBarHeight+"rpx")},{default:l((()=>[s(p,{class:"flex row alignCenter",onClick:t[0]||(t[0]=e=>f.goHomePage()())},{default:l((()=>[s(m,{class:"header_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M6.36025%2012.9744H13.0683V6.4359C13.0683%205.15385%2012.0745%204%2010.7081%204H6.36025C4.99379%204%204%205.15385%204%206.4359V10.6667C4%2011.9487%204.99379%2012.9744%206.36025%2012.9744ZM23.8758%2010.6667V6.4359C23.8758%205.15385%2022.882%204%2021.5155%204H17.1677C15.9255%204%2014.8075%205.02564%2014.8075%206.4359V13.1026H21.5155C22.882%2012.9744%2023.8758%2011.9487%2023.8758%2010.6667ZM17.2919%2024H21.764C23.0062%2024%2024%2022.9744%2024%2021.5641V17.3333C24%2016.0513%2023.0062%2014.8974%2021.6398%2014.8974H14.9317V21.5641C14.9317%2022.8462%2015.9255%2024%2017.2919%2024ZM6.36025%2024H10.7081C11.9503%2024%2013.0683%2022.9744%2013.0683%2021.5641V15.0256H6.36025C5.11801%2015.0256%204%2016.0513%204%2017.4615V21.6923C4%2022.8462%204.99379%2024%206.36025%2024Z'%20fill='white'/%3e%3c/svg%3e"}),s(p,{class:"title"},{default:l((()=>[a("Deploy AI")])),_:1})])),_:1})])),_:1},8,["style"]),s(p,{class:"login_text"},{default:l((()=>[a(d(e.$t("02_Sign")),1)])),_:1}),_.isGoogleLogin?(n(),o(p,{key:0,class:"flex column justifyCenter alignCenter main_login_div"},{default:l((()=>[s(m,{class:"main_login_img",src:u}),s(p,{class:"main_login_text"},{default:l((()=>[a(d(e.$t("02_Sign_Google")),1)])),_:1})])),_:1})):(n(),o(p,{key:1,class:"flex column justifyStart alignCenter main_login_div relative",onClick:t[1]||(t[1]=e=>f.goNextPage())},{default:l((()=>[c("iframe",{src:`${_.viewerUrl}`,width:"100%",height:"100%",frameborder:"0"},null,8,["src"])])),_:1})),s(p,{class:"flex row alignCenter divider_div"},{default:l((()=>[s(p,{class:"divider_line"}),s(p,{class:"divider_text"},{default:l((()=>[a(d(e.$t("02_or")),1)])),_:1}),s(p,{class:"divider_line2"})])),_:1}),_.isGoogleLogin?(n(),o(p,{key:2,class:"flex column justifyCenter alignCenter other_login_div",onClick:t[2]||(t[2]=e=>f.changeLoginType())},{default:l((()=>[s(m,{class:"other_login_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M18.3012%2010.1008C18.5691%2010.1008%2018.8371%2010.1008%2019.1051%2010.1445C18.3477%206.70469%2014.6809%204.15625%2010.4781%204.15625C5.78594%204.15625%201.94141%207.37461%201.94141%2011.3969C1.94141%2013.7211%203.19375%2015.6871%205.3375%2017.1637L4.48711%2019.7121L7.48125%2018.2383C8.55312%2018.4625%209.40352%2018.684%2010.4754%2018.684C10.7434%2018.684%2011.0113%2018.684%2011.3258%2018.6402C11.148%2018.0578%2011.0578%2017.4781%2011.0578%2016.852C11.0605%2013.1414%2014.2352%2010.1008%2018.3012%2010.1008ZM13.6965%207.77656C14.3664%207.77656%2014.7684%208.22227%2014.7684%208.84844C14.7684%209.47461%2014.3227%209.92031%2013.6965%209.92031C13.0266%209.92031%2012.4004%209.47188%2012.4004%208.84844C12.4004%208.17852%2013.073%207.77656%2013.6965%207.77656ZM7.78203%209.77539C7.10664%209.77539%206.475%209.33242%206.475%208.71445C6.475%208.05%207.15039%207.65352%207.78203%207.65352C8.41367%207.65352%208.86211%208.09648%208.86211%208.71445C8.86484%209.33516%208.41367%209.77539%207.78203%209.77539Z'%20fill='%230FC56D'/%3e%3cpath%20d='M26.0805%2016.7618C26.0805%2013.3192%2022.6844%2010.5493%2018.8398%2010.5493C14.7711%2010.5493%2011.5527%2013.3657%2011.5527%2016.7618C11.5527%2020.2044%2014.7711%2022.9743%2018.8398%2022.9743C19.6902%2022.9743%2020.5379%2022.7501%2021.3883%2022.5286L23.7125%2023.8247L23.0863%2021.6782C24.7844%2020.3821%2026.0805%2018.6841%2026.0805%2016.7618ZM16.4691%2015.6899C16.0672%2015.6899%2015.6188%2015.288%2015.6188%2014.8396C15.6188%2014.4376%2016.0645%2013.9892%2016.4691%2013.9892C17.0953%2013.9892%2017.541%2014.4349%2017.541%2014.8396C17.541%2015.288%2017.1391%2015.6899%2016.4691%2015.6899ZM21.3363%2015.4821C20.9316%2015.4821%2020.4805%2015.0829%2020.4805%2014.6427C20.4805%2014.2435%2020.9316%2013.8032%2021.3363%2013.8032C21.968%2013.8032%2022.4164%2014.2462%2022.4164%2014.6427C22.4164%2015.0856%2021.968%2015.4821%2021.3363%2015.4821Z'%20fill='%230FC56D'/%3e%3c/svg%3e"}),s(p,{class:"other_login_text"},{default:l((()=>[a(d(e.$t("02_Sign_WeiChat")),1)])),_:1})])),_:1})):(n(),o(p,{key:3,class:"flex column justifyCenter alignCenter other_login_div",onClick:t[3]||(t[3]=e=>f.changeLoginType())},{default:l((()=>[s(m,{class:"other_login_img",src:u}),s(p,{class:"other_login_text"},{default:l((()=>[a(d(e.$t("02_Sign_Google")),1)])),_:1})])),_:1}))])),_:1})}],["__scopeId","data-v-eacbf360"]]);export{f as default};

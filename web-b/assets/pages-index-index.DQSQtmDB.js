import{g as e,a as t,s as a,b as s,r as l,l as i,c as n,d as o,h as r,n as c,e as u,f as d,w as f,i as _,o as m,j as g,k as p,m as x,p as h,q as b,F as C,t as w,u as v,v as y,x as j}from"./index-DZZGyAJD.js";import{_ as k}from"./uni-link.D3O7D8ha.js";import{r as L}from"./uni-app.es.CjVRXCaX.js";import{r as P,c as T,_ as B}from"./home.BwDbU5G1.js";import{_ as H,a as I}from"./speed.FiO8-Deg.js";import{_ as D}from"./_plugin-vue_export-helper.BCo6x5W8.js";const R=D({data:()=>({src:"https://beian.miit.gov.cn/",appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui",isChinese:e("isChinese"),clientList:[]}),onLoad(e){if("mp-weixin"!==t("uniPlatform")){let e=new URL(window.location.href).searchParams.get("token");e&&a("token",e)}this.getFlowsList()},onShow:function(){let{statusBarHeight:e}=s();e>0&&(this.appStatusBarHeight=40+e)},methods:{getFlowsList(){var e;P.httpRequest({url:T.flowsList,method:"GET"},e).then((e=>{200==e.status&&(this.clientList=e.data||[])}))},handleLogin(){if(t("token"))this.getFlowsList();else{var e=this;if("mp-weixin"===t("uniPlatform"))i({success(t){if(t.code){n({title:"加载中",mask:!0});var s=t.code;uni.getUserInfo({lang:"zh_CN",success:t=>{let l={};var i;l.code=s,l.rawData=t.rawData,l.signature=t.signature,l.encryptedData=t.encryptedData,l.iv=t.iv,(i=l,P.httpRequest({url:T.mplogin,method:"POST"},i)).then((t=>{if(200!=t.status)return o({icon:"none",title:t.data.msg});a("token",t.data.token),o({icon:"success",title:"登录成功"}),e.handleLogin(),r()}))},fail:e=>(r(),o({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:e=>o({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else l({url:"/pages/tob/tob02Login"})}},goCreatePage(){c({url:"/pages/tob/tob17Create"})},onLeftTab(){l({url:"/pages/index/index"})},onHomeTab(){l({url:"/pages/index/index"})},onMeTab(){l({url:"/pages/tob/tob15Me"})}}},[["render",function(e,t,a,s,l,i){const n=v,o=_,r=L(u("uni-link"),k);return m(),d(o,{class:"flex column alignCenter bg_div"},{default:f((()=>[g(o,{class:"flex row justifyBetween alignCenter header_div",style:x("margin-top:"+l.appStatusBarHeight+"rpx")},{default:f((()=>[g(o,{class:"flex row alignCenter",onClick:t[0]||(t[0]=e=>i.onLeftTab())},{default:f((()=>[g(n,{class:"header_img",src:B}),g(o,{class:"title"},{default:f((()=>[p("Deploy AI")])),_:1})])),_:1}),g(o,{class:"flex row justifyCenter alignCenter tab_div"},{default:f((()=>[g(o,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:t[1]||(t[1]=e=>i.onHomeTab())},{default:f((()=>[g(n,{class:"tab_img",src:B}),g(o,{class:"tab_label"},{default:f((()=>[p("complaint")])),_:1})])),_:1}),g(o,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:t[2]||(t[2]=e=>i.onMeTab())},{default:f((()=>[g(n,{class:"tab_img",src:H}),g(o,{class:"tab_label"},{default:f((()=>[p("me")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),g(o,{class:"flex column alignCenter div_content"},{default:f((()=>[g(o,{class:"text1"},{default:f((()=>[p("快速创建")])),_:1}),g(o,{class:"text2"},{default:f((()=>[p("你的AI产品")])),_:1}),g(o,{class:"text3"},{default:f((()=>[p("将Comfyui工作流一键转化为Web/H5/小")])),_:1}),g(o,{class:"text4"},{default:f((()=>[p("程序/API，快速变现")])),_:1}),g(o,{class:"btn1"},{default:f((()=>[p("安装ComfyUI插件生成")])),_:1}),g(o,{class:"text5"},{default:f((()=>[p("您也可以选择云端转换：")])),_:1}),g(o,{class:"text6"},{default:f((()=>[p("上传或选择工作流模版转换为网页(后续可更换工作流）")])),_:1}),g(o,{class:"flex row wrap card2_div"},{default:f((()=>[(m(!0),h(C,null,b(l.clientList,((e,a)=>(m(),d(o,{class:"flex column card2",key:e.id},{default:f((()=>[g(o,{class:"flex row alignCenter card2_item"},{default:f((()=>[g(n,{class:"product_img",src:e.images[0].image},null,8,["src"]),g(o,{class:"flex column justifyBetween alignCenter card2_right_item"},{default:f((()=>[g(o,{class:"product_value_label"},{default:f((()=>[p(y(e.title),1)])),_:2},1024),g(o,{class:"flex row justifyCenter alignCenter btn_div",onClick:t[3]||(t[3]=e=>i.goCreatePage())},{default:f((()=>[g(n,{class:"btn_img",src:I}),g(o,{class:"btn_text"},{default:f((()=>[p("立即启用")])),_:1})])),_:1})])),_:2},1024)])),_:2},1024),g(o,{class:"flex row justifyBetween wrap card2_item2"},{default:f((()=>[g(o,{class:"flex row justifyBetween card2_right_item"},{default:f((()=>[g(o,{class:"card2_right_label"},{default:f((()=>[j("span",{class:"card2_right_head"},"预览URL:"),p(" https://xxx.xxx.com.xxx… ")])),_:1}),g(o,{class:"card2_right_copy"},{default:f((()=>[p("复制预览")])),_:1})])),_:1})])),_:1})])),_:2},1024)))),128))])),_:1}),g(o,{class:"flex row justifyCenter alignCenter bottom_btn_div",onClick:t[4]||(t[4]=e=>i.goCreatePage())},{default:f((()=>[g(n,{class:"bottom_btn_img",src:I}),g(o,{class:"bottom_btn_text"},{default:f((()=>[p("立即在线创新")])),_:1})])),_:1})])),_:1}),l.isChinese?(m(),d(r,{key:0,href:l.src,text:"【粤ICP备2024312061号-2】",class:"mgT10",style:{"margin-bottom":"40px"}},null,8,["href"])):w("",!0)])),_:1})}],["__scopeId","data-v-d84e0c6d"]]);export{R as default};

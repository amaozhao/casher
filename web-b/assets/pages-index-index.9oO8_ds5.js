import{m as e,o as t,c as a,r as s,n as l,a as i,b as n,w as r,d as c,t as o,i as d,g as _,e as f,f as u,h as x,j as g,k as h,l as m,p,q as b}from"./index-C4OrJxFS.js";import{_ as w,a as C}from"./home.CDDtgVUx.js";import{r as y}from"./uni-app.es.C71S0I2S.js";import{_ as j,a as k,b as S}from"./speed.BCEs_Q6L.js";const v=w({name:"uniLink",props:{href:{type:String,default:""},text:{type:String,default:""},download:{type:String,default:""},showUnderLine:{type:[Boolean,String],default:!0},copyTips:{type:String,default:"已自动复制网址，请在手机浏览器里粘贴该网址"},color:{type:String,default:"#999999"},fontSize:{type:[Number,String],default:14}},computed:{isShowA(){return this._isH5=!0,!(!this.isMail()&&!this.isTel()||!0!==this._isH5)}},created(){this._isH5=null},methods:{isMail(){return this.href.startsWith("mailto:")},isTel(){return this.href.startsWith("tel:")},openURL(){window.open(this.href)},makePhoneCall(t){e({phoneNumber:t})}}},[["render",function(e,_,f,u,x,g){const h=d;return g.isShowA?(t(),a("a",{key:0,class:l(["uni-link",{"uni-link--withline":!0===f.showUnderLine||"true"===f.showUnderLine}]),href:f.href,style:i({color:f.color,fontSize:f.fontSize+"px"}),download:f.download},[s(e.$slots,"default",{},(()=>[c(o(f.text),1)]),!0)],14,["href","download"])):(t(),n(h,{key:1,class:l(["uni-link",{"uni-link--withline":!0===f.showUnderLine||"true"===f.showUnderLine}]),style:i({color:f.color,fontSize:f.fontSize+"px"}),onClick:g.openURL},{default:r((()=>[s(e.$slots,"default",{},(()=>[c(o(f.text),1)]),!0)])),_:3},8,["class","style","onClick"]))}],["__scopeId","data-v-44511933"]]);const B=w({data:()=>({src:"https://beian.miit.gov.cn/",appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui",isChinese:_("isChinese")}),onShow:function(){let{statusBarHeight:e}=f();e>0&&(this.appStatusBarHeight=40+e)},methods:{goCreatePage(){u({url:"/pages/tob/tob17Create"})},onLeftTab(){u({url:"/pages/index/index"})},onHomeTab(){u({url:"/pages/index/index"})},onMeTab(){u({url:"/pages/tob/tob15Me"})}}},[["render",function(e,a,s,l,o,d){const _=b,f=g,u=y(x("uni-link"),v);return t(),n(f,{class:"flex column alignCenter bg_div"},{default:r((()=>[h(f,{class:"flex row justifyBetween alignCenter header_div",style:i("margin-top:"+o.appStatusBarHeight+"rpx")},{default:r((()=>[h(f,{class:"flex row alignCenter",onClick:a[0]||(a[0]=e=>d.onLeftTab())},{default:r((()=>[h(_,{class:"header_img",src:C}),h(f,{class:"title"},{default:r((()=>[c("Deploy AI")])),_:1})])),_:1}),h(f,{class:"flex row justifyCenter alignCenter tab_div"},{default:r((()=>[h(f,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[1]||(a[1]=e=>d.onHomeTab())},{default:r((()=>[h(_,{class:"tab_img",src:C}),h(f,{class:"tab_label"},{default:r((()=>[c("complaint")])),_:1})])),_:1}),h(f,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[2]||(a[2]=e=>d.onMeTab())},{default:r((()=>[h(_,{class:"tab_img",src:j}),h(f,{class:"tab_label"},{default:r((()=>[c("me")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),h(f,{class:"flex column alignCenter div_content"},{default:r((()=>[o.isChinese?(t(),n(f,{key:0,class:"text1"},{default:r((()=>[c("深圳布林科技有限公司")])),_:1})):m("",!0),h(f,{class:"text2"},{default:r((()=>[c("快速创建")])),_:1}),h(f,{class:"text2"},{default:r((()=>[c("你的AI产品")])),_:1}),h(f,{class:"text3"},{default:r((()=>[c("将Comfyui工作流一键转化为Web/H5/小")])),_:1}),h(f,{class:"text4"},{default:r((()=>[c("程序/API，快速变现")])),_:1}),h(f,{class:"btn1"},{default:r((()=>[c("安装ComfyUI插件生成")])),_:1}),h(f,{class:"text5"},{default:r((()=>[c("您也可以选择云端转换：")])),_:1}),h(f,{class:"text6"},{default:r((()=>[c("上传或选择工作流模版转换为网页(后续可更换工作流）")])),_:1}),h(f,{class:"flex row wrap card2_div"},{default:r((()=>[h(f,{class:"flex column card2"},{default:r((()=>[h(f,{class:"flex row alignCenter card2_item"},{default:r((()=>[h(_,{class:"product_img",src:k}),h(f,{class:"flex column justifyBetween alignCenter card2_right_item"},{default:r((()=>[h(f,{class:"product_value_label"},{default:r((()=>[c("文字生成图片2")])),_:1}),h(f,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[3]||(a[3]=e=>d.goCreatePage())},{default:r((()=>[h(_,{class:"btn_img",src:S}),h(f,{class:"btn_text"},{default:r((()=>[c("立即启用")])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex row justifyBetween wrap card2_item2"},{default:r((()=>[h(f,{class:"flex row justifyBetween card2_right_item"},{default:r((()=>[h(f,{class:"card2_right_label"},{default:r((()=>[p("span",{class:"card2_right_head"},"预览URL:"),c(" https://xxx.xxx.com.xxx… ")])),_:1}),h(f,{class:"card2_right_copy"},{default:r((()=>[c("复制预览")])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex column card2"},{default:r((()=>[h(f,{class:"flex row alignCenter card2_item"},{default:r((()=>[h(_,{class:"product_img",src:k}),h(f,{class:"flex column justifyBetween alignCenter card2_right_item"},{default:r((()=>[h(f,{class:"product_value_label"},{default:r((()=>[c("文字生成图片2")])),_:1}),h(f,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[4]||(a[4]=e=>d.goCreatePage())},{default:r((()=>[h(_,{class:"btn_img",src:S}),h(f,{class:"btn_text"},{default:r((()=>[c("立即启用")])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex row justifyBetween wrap card2_item2"},{default:r((()=>[h(f,{class:"flex row justifyBetween card2_right_item"},{default:r((()=>[h(f,{class:"card2_right_label"},{default:r((()=>[p("span",{class:"card2_right_head"},"预览URL:"),c(" https://xxx.xxx.com.xxx… ")])),_:1}),h(f,{class:"card2_right_copy"},{default:r((()=>[c("复制预览")])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex column card2"},{default:r((()=>[h(f,{class:"flex row alignCenter card2_item"},{default:r((()=>[h(_,{class:"product_img",src:k}),h(f,{class:"flex column justifyBetween alignCenter card2_right_item"},{default:r((()=>[h(f,{class:"product_value_label"},{default:r((()=>[c("文字生成图片2")])),_:1}),h(f,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[5]||(a[5]=e=>d.goCreatePage())},{default:r((()=>[h(_,{class:"btn_img",src:S}),h(f,{class:"btn_text"},{default:r((()=>[c("立即启用")])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex row justifyBetween wrap card2_item2"},{default:r((()=>[h(f,{class:"flex row justifyBetween card2_right_item"},{default:r((()=>[h(f,{class:"card2_right_label"},{default:r((()=>[p("span",{class:"card2_right_head"},"预览URL:"),c(" https://xxx.xxx.com.xxx… ")])),_:1}),h(f,{class:"card2_right_copy"},{default:r((()=>[c("复制预览")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),h(f,{class:"flex row justifyCenter alignCenter bottom_btn_div",onClick:a[6]||(a[6]=e=>d.goCreatePage())},{default:r((()=>[h(_,{class:"bottom_btn_img",src:S}),h(f,{class:"bottom_btn_text"},{default:r((()=>[c("立即在线创新")])),_:1})])),_:1})])),_:1}),o.isChinese?(t(),n(u,{key:0,href:o.src,text:"【粤ICP备2024312061号-2】",class:"mgT10",style:{"margin-bottom":"40px"}},null,8,["href"])):m("",!0)])),_:1})}],["__scopeId","data-v-5303cd43"]]);export{B as default};

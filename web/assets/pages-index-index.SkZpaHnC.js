import{i as e,o as t,c as i,w as o,a as l,n as a,b as s,t as n,r as c,d as u,e as p,f as d,I as r,g as f,s as g,h as m,j as h,l as _,k as C,m as x,p as w,q as k,u as v,v as y,x as L,y as T,F as b,z as D}from"./index-BSpGNWiH.js";import{_ as $}from"./http.cZeV5NND.js";import{r as P,_ as j,a as S}from"./speed.BRapscCq.js";import{m as H,f as I}from"./index.CF4oe3Rz.js";import{T as F,c as N}from"./index.UffdP6uz.js";import{_ as V}from"./note2.w3RVvWxD.js";const M={data:()=>({}),created(){this.popup=this.getParent()},methods:{getParent(e="uniPopup"){let t=this.$parent,i=t.$options.name;for(;i!==e;){if(t=t.$parent,!t)return!1;i=t.$options.name}return t}}},U={en:{"uni-popup.cancel":"cancel","uni-popup.ok":"ok","uni-popup.placeholder":"pleace enter","uni-popup.title":"Hint","uni-popup.shareTitle":"Share to"},"zh-Hans":{"uni-popup.cancel":"取消","uni-popup.ok":"确定","uni-popup.placeholder":"请输入","uni-popup.title":"提示","uni-popup.shareTitle":"分享到"},"zh-Hant":{"uni-popup.cancel":"取消","uni-popup.ok":"確定","uni-popup.placeholder":"請輸入","uni-popup.title":"提示","uni-popup.shareTitle":"分享到"}},{t:B}=e(U);const Z=$({name:"uniPopupDialog",mixins:[M],emits:["confirm","close","update:modelValue","input"],props:{inputType:{type:String,default:"text"},showClose:{type:Boolean,default:!0},modelValue:{type:[Number,String],default:""},placeholder:{type:[String,Number],default:""},type:{type:String,default:"error"},mode:{type:String,default:"base"},title:{type:String,default:""},content:{type:String,default:""},beforeClose:{type:Boolean,default:!1},cancelText:{type:String,default:""},confirmText:{type:String,default:""},maxlength:{type:Number,default:-1},focus:{type:Boolean,default:!0}},data:()=>({dialogType:"error",val:""}),computed:{okText(){return this.confirmText||B("uni-popup.ok")},closeText(){return this.cancelText||B("uni-popup.cancel")},placeholderText(){return this.placeholder||B("uni-popup.placeholder")},titleText(){return this.title||B("uni-popup.title")}},watch:{type(e){this.dialogType=e},mode(e){"input"===e&&(this.dialogType="info")},value(e){-1!=this.maxlength&&"input"===this.mode?this.val=e.slice(0,this.maxlength):this.val=e},val(e){this.$emit("update:modelValue",e)}},created(){this.popup.disableMask(),"input"===this.mode?(this.dialogType="info",this.val=this.value,this.val=this.modelValue):this.dialogType=this.type},methods:{onOk(){"input"===this.mode?this.$emit("confirm",this.val):this.$emit("confirm"),this.beforeClose||this.popup.close()},closeDialog(){this.$emit("close"),this.beforeClose||this.popup.close()},close(){this.popup.close()}}},[["render",function(e,f,g,m,h,_){const C=p,x=d,w=r;return t(),i(x,{class:"uni-popup-dialog"},{default:o((()=>[l(x,{class:"uni-dialog-title"},{default:o((()=>[l(C,{class:a(["uni-dialog-title-text",["uni-popup__"+h.dialogType]])},{default:o((()=>[s(n(_.titleText),1)])),_:1},8,["class"])])),_:1}),"base"===g.mode?(t(),i(x,{key:0,class:"uni-dialog-content"},{default:o((()=>[c(e.$slots,"default",{},(()=>[l(C,{class:"uni-dialog-content-text"},{default:o((()=>[s(n(g.content),1)])),_:1})]),!0)])),_:3})):(t(),i(x,{key:1,class:"uni-dialog-content"},{default:o((()=>[c(e.$slots,"default",{},(()=>[l(w,{class:"uni-dialog-input",maxlength:g.maxlength,modelValue:h.val,"onUpdate:modelValue":f[0]||(f[0]=e=>h.val=e),type:g.inputType,placeholder:_.placeholderText,focus:g.focus},null,8,["maxlength","modelValue","type","placeholder","focus"])]),!0)])),_:3})),l(x,{class:"uni-dialog-button-group"},{default:o((()=>[g.showClose?(t(),i(x,{key:0,class:"uni-dialog-button",onClick:_.closeDialog},{default:o((()=>[l(C,{class:"uni-dialog-button-text"},{default:o((()=>[s(n(_.closeText),1)])),_:1})])),_:1},8,["onClick"])):u("",!0),l(x,{class:a(["uni-dialog-button",g.showClose?"uni-border-left":""]),onClick:_.onOk},{default:o((()=>[l(C,{class:"uni-dialog-button-text uni-button-color"},{default:o((()=>[s(n(_.okText),1)])),_:1})])),_:1},8,["class","onClick"])])),_:1})])),_:3})}],["__scopeId","data-v-19f0223c"]]);const z=$({components:{TopDiv:F},data:()=>({isLogin:!0,href:"https://uniapp.dcloud.io/component/README?id=uniui",client_id:"80fd42e0-d652-4732-b209-e14edd0cc217",clientList:[],workflow_id:"",inviteCodeUrl:""}),onLoad(e){if("mp-weixin"!==f("uniPlatform")){let e=new URL(window.location.href).searchParams.get("token");e&&g("token",e)}e.client_id&&(this.client_id=e.client_id),e.workflow_id&&(this.workflow_id=e.workflow_id),this.getFlowsList(),this.inviteCodeUrl=window.location.origin+"#/pages/index/index"},onShow:function(){},methods:{inputDialogToggle(){this.$refs.inputDialog.open()},dialogInputConfirm(e){let t={workflow_id:this.client_id,comment:e};N(t).then((e=>{200==e.status&&(m({icon:"success",title:e.message}),this.$refs.inputDialog.close())}))},handleLogin(){if(f("token"))this.getFlowsList();else{var e=this;if("mp-weixin"===f("uniPlatform"))_({success(t){if(t.code){C({title:"加载中",mask:!0});var i=t.code;uni.getUserInfo({lang:"zh_CN",success:t=>{let o={};o.code=i,o.rawData=t.rawData,o.signature=t.signature,o.encryptedData=t.encryptedData,o.iv=t.iv,H(o).then((t=>{if(200!=t.status)return m({icon:"none",title:t.data.msg});g("token",t.data.token),m({icon:"success",title:"登录成功"}),e.handleLogin(),x()}))},fail:e=>(x(),m({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:e=>m({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else h({url:"/pages/toc/toc02Login"})}},getFlowsList(){I({client_id:this.client_id,workflow_id:this.workflow_id}).then((e=>{200==e.status&&(this.clientList=e.data||[])}))},goNextPage(e,t){if(f("token")){let i=e.workflow_fields.cs_img_nodes.length>0,o=e.workflow_fields.cs_text_nodes.length>0;w({url:t?"/pages/toc/toc27Create?id="+e.id+"&consuming="+e.consuming+"&fee="+e.fee+"&image="+i+"&text="+o:"/pages/index/index?workflow_id="+e.id})}else{var i=this;if("mp-weixin"===f("uniPlatform"))_({success(o){if(o.code){C({title:"加载中",mask:!0});var l=o.code;uni.getUserInfo({lang:"zh_CN",success:o=>{let a={};a.code=l,a.rawData=o.rawData,a.signature=o.signature,a.encryptedData=o.encryptedData,a.iv=o.iv,H(a).then((o=>{if(200!=o.status)return m({icon:"none",title:o.data.msg});g("token",o.data.token),m({icon:"success",title:"登录成功"}),i.goNextPage(e,t),x()}))},fail:e=>(x(),m({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:e=>m({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else w({url:"/pages/toc/toc02Login"})}},goHomePage(){h({url:"/pages/toc/toc27Create"})},goRecordPage(){h({url:"/pages/toc/toc24Record"})},copyText(e){k({data:e,success:()=>{m({title:"复制成功",icon:"success",duration:2e3})},fail:()=>{m({title:"复制失败",icon:"none"})}})}}},[["render",function(e,a,c,p,r,f){const g=v("TopDiv"),m=D,h=d,_=P(y("uni-popup-dialog"),Z),C=P(y("uni-popup"),j);return t(),i(h,{class:"flex column alignCenter bg_div"},{default:o((()=>[l(g),l(h,{class:"flex column alignCenter content_div"},{default:o((()=>[l(h,{class:"flex row wrap justifyCenter alignCenter content_item_div"},{default:o((()=>[0!==r.clientList[0].images.length?(t(),i(m,{key:0,class:"home_image",mode:"aspectFill",src:r.clientList[0].images[0].image},null,8,["src"])):u("",!0),l(h,{class:"flex column alignCenter contentDiv"},{default:o((()=>[l(h,{class:"text1 textAlign"},{default:o((()=>[s(n(r.clientList[0].title),1)])),_:1}),l(h,{class:"text3"},{default:o((()=>[s(n(r.clientList[0].gn_desc),1)])),_:1}),l(h,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[0]||(a[0]=e=>f.goNextPage(r.clientList[0],!0))},{default:o((()=>[l(m,{class:"btn_img",mode:"aspectFill",src:S}),l(h,{class:"btn_text"},{default:o((()=>[s(n(e.$t("start")),1)])),_:1})])),_:1}),l(h,{class:"flex row justifyBetween alignCenter options_div"},{default:o((()=>[l(h,{class:"flex column alignCenter options_item",onClick:f.inputDialogToggle},{default:o((()=>[l(m,{class:"options_item_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M22.3146%2016.4836L12.7484%2023.7636C12.3505%2024.0669%2011.8641%2024.2312%2011.3638%2024.2312H7.63841C6.70148%2024.2272%205.80452%2023.8512%205.14477%2023.1859C4.48502%2022.5206%204.11649%2021.6206%204.12021%2020.6836V5.85204C4.11649%204.91511%204.48502%204.01506%205.14477%203.3498C5.80452%202.68453%206.70148%202.30852%207.63841%202.30444H19.7106C20.6475%202.30852%2021.5445%202.68453%2022.2042%203.3498C22.864%204.01506%2023.2325%204.91511%2023.2288%205.85204V14.6342C23.229%2014.9921%2023.1466%2015.3451%2022.988%2015.6659C22.8295%2015.9866%2022.599%2016.2665%2022.3146%2016.4836Z'%20fill='%23019083'/%3e%3cpath%20d='M25.48%2019.0848L24.3012%2017.6288C24.173%2017.4688%2023.9869%2017.3658%2023.7832%2017.3422C23.5795%2017.3186%2023.3748%2017.3763%2023.2134%2017.5028L16.394%2022.785C16.2948%2022.8616%2016.2156%2022.9611%2016.163%2023.0748L15.3132%2024.8948C15.2506%2025.028%2015.2263%2025.1759%2015.2431%2025.3221C15.2599%2025.4683%2015.3172%2025.6068%2015.4084%2025.7222C15.4982%2025.8369%2015.6184%2025.9239%2015.7553%2025.9734C15.8922%2026.023%2016.0403%2026.0329%2016.1826%2026.0022L18.3568%2025.5486C18.4736%2025.5243%2018.5833%2025.4735%2018.6774%2025.4002L25.354%2020.209C25.4365%2020.1443%2025.5054%2020.0639%2025.5566%2019.9724C25.6078%2019.8809%2025.6404%2019.7801%2025.6524%2019.6759C25.6643%2019.5718%2025.6555%2019.4662%2025.6264%2019.3655C25.5973%2019.2648%2025.5485%2019.1708%2025.4828%2019.089L25.48%2019.0848Z'%20fill='%23A9FCF5'/%3e%3cpath%20d='M16.8238%2010.1738H10.1654C9.86837%2010.1738%209.58349%2010.0558%209.37345%209.8458C9.16341%209.63576%209.04541%209.35088%209.04541%209.05384C9.04541%208.7568%209.16341%208.47192%209.37345%208.26188C9.58349%208.05184%209.86837%207.93384%2010.1654%207.93384H16.8238C17.1209%207.93384%2017.4057%208.05184%2017.6158%208.26188C17.8258%208.47192%2017.9438%208.7568%2017.9438%209.05384C17.9438%209.35088%2017.8258%209.63576%2017.6158%209.8458C17.4057%2010.0558%2017.1209%2010.1738%2016.8238%2010.1738ZM16.8238%2015.8578H10.1654C9.86837%2015.8578%209.58349%2015.7398%209.37345%2015.5298C9.16341%2015.3198%209.04541%2015.0349%209.04541%2014.7378C9.04541%2014.4408%209.16341%2014.1559%209.37345%2013.9459C9.58349%2013.7358%209.86837%2013.6178%2010.1654%2013.6178H16.8238C17.1209%2013.6178%2017.4057%2013.7358%2017.6158%2013.9459C17.8258%2014.1559%2017.9438%2014.4408%2017.9438%2014.7378C17.9438%2015.0349%2017.8258%2015.3198%2017.6158%2015.5298C17.4057%2015.7398%2017.1209%2015.8578%2016.8238%2015.8578Z'%20fill='%23161622'/%3e%3c/svg%3e"}),l(h,{class:"options_item_text"},{default:o((()=>[s(n(e.$t("tocIndex_text4")),1)])),_:1})])),_:1},8,["onClick"]),l(h,{class:"flex column alignCenter options_item",onClick:a[1]||(a[1]=e=>f.goRecordPage())},{default:o((()=>[l(m,{class:"options_item_img",src:V}),l(h,{class:"options_item_text"},{default:o((()=>[s(n(e.$t("tocIndex_text3")),1)])),_:1})])),_:1}),l(h,{class:"flex column alignCenter options_item",onClick:a[2]||(a[2]=e=>f.copyText(r.inviteCodeUrl))},{default:o((()=>[l(m,{class:"options_item_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M13.9727%201.75C7.20508%201.75%201.72266%207.23242%201.72266%2014C1.72266%2020.7648%207.20781%2026.25%2013.9727%2026.25C20.7375%2026.25%2026.2227%2020.7648%2026.2227%2014C26.2227%207.23242%2020.7375%201.75%2013.9727%201.75ZM12.1461%2014C12.1461%2014.2789%2012.0887%2014.5469%2011.9875%2014.7902L15.3562%2017.0352C15.6844%2016.8027%2016.0863%2016.666%2016.5184%2016.666C17.6367%2016.666%2018.5445%2017.5738%2018.5445%2018.6922C18.5445%2019.8105%2017.6367%2020.7184%2016.5184%2020.7184C15.4%2020.7184%2014.4922%2019.8105%2014.4922%2018.6922C14.4922%2018.5363%2014.5113%2018.3859%2014.5441%2018.2383L10.9512%2015.843C10.6969%2015.9578%2010.4152%2016.0234%2010.1172%2016.0234C8.99883%2016.0234%208.09102%2015.1156%208.09102%2013.9973C8.09102%2012.8789%208.99883%2011.9711%2010.1172%2011.9711C10.4152%2011.9711%2010.6969%2012.0367%2010.9512%2012.1516L14.5441%209.75625C14.5113%209.61133%2014.4922%209.4582%2014.4922%209.30234C14.4922%208.18398%2015.4%207.27617%2016.5184%207.27617C17.6367%207.27617%2018.5445%208.18398%2018.5445%209.30234C18.5445%2010.4207%2017.6367%2011.3285%2016.5184%2011.3285C16.0863%2011.3285%2015.6844%2011.1918%2015.3562%2010.9594L11.9875%2013.2043C12.0887%2013.4531%2012.1461%2013.7184%2012.1461%2014Z'%20fill='%23019083'/%3e%3c/svg%3e"}),l(h,{class:"options_item_text"},{default:o((()=>[s(n(e.$t("tocIndex_text5")),1)])),_:1})])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),r.clientList.length>1?(t(),i(h,{key:0,class:"flex row wrap justifyCenter alignCenter bottom_div"},{default:o((()=>[(t(!0),L(b,null,T(r.clientList,((e,a)=>(t(),i(h,{key:e.id,onClick:t=>f.goNextPage(e,!1)},{default:o((()=>[0!==a?(t(),i(h,{key:0,class:"flex row bottom_item"},{default:o((()=>[l(m,{class:"bottom_item_img",mode:"aspectFill",src:e.images[0].image},null,8,["src"]),l(h,{class:"flex column justifyCenter rightDiv"},{default:o((()=>[l(h,{class:"bottom_item_label"},{default:o((()=>[s(n(e.title),1)])),_:2},1024),l(h,{class:"bottom_item_value"},{default:o((()=>[s(n(e.gn_desc),1)])),_:2},1024)])),_:2},1024)])),_:2},1024)):u("",!0)])),_:2},1032,["onClick"])))),128))])),_:1})):u("",!0),l(C,{ref:"inputDialog",type:"dialog"},{default:o((()=>[l(_,{ref:"inputClose",mode:"input",title:"投诉建议",placeholder:"请输入",onConfirm:f.dialogInputConfirm},null,8,["onConfirm"])])),_:1},512)])),_:1})}],["__scopeId","data-v-5d71dce6"]]);export{z as default};
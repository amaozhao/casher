import{b as t,n as e,d as a,r as s,e as l,J as i,f as n,w as o,i as u,o as c,j as d,k as r,m as _,t as p,p as f,q as g,F as h,u as y,x as m,v as b,y as x}from"./index-rhrdExhZ.js";import{_ as C}from"./uni-link.q6pZ_FqV.js";import{d as w,t as D,g as I,r as k}from"./index.Cp4K2WbV.js";import{_ as P}from"./uni-icons.C22uUJeP.js";import{d as v,e as T,g as j,f as S,_ as $}from"./browser.D9312iSU.js";import{P as L,_ as B}from"./index.CIXM9Cax.js";import{_ as A}from"./home.BkC5lZfE.js";import{_ as G,a as U}from"./speed.FiO8-Deg.js";import{_ as E}from"./_plugin-vue_export-helper.BCo6x5W8.js";const H=E({components:{Pay:L},data:()=>({appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui",templatelist:[],gpulist:[],templatesID:null,gpuID:null,account:null,powersID:null,powersList:[],powerValue:null,priceShow:{},durationTypeList:[],durationTypeArray:{}}),onLoad(t){t.id&&(this.templatesID=Number(t.id))},onShow:function(){this.getDurationType(),Promise.all([this.getTemplatesList(),this.getGpusList()]).then((t=>{this.getDurationPrice()})),this.getUserPower();let{statusBarHeight:e}=t();e>0&&(this.appStatusBarHeight=40+e)},methods:{handlepop(){this.$refs.popDialog.open()},handleClose(){this.$refs.popDialog.close()},goCpuProduct(){e({url:"/pages/tob/tob18Product"})},getDurationPrice(){let t={gpu_config_id:this.gpuID,template_id:this.templatesID};v(t).then((t=>{this.durationTypeList=t.data.result,this.durationTypeArray=this.durationTypeList.find((t=>t.select)),this.getClculatePrice()}))},getDurationType(){T().then((t=>{this.durationTypeList=t.data.durationTypes}))},async goProductPage(){if(await this.getUserPower(),this.account>=this.priceShow.amount){let t={gpu_config_id:this.gpuID,template_id:this.templatesID,billing_type:this.durationTypeArray.type};w(t).then((t=>{2e4==t.code&&(a({icon:"success",title:"实例创建成功"}),s({url:"/pages/tob/tob18Product"}))}))}else this.$refs.pay.goProductPage()},goPay(){this.$refs.popup.close(),s({url:"/pages/tob/tob18Product"})},getUserPower(){j().then((t=>{2e4==t.code&&(this.account=t.data.account)}))},onLeftTab(){s({url:"/pages/index/index"})},onHomeTab(){s({url:"/pages/index/index"})},onMeTab(){s({url:"/pages/tob/tob15Me"})},async getTemplatesList(){await D().then((t=>{2e4===t.code&&(this.templatelist=t.data.templates,this.templatesID=this.templatesID?this.templatesID:this.templatelist[0].ID)}))},async getGpusList(){await I().then((t=>{2e4===t.code&&(this.gpulist=t.data.gpus,this.gpuID=this.gpulist.find((t=>"available"==t.Status)).ID)}))},templateChange(t){this.templatesID=t.ID,this.getClculatePrice()},gpuChange(t){if("sold_out"==t.Status||"in_maintenance"==t.Status)return a({icon:"none",title:`当前GPU${"sold_out"==t.Status?"已售完":"在维护"}，请选择其他模块`});this.gpuID=t.ID,this.getClculatePrice()},durationTypeChange(t){if(t.isSoldOut)return a({icon:"none",title:"当前模块已售完，请选择其他模块"});this.durationTypeArray=t,this.getClculatePrice()},getClculatePrice(){let t={gpu_config_id:this.gpuID,template_id:this.templatesID,duration_type:this.durationTypeArray.type};S(t).then((t=>{2e4==t.code&&(this.priceShow=t.data)}))}}},[["render",function(t,e,a,s,w,D){const I=b,v=u,T=k(l("uni-link"),C),j=k(l("uni-icons"),P),S=i("Pay"),L=k(l("uni-popup"),$);return c(),n(v,{class:"flex column alignCenter bg_div"},{default:o((()=>[d(v,{class:"flex row justifyBetween alignCenter header_div",style:_("margin-top:"+w.appStatusBarHeight+"rpx")},{default:o((()=>[d(v,{class:"flex row alignCenter",onClick:e[0]||(e[0]=t=>D.onLeftTab())},{default:o((()=>[d(I,{class:"header_img",src:A}),d(v,{class:"title"},{default:o((()=>[r("Deploy AI")])),_:1})])),_:1}),d(v,{class:"flex row justifyCenter alignCenter tab_div"},{default:o((()=>[d(v,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:e[1]||(e[1]=t=>D.goCpuProduct())},{default:o((()=>[d(I,{class:"tab_img",src:A}),d(v,{class:"tab_label"},{default:o((()=>[r("complaint")])),_:1})])),_:1}),d(v,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:e[2]||(e[2]=t=>D.onMeTab())},{default:o((()=>[d(I,{class:"tab_img",src:G}),d(v,{class:"tab_label"},{default:o((()=>[r("me")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),d(v,{class:"text1"},{default:o((()=>[r(p(t.$t("14_text1")),1)])),_:1}),d(v,{class:"text3"},{default:o((()=>[r(p(t.$t("14_text3")),1)])),_:1}),d(v,{class:"text4"},{default:o((()=>[r(p(t.$t("14_text4")),1)])),_:1}),d(v,{class:"text5"},{default:o((()=>[r(p(t.$t("14_text5")),1)])),_:1}),d(v,{class:"flex row justifyCenter wrap tab_content_div"},{default:o((()=>[(c(!0),f(h,null,g(w.templatelist,((e,a)=>(c(),n(v,{class:"card1",key:e.ID,onClick:t=>D.templateChange(e),style:_(w.templatesID==e.ID?"border: 5px solid #019083;":"border : unset")},{default:o((()=>[d(v,{class:"flex row justifyBetween alignStart"},{default:o((()=>[d(v,{class:"card1_title"},{default:o((()=>[r(p(e.Title)+" ",1),m("span",{class:"red"},"（"+p(e.Subtitle)+"）",1)])),_:2},1024),w.templatesID==e.ID?(c(),n(I,{key:0,class:"check_img",src:B})):y("",!0)])),_:2},1024),d(v,{class:"card1_value"},{default:o((()=>[r(p(e.Description),1)])),_:2},1024),d(v,{class:"card1_value"},{default:o((()=>[r(p(t.$t("webCreate_text2"))+"：",1)])),_:1}),d(v,{class:"card1_value color_main"},{default:o((()=>[d(T,{class:"custom-link",href:e.ProjectLink,text:e.ProjectLink},null,8,["href","text"])])),_:2},1024),d(v,{class:"flex justifyBetween card1_value2"},{default:o((()=>[d(v,null,{default:o((()=>[r(p(e.UpdateKey),1)])),_:2},1024),d(v,null,{default:o((()=>[r(p(e.UpdateValue),1)])),_:2},1024)])),_:2},1024)])),_:2},1032,["onClick","style"])))),128))])),_:1}),d(v,{class:"text6"},{default:o((()=>[r(p(t.$t("14_Choose_machine")),1)])),_:1}),d(v,{class:"flex row justifyCenter alignEnd wrap tab_content_div"},{default:o((()=>[(c(!0),f(h,null,g(w.gpulist,((e,a)=>(c(),n(v,{key:e.ID,onClick:t=>D.gpuChange(e)},{default:o((()=>["sold_out"==e.Status?(c(),n(v,{key:0,class:"sale_out"},{default:o((()=>[r(p(t.$t("14_sold_out")),1)])),_:1})):"in_maintenance"==e.Status?(c(),n(v,{key:1,class:"sale_out"},{default:o((()=>[r(p(t.$t("15_sold_out")),1)])),_:1})):y("",!0),d(v,{class:"flex column tab_content_item"},{default:o((()=>[d(v,{class:"flex row justifyBetween alignCenter"},{default:o((()=>[d(v,{class:"skewCss"}),d(v,{class:"tab_content_title"},{default:o((()=>[r(p(e.GpuType),1)])),_:2},1024),w.gpuID==e.ID?(c(),n(I,{key:0,class:"check_img",src:B})):y("",!0)])),_:2},1024),d(v,{class:"flex column tab_content_row"},{default:o((()=>[d(v,{class:"flex row alignCenter"},{default:o((()=>[d(v,{class:"tab_content_value"},{default:o((()=>[r(p(e.VramGB)+"G",1)])),_:2},1024),d(v,{class:"tab_content_label"},{default:o((()=>[r(p(t.$t("14_video_memory")),1)])),_:1})])),_:2},1024),d(v,{class:"flex row alignCenter"},{default:o((()=>[d(v,{class:"tab_content_value"},{default:o((()=>[r(p(e.MemoryGB)+"G",1)])),_:2},1024),d(v,{class:"tab_content_label"},{default:o((()=>[r(p(t.$t("14_memory")),1)])),_:1})])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1032,["onClick"])))),128))])),_:1}),d(v,{class:"divider"}),d(v,{class:"bottomDiv alignCenter"},{default:o((()=>[d(v,{class:"flex wrap justifyEnd"},{default:o((()=>[d(v,{style:{width:"100%"},class:"flex wrap justifyEnd price_div"},{default:o((()=>[w.priceShow.discountInfo?(c(),n(v,{key:0,class:"pay_btn flex alignCenter justifyCenter",onClick:D.handlepop},{default:o((()=>[d(v,null,{default:o((()=>[r("1分钱/小时体验券（7X24小时）")])),_:1}),d(j,{type:"info",size:"20"})])),_:1},8,["onClick"])):y("",!0)])),_:1}),d(v,{class:"flex row justifyEnd alignCenter price_div"},{default:o((()=>[d(v,{class:"price_label"},{default:o((()=>[r("（"+p(w.priceShow.amount)+p(t.$t("webCreate_text1"))+"/"+p(w.durationTypeArray.tag)+"）",1)])),_:1}),d(v,{class:"price_value"},{default:o((()=>[r(p(w.priceShow.currencySymbol)+" "+p(w.priceShow.currencyAmount)+"/"+p(w.durationTypeArray.tag),1)])),_:1})])),_:1})])),_:1}),d(v,{class:"bottomBtnDiv"},{default:o((()=>[d(v,{class:"flex row alignCenter bottom_div"},{default:o((()=>[d(v,{class:"flex alignEnd justifyBetween row sale_type_div"},{default:o((()=>[(c(!0),f(h,null,g(w.durationTypeList,((e,a)=>(c(),n(v,{class:"flex column alignCenter sale_type_item",key:e.type,onClick:t=>D.durationTypeChange(e)},{default:o((()=>[e.isSoldOut?(c(),n(v,{key:0,class:"sale_out"},{default:o((()=>[r(p(t.$t("14_sold_out")),1)])),_:1})):y("",!0),e.discountInfo?(c(),n(v,{key:1,class:"sale_out discountDiv"},{default:o((()=>[r("1分/小时")])),_:1})):y("",!0),d(v,{class:x(["sale_type",w.durationTypeArray.type==e.type?"sale_type_active":""])},{default:o((()=>[r(p(t.$t("webCreate_text3"))+p(e.tag)+p(t.$t("webCreate_text4")),1)])),_:2},1032,["class"])])),_:2},1032,["onClick"])))),128))])),_:1})])),_:1}),d(v,{class:"flex row justifyCenter alignCenter btn_div",onClick:e[3]||(e[3]=t=>D.goProductPage())},{default:o((()=>[d(I,{class:"btn_img",src:U}),d(v,{class:"btn_text"},{default:o((()=>[r(p(t.$t("start")),1)])),_:1})])),_:1})])),_:1})])),_:1}),d(S,{ref:"pay"},null,512),d(L,{ref:"popDialog",type:"dialog"},{default:o((()=>[d(v,{class:"popDialog"},{default:o((()=>[m("h3",null,"1分钱/小时专享体验券使用说明"),d(v,{class:"bold mgT10"},{default:o((()=>[r("亲爱的用户！您将享受前所未有的超值体验——只需 1 分钱/小时，开启高效 GPU 实例之旅！")])),_:1}),d(v,{class:"bold"},{default:o((()=>[r("体验券详情")])),_:1}),d(v,{class:"bold"},{default:o((()=>[r("1. 优惠内容：")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r("每张体验券提供 7 次 24 小时的 GPU 实例使用权，仅需 1 分钱/小时。")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r("每次使用都将扣除一次机会，不管是否使用满 24 小时。")])),_:1}),d(v,{class:"bold"},{default:o((()=>[r("2. 使用规则：")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[m("span",{class:"bold"},"每个自然周"),r(" 仅可使用 "),m("span",{class:"bold"},"1"),r(" 次。 ")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r(" 每次使用需新建或续用 GPU 实例，每周仅限 "),m("span",{class:"bold"},"1 个容器"),r(" 享受优惠。 ")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[m("span",{class:"bold"},"实例创建即消耗一次使用机会"),r(" ，不论实际使用时长。 ")])),_:1}),d(v,{class:"bold"},{default:o((()=>[r("3. 使用方式：")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r(" 未使用体验券的新用户，系统将在创建容器时 "),m("span",{class:"bold"},"默认推荐按小时付费方式"),r(" ，确保体验优惠。 ")])),_:1}),d(v,{class:"bold"},{default:o((()=>[r("温馨提示")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r("请合理规划每周的使用时间，避免浪费您的体验券机会。")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r("体验券自领取后有效期为7周，请尽早使用！")])),_:1}),d(v,{class:"textIndent"},{default:o((()=>[r("立即开启您的高性能之旅，享受每小时仅需1分钱的强大算力支持吧！")])),_:1}),d(v,{class:"closeBtn",onClick:D.handleClose},{default:o((()=>[r("知道啦")])),_:1},8,["onClick"])])),_:1})])),_:1},512)])),_:1})}],["__scopeId","data-v-b9a3e37d"]]);export{H as default};
import{l as e,k as a,c as t,w as l,i as s,o as c,d as u,e as n,x as o,v as i,f as r,h as _,F as d,t as f,j as p,L as m,A as g}from"./index-BnGBZ2Zx.js";import{r as b}from"./httpUtil.DN75PITx.js";import{_ as h}from"./home.zzgta-u4.js";import{_ as y}from"./me2.D5gY6gCa.js";import{_ as x,a as C,b as v}from"./connect.CZokdgBA.js";import{_ as w}from"./check.DZEWLAjS.js";import{_ as j}from"./_plugin-vue_export-helper.BCo6x5W8.js";const k=j({data:()=>({appStatusBarHeight:0,fee:{},gpus:[],priceArr:[],templates:[],clculateVo:{template_id:1,gpu_config_id:1,duration_type:"minute"},href:"https://uniapp.dcloud.io/component/README?id=uniui",durationMap:{minute:"分钟",hourly:"小时",weekly:"周",monthly:"月"}}),watch:{clculateVo:{handler(e,a){b({url:"gpu/gpucloud-fetch/",method:"POST",data:{method:"post",url:"/api/powers/clculate-price",data:e}}).then((e=>{this.fee=e.data})),console.log("User object changed:",e,a)},deep:!0}},onShow(){let{statusBarHeight:a}=e();a>0&&(this.appStatusBarHeight=40+a),b({url:"gpu/gpucloud-fetch/",method:"POST",data:{method:"get",url:"/api/capps/templates"}}).then((e=>{var a;this.templates=null==(a=e.data)?void 0:a.templates})),b({url:"gpu/gpucloud-fetch/",method:"POST",data:{method:"get",url:"/api/capps/gpus"}}).then((e=>{var a;this.gpus=null==(a=e.data)?void 0:a.gpus})),b({url:"gpu/gpucloud-fetch/",method:"POST",data:{method:"post",url:"/api/powers/clculate-duration-price",data:{gpu_config_id:1,template_id:1}}}).then((e=>{var a;this.priceArr=null==(a=e.data)?void 0:a.result}))},methods:{selectTemplate(e){this.clculateVo.template_id=e.ID},selectGpu(e){this.clculateVo.gpu_config_id=e.ID},selectPrice(e){this.clculateVo.duration_type=e.type},goProductPage(){a({url:"/pages/tob/tob18Product"})},onLeftTab(){a({url:"/pages/index/index"})},onHomeTab(){a({url:"/pages/tob/tob13Index"})},onMeTab(){a({url:"/pages/tob/tob15Me"})}}},[["render",function(e,a,b,j,k,T){const B=p,P=s;return c(),t(P,{class:"flex column alignCenter bg_div"},{default:l((()=>[u(P,{class:"flex row justifyBetween alignCenter header_div",style:o("margin-top:"+k.appStatusBarHeight+"rpx")},{default:l((()=>[u(P,{class:"flex row alignCenter",onClick:a[0]||(a[0]=e=>T.onLeftTab())},{default:l((()=>[u(B,{class:"header_img",src:h}),u(P,{class:"title"},{default:l((()=>[n(" Deploy AI ")])),_:1})])),_:1}),u(P,{class:"flex row justifyCenter alignCenter tab_div"},{default:l((()=>[u(P,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[1]||(a[1]=e=>T.onHomeTab())},{default:l((()=>[u(B,{class:"tab_img",src:h}),u(P,{class:"tab_label"},{default:l((()=>[n(" complaint ")])),_:1})])),_:1}),u(P,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[2]||(a[2]=e=>T.onMeTab())},{default:l((()=>[u(B,{class:"tab_img",src:y}),u(P,{class:"tab_label"},{default:l((()=>[n(" me ")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),u(P,{class:"flex column alignCenter div_content"},{default:l((()=>[u(P,{class:"text1"},{default:l((()=>[n(" 我的实例 ")])),_:1}),u(P,{class:"flex row wrap card1"},{default:l((()=>[u(P,{class:"flex column justifyStart card1_item"},{default:l((()=>[u(P,{class:"card1_item_title"},{default:l((()=>[n(" ComfyUI最新版"),i("span",{class:"red"},"（官方推荐）")])),_:1}),u(P,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:l((()=>[u(P,{class:"card1_item_value"},{default:l((()=>[n(" RTX3090 ")])),_:1}),u(P,{class:"flex column"},{default:l((()=>[u(P,{class:"card1_item_value2"},{default:l((()=>[i("span",{class:"color_green"},"24G"),n(" 显存 ")])),_:1}),u(P,{class:"card1_item_value2"},{default:l((()=>[i("span",{class:"color_green"},"64G"),n(" 空间 ")])),_:1})])),_:1})])),_:1}),u(P,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:l((()=>[u(P,{class:"card1_item_value2"},{default:l((()=>[n(" 到期时间 ")])),_:1}),u(P,{class:"card1_item_value2"},{default:l((()=>[n(" 2024.8.13 ")])),_:1})])),_:1})])),_:1}),u(P,{class:"flex column justifyBetween alignCenter card1_item"},{default:l((()=>[u(P,{class:"card1_item_btn"},{default:l((()=>[n(" 打开comfyUI ")])),_:1}),u(P,{class:"flex row option_btn_div"},{default:l((()=>[u(P,{class:"flex column alignCenter option_item"},{default:l((()=>[u(B,{class:"option_img",src:x}),u(P,{class:"option_label"},{default:l((()=>[n("文件管理")])),_:1})])),_:1}),u(P,{class:"flex column alignCenter option_item"},{default:l((()=>[u(B,{class:"option_img",src:C}),u(P,{class:"option_label"},{default:l((()=>[n("关机")])),_:1})])),_:1}),u(P,{class:"flex column alignCenter option_item"},{default:l((()=>[u(B,{class:"option_img",src:v}),u(P,{class:"option_label"},{default:l((()=>[n("释放")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),u(P,{class:"flex row justifyCenter alignCenter wrap btn_view"},{default:l((()=>[u(P,{class:"btn1",onClick:a[3]||(a[3]=e=>T.goProductPage())},{default:l((()=>[n(" 创建新的实例 ")])),_:1}),u(P,{class:"btn2",onClick:a[4]||(a[4]=e=>T.goProductPage())},{default:l((()=>[n(" 工作流转Web ")])),_:1})])),_:1}),u(P,{class:"text2"},{default:l((()=>[n(" 应用推荐 ")])),_:1}),(c(!0),r(d,null,_(k.templates,(e=>(c(),t(P,{class:m(["card2",{card2_active:k.clculateVo.template_id==e.ID}]),onClick:a=>T.selectTemplate(e)},{default:l((()=>[u(P,{class:"flex row justifyBetween alignStart"},{default:l((()=>[u(P,{class:"card2_title"},{default:l((()=>[n(f(e.Title)+" ",1),i("span",{class:"red"},"（"+f(e.Subtitle)+"）",1)])),_:2},1024)])),_:2},1024),u(P,{class:"card2_value"},{default:l((()=>[n(f(e.Description),1)])),_:2},1024),u(P,{class:"card2_value"},{default:l((()=>[n(" 移植自官方项目： ")])),_:1}),u(P,{class:"card2_value color_main"},{default:l((()=>[n(f(e.ProjectLink),1)])),_:2},1024),u(P,{class:"flex justifyBetween card2_value2"},{default:l((()=>[u(P,null,{default:l((()=>[n(f(e.UpdateKey),1)])),_:2},1024),u(P,null,{default:l((()=>[n(f(e.UpdateValue),1)])),_:2},1024)])),_:2},1024)])),_:2},1032,["class","onClick"])))),256)),u(P,{class:""},{default:l((()=>[n(" 选择适合您需求的机器类型 ")])),_:1}),u(P,{class:"flex row justifyCenter alignEnd wrap tab_content_div"},{default:l((()=>[(c(!0),r(d,null,_(k.gpus,(e=>(c(),t(P,{class:"",onClick:a=>T.selectGpu(e)},{default:l((()=>["sold_out"==e.Status?(c(),t(P,{key:0,class:"sale_out"},{default:l((()=>[n("售罄")])),_:1})):g("",!0),u(P,{class:"flex column tab_content_item"},{default:l((()=>[u(P,{class:"flex row justifyBetween alignCenter"},{default:l((()=>[u(P,{class:"skewCss"}),u(P,{class:"tab_content_title"},{default:l((()=>[n(f(e.GpuType),1)])),_:2},1024),u(B,{class:"check_img",src:w})])),_:2},1024),u(P,{class:"flex column tab_content_row"},{default:l((()=>[u(P,{class:"flex row alignCenter"},{default:l((()=>[u(P,{class:"tab_content_value"},{default:l((()=>[n(f(e.VramGB),1)])),_:2},1024),u(P,{class:"tab_content_label"},{default:l((()=>[n("显存")])),_:1})])),_:2},1024),u(P,{class:"flex row alignCenter"},{default:l((()=>[u(P,{class:"tab_content_value"},{default:l((()=>[n(f(e.MemoryGB),1)])),_:2},1024),u(P,{class:"tab_content_label"},{default:l((()=>[n("内存")])),_:1})])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1032,["onClick"])))),256))])),_:1}),u(P,{class:"bottomDiv alignCenter"},{default:l((()=>[u(P,{class:"flex column wrap justifyEnd"},{default:l((()=>[u(P,{class:"flex wrap justifyEnd price_div"},{default:l((()=>[u(P,{class:"pay_btn flex alignCenter justifyCenter"},{default:l((()=>[u(P,{class:""},{default:l((()=>[n("1分钱/小时体验券（7X24小时）")])),_:1}),u(P,{class:"uni-icons uniui-info"})])),_:1})])),_:1}),u(P,{class:"flex row justifyEnd alignCenter price_div"},{default:l((()=>[u(P,{class:"price_label"},{default:l((()=>[n("( "+f(k.fee.amount)+"算力值/ "+f(k.durationMap[k.fee.durationType])+" )",1)])),_:1}),u(P,{class:"price_value"},{default:l((()=>[n(f(k.fee.currencySymbol)+" "+f(k.fee.currencyAmount)+" / "+f(k.durationMap[k.fee.durationType]),1)])),_:1})])),_:1}),u(P,{class:""})])),_:1}),u(P,{class:"bottomBtnDiv bottom_div flex row alignEnd"},{default:l((()=>[(c(!0),r(d,null,_(k.priceArr,(e=>(c(),t(P,{class:"flex column alignCenter",onClick:a=>T.selectPrice(e)},{default:l((()=>[e.discountInfo?(c(),t(P,{key:0,class:"sale_out discountDiv"},{default:l((()=>[n(" 1分钱/小时 ")])),_:1})):g("",!0),u(P,{class:m(["flex column alignCenter sale_type_item sale_type",{sale_type_active:k.clculateVo.duration_type==e.type}])},{default:l((()=>[n(" 按"+f(e.tag)+"计费 ",1)])),_:2},1032,["class"])])),_:2},1032,["onClick"])))),256))])),_:1}),u(P,{class:"flex row justifyCenter alignCenter btn_div"},{default:l((()=>[n(" 立即启动 ")])),_:1})])),_:1})])),_:1})])),_:1})}],["__scopeId","data-v-5aec3b38"]]);export{k as default};
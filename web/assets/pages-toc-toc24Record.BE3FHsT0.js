import{r as e,n as s,c as t,w as a,i as l,o,a as i,b as n,A as d,B as c,F as r,j as u,d as _}from"./index-EY3OXLqc.js";import{r as f}from"./httpUtil.BVq9Uu_k.js";import{_ as g}from"./load.DB4DbRB_.js";import{_ as p}from"./_plugin-vue_export-helper.BCo6x5W8.js";const m=p({data:()=>({isLogin:!1,historyList:[],href:"https://uniapp.dcloud.io/component/README?id=uniui"}),onShow:function(){f({url:"task/history/",method:"GET"}).then((e=>{this.historyList=e.data})),console.log("index Show")},methods:{goHomePage(){e({url:"/pages/index/index"})},goNextPage(){e({url:"/pages/toc/toc35Index"})},goProduct(e){s({url:"/pages/toc/toc25Product?jilu_id="+e.jilu_id})}}},[["render",function(e,s,f,p,m,x){const h=l,w=_;return o(),t(h,{class:"flex column alignCenter bg_div"},{default:a((()=>[i(h,{class:"flex row justifyBetween alignCenter header_div"},{default:a((()=>[i(h,{class:"flex row alignCenter title_content_view",onClick:s[0]||(s[0]=e=>x.goHomePage())},{default:a((()=>[i(h,{class:"title_btn"},{default:a((()=>[n(" 创建 ")])),_:1}),i(h,{class:"title_label"},{default:a((()=>[n(" 在Deploy上创建一个 Ai 应用 ")])),_:1})])),_:1})])),_:1}),i(h,{class:"header_btn",onClick:s[1]||(s[1]=e=>x.goNextPage())},{default:a((()=>[n(" 前往主页，查看更多好玩 ")])),_:1}),i(h,{class:"flex wrap row justifyCenter product_div"},{default:a((()=>[(o(!0),d(r,null,c(m.historyList,(e=>(o(),t(h,{class:"loding_div"},{default:a((()=>["success"==e.status?(o(),t(w,{key:0,class:"product_image",mode:"aspectFill",src:e.result,onClick:s=>x.goProduct(e)},null,8,["src","onClick"])):(o(),t(h,{key:1,class:"flex column alignCenter loding_box"},{default:a((()=>[i(w,{class:"load_image",src:g}),i(h,{class:"loding_text"},{default:a((()=>[n(" 生成中 ")])),_:1}),i(h,{class:"loding_text2"},{default:a((()=>[n(" 大约还需 "),u("span",{class:"loding_value"},"45"),n(" 秒 ….. ")])),_:1}),i(h,{class:"notice"},{default:a((()=>[n(" 一小时内未生成成功, ")])),_:1}),i(h,{class:"notice2"},{default:a((()=>[n(" 系统自动退款 ")])),_:1})])),_:1}))])),_:2},1024)))),256))])),_:1})])),_:1})}],["__scopeId","data-v-5c962b14"]]);export{m as default};

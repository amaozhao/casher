import{r as e,y as t,z as o,c as s,w as a,i as l,o as i,a as c,b as n,d as r}from"./index-CYB8ynpA.js";import{r as d}from"./httpUtil.6tx-ljDa.js";import{_ as u}from"./record.bSuQS5ND.js";import{_}from"./delete.okYJrUrz.js";import{_ as p}from"./_plugin-vue_export-helper.BCo6x5W8.js";const f=p({data:()=>({product:{},href:"https://uniapp.dcloud.io/component/README?id=uniui"}),onLoad(e){console.log("option25",e),d({url:"task/history/detail/",method:"GET",data:{jilu_id:e.jilu_id}}).then((e=>{this.product=e.data}))},onShow:function(){console.log("index Show")},methods:{goHomePage(){e({url:"/pages/index/index"})},goRecordPage(){e({url:"/pages/toc/toc24Record"})},del(){d({url:"task/history/delete/"+this.product.id+"/",method:"DELETE",data:{id:this.product.id}}).then((o=>{t({title:"删除成功",icon:"none"}),setTimeout((()=>{e({url:"/pages/toc/toc24Record"})}),1e3)}))},share(){o({data:this.product.result,success:function(){console.log("success")}})}}},[["render",function(e,t,o,d,p,f){const g=l,m=r;return i(),s(g,{class:"flex column alignCenter bg_div"},{default:a((()=>[c(g,{class:"flex row justifyBetween alignCenter header_div"},{default:a((()=>[c(g,{class:"flex row alignCenter title_content_view",onClick:t[0]||(t[0]=e=>f.goHomePage())},{default:a((()=>[c(g,{class:"title_btn"},{default:a((()=>[n(" 创建 ")])),_:1}),c(g,{class:"title_label"},{default:a((()=>[n(" 在Deploy上创建一个 Ai 应用 ")])),_:1})])),_:1})])),_:1}),c(m,{class:"record_img",src:u,onClick:t[1]||(t[1]=e=>f.goRecordPage())}),c(m,{class:"product_image",src:p.product.result},null,8,["src"]),c(g,{class:"flex row alignCenter bottom_div"},{default:a((()=>[c(g,{class:"flex row justifyBetween alignCenter option_div"},{default:a((()=>[c(g,{class:"flex column alignCenter option_item"},{default:a((()=>[c(m,{class:"option_image",src:"/static/change.svg"}),c(g,{class:"option_text"},{default:a((()=>[n(" 重新生成 ")])),_:1})])),_:1}),c(g,{class:"flex column alignCenter option_item",onClick:f.del},{default:a((()=>[c(m,{class:"option_image",src:_}),c(g,{class:"option_text"},{default:a((()=>[n(" 删除作品 ")])),_:1})])),_:1},8,["onClick"]),c(g,{class:"flex column alignCenter option_item"},{default:a((()=>[c(m,{class:"option_image",src:"/static/download.svg"}),c(g,{class:"option_text"},{default:a((()=>[n(" 下载保存 ")])),_:1})])),_:1})])),_:1}),c(g,{class:"flex column justifyCenter alignCenter share_div",onClick:f.share},{default:a((()=>[c(m,{class:"option_image",src:"/static/share.svg"}),c(g,{class:"share_text"},{default:a((()=>[n(" 分享好友 ")])),_:1})])),_:1},8,["onClick"])])),_:1})])),_:1})}],["__scopeId","data-v-1199c389"]]);export{f as default};

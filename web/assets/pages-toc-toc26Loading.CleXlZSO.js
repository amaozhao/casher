import{b as t,r as e,c as o,w as s,i,o as a,d as l,e as n,t as c,q as d,m as r}from"./index-Bv58QUZ6.js";import{a as _}from"./index.PG0_jtA1.js";import{_ as g}from"./load.B3pZkcbV.js";import{_ as u}from"./_plugin-vue_export-helper.BCo6x5W8.js";import"./http.C00EEzHW.js";const x=u({data:()=>({isLogin:!1,href:"https://uniapp.dcloud.io/component/README?id=uniui",second:6,start:!0,timer:null,jilu_id:""}),onLoad(t){t.jilu_id&&(this.jilu_id=t.jilu_id)},onShow:function(){this.getResult()},methods:{getResult(){this.timer=setInterval((()=>{this.second>0&&(this.second--,console.log(this.second,"==="),_({jilu_id:this.jilu_id}).then((t=>{200==t.code&&(this.start=!1,this.goNextPage())})),(this.second<1||!this.start)&&(this.start=!1,t({icon:"none",title:"生成失败！"}),e({url:"/pages/index/index"}),this.clearTimer()))}),1e3)},clearTimer(){this.timer&&(clearInterval(this.timer),this.timer=null)},goHomePage(){e({url:"/pages/toc/toc27Create"})},goRecordPage(){e({url:"/pages/toc/toc24Record"})},goNextPage(){e({url:"/pages/toc/toc25Product"})}},beforeUnmount(){this.clearTimer()}},[["render",function(t,e,_,u,x,m){const f=i,h=r;return a(),o(f,{class:"flex column alignCenter bg_div"},{default:s((()=>[l(f,{class:"flex row justifyBetween alignCenter header_div"},{default:s((()=>[l(f,{class:"flex row alignCenter title_content_view",onClick:e[0]||(e[0]=t=>m.goHomePage())},{default:s((()=>[l(f,{class:"title_btn"},{default:s((()=>[n(c(t.$t("tocIndex_text1")),1)])),_:1}),l(f,{class:"title_label"},{default:s((()=>[n(c(t.$t("tocIndex_text2")),1)])),_:1})])),_:1}),l(f,{class:"title_btn2 xsHide",onClick:e[1]||(e[1]=t=>m.goRecordPage())},{default:s((()=>[n(c(t.$t("tocIndex_text3")),1)])),_:1})])),_:1}),l(f,{class:"flex column alignCenter loding_div"},{default:s((()=>[l(f,{class:"title_btn2 xsShow mgT20",onClick:e[2]||(e[2]=t=>m.goRecordPage())},{default:s((()=>[n(c(t.$t("tocIndex_text3")),1)])),_:1}),l(h,{class:"load_image",src:g}),l(f,{class:"loding_text textAlign"},{default:s((()=>[n(c(t.$t("tocLoading_text1"))+" ",1),d("span",{class:"loding_value"},c(x.second),1),n(" "+c(t.$t("tocLoading_text2"))+" ….. ",1)])),_:1})])),_:1}),l(f,{class:"notice textAlign"},{default:s((()=>[n(c(t.$t("tocLoading_text3")),1)])),_:1}),l(f,{class:"notice2"},{default:s((()=>[n(c(t.$t("tocLoading_text4")),1)])),_:1}),l(f,{class:"bottom_btn",onClick:e[3]||(e[3]=t=>m.goNextPage())},{default:s((()=>[n(c(t.$t("tocLoading_text5")),1)])),_:1})])),_:1})}],["__scopeId","data-v-ade8509c"]]);export{x as default};

import{j as s,u as t,c as o,w as a,f as e,o as i,a as n,b as r,t as d,x as l,y as c,F as u,d as g,z as p}from"./index-BSpGNWiH.js";import{i as f}from"./index.CF4oe3Rz.js";import{T as m}from"./index.UffdP6uz.js";import{_ as x}from"./http.cZeV5NND.js";const _=x({components:{TopDiv:m},data:()=>({isLogin:!1,proList:[]}),onShow:function(){this.getList(),console.log("index Show")},methods:{getList(){f().then((s=>{200==s.status&&(console.log(s.data,"==res.data"),this.proList=s.data||[])}))},goHomePage(){s({url:"/pages/index/index"})},goNextPage(t){s({url:"/pages/toc/toc25Product?id="+t})}}},[["render",function(s,f,m,x,_,h){const j=t("TopDiv"),L=e,b=p;return i(),o(L,{class:"flex column alignCenter bg_div"},{default:a((()=>[n(j),n(L,{class:"header_btn",onClick:f[0]||(f[0]=s=>h.goHomePage())},{default:a((()=>[r(d(s.$t("tocRecord_text1")),1)])),_:1}),n(L,{class:"product_div flex wrap justifyCenter"},{default:a((()=>[(i(!0),l(u,null,c(_.proList,((s,t)=>(i(),l(u,{key:s.id},[s.result?(i(),o(b,{key:0,class:"product_image",src:s.result,onClick:t=>h.goNextPage(s.id)},null,8,["src","onClick"])):g("",!0)],64)))),128))])),_:1})])),_:1})}],["__scopeId","data-v-d19003b8"]]);export{_ as default};
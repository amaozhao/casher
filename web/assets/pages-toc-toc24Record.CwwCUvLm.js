import{o as s,c as e,w as t,a,b as o,z as i,f as l,j as d,u as n,t as c,x as r,y as u,F as _,d as f}from"./index-DOOzXzrL.js";import{i as g}from"./index.DGzkNEGj.js";import{w as m,T as p}from"./index.Bpel1_5q.js";import{_ as x}from"./load.B3pZkcbV.js";import{_ as j}from"./home.hDAa9BDp.js";const h=j({components:{TopDiv:p,Record:j({props:{jilu_id:{type:String,default:""}},data:()=>({}),created(){},methods:{getworkInfo(){m({jilu_id:this.jilu_id}).then((s=>{s.status}))}}},[["render",function(d,n,c,r,u,_){const f=i,g=l;return s(),e(g,{class:"flex column alignCenter loding_div"},{default:t((()=>[a(f,{class:"load_image",src:x}),a(g,{class:"loding_text"},{default:t((()=>[o("生成中")])),_:1}),a(g,{class:"notice"},{default:t((()=>[o("一小时内未生成成功,")])),_:1}),a(g,{class:"notice2"},{default:t((()=>[o("系统自动退款")])),_:1})])),_:1})}],["__scopeId","data-v-125edbc2"]])},data:()=>({isLogin:!1,proList:[]}),onShow:function(){this.getList(),console.log("index Show")},methods:{getList(){g().then((s=>{200==s.status&&(this.proList=s.data||[])}))},goHomePage(){d({url:"/pages/index/index"})},goNextPage(s){d({url:"/pages/toc/toc25Product?id="+s})}}},[["render",function(d,g,m,p,j,h){const k=n("TopDiv"),v=l,b=n("Record"),y=i;return s(),e(v,{class:"flex column alignCenter bg_div"},{default:t((()=>[a(k),a(v,{class:"header_btn",onClick:g[0]||(g[0]=s=>h.goHomePage())},{default:t((()=>[o(c(d.$t("tocRecord_text1")),1)])),_:1}),a(v,{class:"product_div flex wrap justifyCenter"},{default:t((()=>[(s(!0),r(_,null,u(j.proList,((i,l)=>(s(),r(_,{key:i.id},["queue"==i.status?(s(),e(b,{key:0,jilu_id:i.jilu_id},null,8,["jilu_id"])):"fail"==i.status?(s(),e(v,{key:1,class:"flex column alignCenter loding_div"},{default:t((()=>[a(y,{class:"load_image",src:x}),a(v,{class:"loding_text"},{default:t((()=>[o("生成失败")])),_:1})])),_:1})):"success"==i.status?(s(),e(y,{key:2,mode:"aspectFill",class:"product_image",src:i.result,onClick:s=>h.goNextPage(i.jilu_id)},null,8,["src","onClick"])):f("",!0)],64)))),128))])),_:1})])),_:1})}],["__scopeId","data-v-4b281b2e"]]);export{h as default};

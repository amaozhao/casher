import{j as s,u as a,c as t,w as o,f as e,o as l,a as i,b as d,t as n,B as c,x as r,y as u,F as g,z as _}from"./index-CseF7hPJ.js";import{i as f}from"./index.DD8BGfc4.js";import{T as p}from"./index.CQxaDcC-.js";import{_ as m}from"./load.B3pZkcbV.js";import{_ as x}from"./http.DZ3dZdYj.js";const h=x({components:{TopDiv:p},data:()=>({isLogin:!1,proList:[]}),onShow:function(){this.getList(),console.log("index Show")},methods:{getList(){f().then((s=>{200==s.status&&(console.log(s.data,"==res.data"),this.proList=s.data||[])}))},goHomePage(){s({url:"/pages/index/index"})},goNextPage(a){s({url:"/pages/toc/toc25Product?id="+a})}}},[["render",function(s,f,p,x,h,j){const v=a("TopDiv"),C=e,L=_;return l(),t(C,{class:"flex column alignCenter bg_div"},{default:o((()=>[i(v),i(C,{class:"header_btn",onClick:f[0]||(f[0]=s=>j.goHomePage())},{default:o((()=>[d(n(s.$t("tocRecord_text1")),1)])),_:1}),i(C,{class:"product_div flex wrap justifyCenter"},{default:o((()=>[i(C,{class:"flex column alignCenter loding_div"},{default:o((()=>[i(L,{class:"load_image",src:m}),i(C,{class:"loding_text"},{default:o((()=>[d("生成中")])),_:1}),i(C,{class:"loding_text2"},{default:o((()=>[d(" 大约还需 "),c("span",{class:"loding_value"},"45"),d(" 秒 ….. ")])),_:1}),i(C,{class:"notice"},{default:o((()=>[d("一小时内未生成成功,")])),_:1}),i(C,{class:"notice2"},{default:o((()=>[d("系统自动退款")])),_:1})])),_:1}),(l(!0),r(g,null,u(h.proList,((s,a)=>(l(),t(L,{key:s.id,class:"product_image",src:s.result,onClick:a=>j.goNextPage(s.id)},null,8,["src","onClick"])))),128))])),_:1})])),_:1})}],["__scopeId","data-v-b016a483"]]);export{h as default};

import{o as e,c as t,w as s,a,b as n,t as l,d as r,A as o,f as i}from"./index-XYCATuhz.js";import{r as c,c as d,_ as u,a as f}from"./home.CuM7m_8H.js";function h(e){return c.httpRequest({url:d.imgInfo,method:"GET"},e)}function m(e){return c.httpRequest({url:d.workInfo,method:"GET"},e)}function _(e){return c.httpRequest({url:d.commentsPop,method:"POST"},e)}function p(e){return c.httpRequest({url:d.delimg,method:"DELETE"},e)}const g=u({data:()=>({list:{}}),created(){this.getBanner()},methods:{getBanner(){var e;c.httpRequest({url:d.banner,method:"GET"},e).then((e=>{200==e.status&&(this.list=e.data||{})}))},openHref(e){window.open(e)}}},[["render",function(c,d,u,h,m,_){const p=o,g=i;return 0!==Object.keys(m.list).length?(e(),t(g,{key:0,class:"flex row justifyBetween alignCenter header_div"},{default:s((()=>[a(g,{class:"flex row alignCenter title_content_view",onClick:d[1]||(d[1]=e=>_.openHref(m.list.url))},{default:s((()=>[a(g,{class:"title_btn flex alignCenter"},{default:s((()=>[a(p,{class:"header_img",src:f}),n(" "+l(c.$t("tocIndex_text1")),1)])),_:1}),a(g,{class:"title_label"},{default:s((()=>[n(l(m.list.desc),1)])),_:1}),a(g,{class:"flex row alignCenter mgR10",onClick:d[0]||(d[0]=e=>c.onLeftTab())},{default:s((()=>[a(p,{class:"header_img",src:f}),a(g,{class:"title"},{default:s((()=>[n("Deploy AI")])),_:1})])),_:1})])),_:1})])),_:1})):r("",!0)}],["__scopeId","data-v-10aa8067"]]);export{g as T,_ as c,p as d,h as i,m as w};
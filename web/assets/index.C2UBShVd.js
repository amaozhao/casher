import{o as t,c as e,w as s,a,b as n,t as l,d as r,f as o}from"./index-89Q_U4E3.js";import{r as i,c,_ as d}from"./http.Dd-U2tcs.js";function u(t){return i.httpRequest({url:c.commentsPop,method:"POST"},t)}const f=d({data:()=>({list:{}}),created(){this.getBanner()},methods:{getBanner(){var t;i.httpRequest({url:c.banner,method:"GET"},t).then((t=>{200==t.status&&(this.list=t.data||{})}))},openHref(t){window.open(t)}}},[["render",function(i,c,d,u,f,_){const h=o;return 0!==Object.keys(f.list).length?(t(),e(h,{key:0,class:"flex row justifyBetween alignCenter header_div"},{default:s((()=>[a(h,{class:"flex row alignCenter title_content_view",onClick:c[0]||(c[0]=t=>_.openHref(f.list.url))},{default:s((()=>[a(h,{class:"title_btn"},{default:s((()=>[n(l(i.$t("tocIndex_text1")),1)])),_:1}),a(h,{class:"title_label"},{default:s((()=>[n(l(f.list.desc),1)])),_:1})])),_:1})])),_:1})):r("",!0)}],["__scopeId","data-v-204c7ec0"]]);export{f as T,u as c};

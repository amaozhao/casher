import{j as t,u as e,c as s,w as i,f as a,o,a as l,b as c,t as n,B as d,z as r}from"./index-DZjkAVNJ.js";import{a as h}from"./index.D7jQgFYH.js";import{T as u}from"./index.BKgJWPnt.js";import{_ as g}from"./note2.w3RVvWxD.js";import{_ as C}from"./http.Dhq5wnZ7.js";const _=C({components:{TopDiv:u},data:()=>({isLogin:!1,href:"https://uniapp.dcloud.io/component/README?id=uniui",second:60,start:!0,timer:null,jilu_id:"",workflow_id:"",fee:""}),onLoad(t){t.jilu_id&&(this.jilu_id=t.jilu_id),t.id&&(this.workflow_id=t.id),t.fee&&(this.fee=Number(t.fee)),t.consuming&&(this.consuming=t.consuming,this.second=t.consuming)},onShow:function(){this.getResult()},methods:{getResult(){this.timer=setInterval((()=>{this.second>0&&(this.second--,h({jilu_id:this.jilu_id}).then((t=>{200==t.status&&"success"==t.data.task_status&&(this.start=!1,this.goNextPage(this.jilu_id))})),(this.second<1||!this.start)&&(this.start=!1,this.clearTimer(),this.getResult2()))}),1e3)},getResult2(){this.start=!0,this.timer=setInterval((()=>{this.second++,h({jilu_id:this.jilu_id}).then((t=>{200==t.status&&"success"==t.data.task_status&&(this.start=!1,this.goNextPage(this.jilu_id))})),this.start||(this.start=!1)}),1e3)},clearTimer(){this.timer&&(clearInterval(this.timer),this.timer=null)},goHomePage(){t({url:"/pages/index/index"})},goRecordPage(){t({url:"/pages/toc/toc24Record"})},goNextPage(e){t({url:"/pages/toc/toc25Product?id="+e})}},beforeUnmount(){this.clearTimer()}},[["render",function(t,h,u,C,_,m){const f=e("TopDiv"),p=r,x=a;return o(),s(x,{class:"flex column alignCenter bg_div"},{default:i((()=>[l(f),l(x,{class:"btn2Bottom flex",onClick:h[0]||(h[0]=t=>m.goRecordPage())},{default:i((()=>[l(p,{src:g}),l(x,{class:"goRecordPage"},{default:i((()=>[c(n(t.$t("tocIndex_text3")),1)])),_:1})])),_:1}),l(x,{class:"flex column alignCenter loding_div"},{default:i((()=>[l(p,{class:"load_image",src:"data:image/svg+xml,%3csvg%20width='59'%20height='59'%20viewBox='0%200%2059%2059'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_16_248)'%3e%3cpath%20d='M42.4796%2030.2868C42.4796%2030.0902%2042.4796%2030.0902%2042.4796%2030.2868C42.4796%2028.3202%2042.2829%2026.5502%2041.4962%2024.7802C40.9062%2023.0102%2039.9229%2021.6335%2038.5462%2020.2568C37.3662%2018.8802%2035.7929%2017.8968%2034.0229%2017.1102C32.2529%2016.3235%2030.4829%2015.9302%2028.7129%2015.9302C26.9429%2015.9302%2024.9762%2016.1268%2023.2062%2016.9135C21.4362%2017.5035%2019.8629%2018.6835%2018.4862%2019.8635C17.1096%2021.2402%2015.9296%2022.8135%2015.1429%2024.5835C14.3562%2026.3535%2013.9629%2028.3202%2013.9629%2030.0902C13.9629%2032.0568%2014.1596%2034.0235%2014.9462%2035.7935C15.7329%2037.5635%2016.7162%2039.3335%2018.0929%2040.7102C19.4696%2042.0868%2021.0429%2043.2668%2022.8129%2044.0535C24.5829%2044.8402%2026.5496%2045.2335%2028.5162%2045.4302C30.4829%2045.4302%2032.4496%2045.0368%2034.4162%2044.4468C36.3829%2043.6602%2037.9562%2042.6768%2039.5296%2041.1035C41.1029%2039.7268%2042.2829%2037.9568%2043.0696%2036.1868C43.6596%2035.0068%2043.8562%2033.8268%2044.2496%2032.6468C43.4629%2032.4502%2042.4796%2031.4668%2042.4796%2030.2868Z'%20fill='white'/%3e%3cpath%20d='M29.5%200C13.1767%200%200%2013.1767%200%2029.5C0%2045.8233%2013.1767%2059%2029.5%2059C45.8233%2059%2059%2045.8233%2059%2029.5C59%2013.1767%2045.8233%200%2029.5%200ZM47.0033%2030.09C47.0033%2031.4667%2046.02%2032.45%2044.6433%2032.45C44.6433%2032.45%2044.6433%2032.45%2044.4467%2032.45C44.25%2033.63%2044.0533%2035.0067%2043.4633%2036.1867C42.6767%2038.1533%2041.4967%2039.9233%2040.12%2041.4967C38.7433%2043.07%2036.9733%2044.25%2035.0067%2045.0367C33.04%2045.8233%2030.8767%2046.4133%2028.7133%2046.4133C26.55%2046.4133%2024.3867%2046.02%2022.42%2045.2333C20.4533%2044.4467%2018.4867%2043.2667%2016.9133%2041.6933C15.34%2040.12%2013.9633%2038.35%2013.1767%2036.3833C12.1933%2034.4167%2011.8%2032.2533%2011.8%2029.8933C11.8%2027.73%2012.1933%2025.37%2012.98%2023.4033C13.7667%2021.24%2014.9467%2019.47%2016.52%2017.7C18.0933%2016.1267%2020.06%2014.75%2022.0267%2013.7667C24.19%2012.7833%2026.3533%2012.39%2028.7133%2012.39C31.0733%2012.39%2033.2367%2012.7833%2035.4%2013.57C37.5633%2014.3567%2039.53%2015.7333%2041.3%2017.3067C43.07%2018.88%2044.4467%2020.8467%2045.2333%2023.01C46.4133%2025.37%2047.0033%2027.73%2047.0033%2030.09Z'%20fill='white'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_16_248'%3e%3crect%20width='59'%20height='59'%20fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"}),l(x,{class:"loding_text textAlign"},{default:i((()=>[c(n(t.$t("tocLoading_text1"))+" ",1),d("span",{class:"loding_value"},n(_.second),1),c(" "+n(t.$t("tocLoading_text2"))+" ….. ",1)])),_:1})])),_:1}),l(x,{class:"notice textAlign"},{default:i((()=>[c(n(t.$t("tocLoading_text3")),1)])),_:1}),l(x,{class:"notice2"},{default:i((()=>[c(n(t.$t("tocLoading_text4")),1)])),_:1}),l(x,{class:"bottom_btn",onClick:h[1]||(h[1]=t=>m.goHomePage())},{default:i((()=>[c(n(t.$t("tocLoading_text5")),1)])),_:1})])),_:1})}],["__scopeId","data-v-3a405449"]]);export{_ as default};

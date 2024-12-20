import{z as t,o as e,c as o,w as s,x as n,e as i,t as a,A as l,d as u,B as d,i as c,k as r,r as h,j as m}from"./index-B-psPONm.js";import{_ as y}from"./_plugin-vue_export-helper.BCo6x5W8.js";import{r as f}from"./uni-app.es.Cgh3b5Wp.js";import{r as p}from"./httpUtil.D_oA_U_l.js";import{_}from"./load.DB4DbRB_.js";const w={en:{"uni-countdown.day":"day","uni-countdown.h":"h","uni-countdown.m":"m","uni-countdown.s":"s"},"zh-Hans":{"uni-countdown.day":"天","uni-countdown.h":"时","uni-countdown.m":"分","uni-countdown.s":"秒"},"zh-Hant":{"uni-countdown.day":"天","uni-countdown.h":"時","uni-countdown.m":"分","uni-countdown.s":"秒"}},{t:g}=t(w);const x=y({name:"UniCountdown",emits:["timeup"],props:{showDay:{type:Boolean,default:!0},showHour:{type:Boolean,default:!0},showMinute:{type:Boolean,default:!0},showColon:{type:Boolean,default:!0},start:{type:Boolean,default:!0},backgroundColor:{type:String,default:""},color:{type:String,default:"#333"},fontSize:{type:Number,default:14},splitorColor:{type:String,default:"#333"},day:{type:Number,default:0},hour:{type:Number,default:0},minute:{type:Number,default:0},second:{type:Number,default:0},timestamp:{type:Number,default:0}},data:()=>({timer:null,syncFlag:!1,d:"00",h:"00",i:"00",s:"00",leftTime:0,seconds:0}),computed:{dayText:()=>g("uni-countdown.day"),hourText:t=>g("uni-countdown.h"),minuteText:t=>g("uni-countdown.m"),secondText:t=>g("uni-countdown.s"),timeStyle(){const{color:t,backgroundColor:e,fontSize:o}=this;return{color:t,backgroundColor:e,fontSize:`${o}px`,width:22*o/14+"px",lineHeight:20*o/14+"px",borderRadius:3*o/14+"px"}},splitorStyle(){const{splitorColor:t,fontSize:e,backgroundColor:o}=this;return{color:t,fontSize:12*e/14+"px",margin:o?4*e/14+"px":""}}},watch:{day(t){this.changeFlag()},hour(t){this.changeFlag()},minute(t){this.changeFlag()},second(t){this.changeFlag()},start:{immediate:!0,handler(t,e){if(t)this.startData();else{if(!e)return;clearInterval(this.timer)}}}},created:function(t){this.seconds=this.toSeconds(this.timestamp,this.day,this.hour,this.minute,this.second),this.countDown()},unmounted(){clearInterval(this.timer)},methods:{toSeconds:(t,e,o,s,n)=>t?t-parseInt((new Date).getTime()/1e3,10):60*e*60*24+60*o*60+60*s+n,timeUp(){clearInterval(this.timer),this.$emit("timeup")},countDown(){let t=this.seconds,[e,o,s,n]=[0,0,0,0];t>0?(e=Math.floor(t/86400),o=Math.floor(t/3600)-24*e,s=Math.floor(t/60)-24*e*60-60*o,n=Math.floor(t)-24*e*60*60-60*o*60-60*s):this.timeUp(),e<10&&(e="0"+e),o<10&&(o="0"+o),s<10&&(s="0"+s),n<10&&(n="0"+n),this.d=e,this.h=o,this.i=s,this.s=n},startData(){if(this.seconds=this.toSeconds(this.timestamp,this.day,this.hour,this.minute,this.second),this.seconds<=0)return this.seconds=this.toSeconds(0,0,0,0,0),void this.countDown();clearInterval(this.timer),this.countDown(),this.timer=setInterval((()=>{this.seconds--,this.seconds<0?this.timeUp():this.countDown()}),1e3)},update(){this.startData()},changeFlag(){this.syncFlag||(this.seconds=this.toSeconds(this.timestamp,this.day,this.hour,this.minute,this.second),this.startData(),this.syncFlag=!0)}}},[["render",function(t,r,h,m,y,f){const p=d,_=c;return e(),o(_,{class:"uni-countdown"},{default:s((()=>[h.showDay?(e(),o(p,{key:0,style:n([f.timeStyle]),class:"uni-countdown__number"},{default:s((()=>[i(a(y.d),1)])),_:1},8,["style"])):l("",!0),h.showDay?(e(),o(p,{key:1,style:n([f.splitorStyle]),class:"uni-countdown__splitor"},{default:s((()=>[i(a(f.dayText),1)])),_:1},8,["style"])):l("",!0),h.showHour?(e(),o(p,{key:2,style:n([f.timeStyle]),class:"uni-countdown__number"},{default:s((()=>[i(a(y.h),1)])),_:1},8,["style"])):l("",!0),h.showHour?(e(),o(p,{key:3,style:n([f.splitorStyle]),class:"uni-countdown__splitor"},{default:s((()=>[i(a(h.showColon?":":f.hourText),1)])),_:1},8,["style"])):l("",!0),h.showMinute?(e(),o(p,{key:4,style:n([f.timeStyle]),class:"uni-countdown__number"},{default:s((()=>[i(a(y.i),1)])),_:1},8,["style"])):l("",!0),h.showMinute?(e(),o(p,{key:5,style:n([f.splitorStyle]),class:"uni-countdown__splitor"},{default:s((()=>[i(a(h.showColon?":":f.minuteText),1)])),_:1},8,["style"])):l("",!0),u(p,{style:n([f.timeStyle]),class:"uni-countdown__number"},{default:s((()=>[i(a(y.s),1)])),_:1},8,["style"]),h.showColon?l("",!0):(e(),o(p,{key:6,style:n([f.splitorStyle]),class:"uni-countdown__splitor"},{default:s((()=>[i(a(f.secondText),1)])),_:1},8,["style"]))])),_:1})}],["__scopeId","data-v-8f544fc2"]]);let S;const b=y({data:()=>({isLogin:!1,consuming:0}),onLoad(t){this.consuming=1*t.consuming,S=setTimeout((()=>{p({url:"task/view/",method:"GET",data:{jilu_id:t.jilu_id}}).then((e=>{"success"==e.data.task_status&&r({url:"/pages/toc/toc25Product?jilu_id="+t.jilu_id})}))}),2e3)},onShow:function(){console.log("index Show")},methods:{goHomePage(){r({url:"/pages/index/index"})},goRecordPage(){r({url:"/pages/toc/toc24Record"})},goNextPage(){r({url:"/pages/toc/toc25Product"})},clearTimer(){S&&(clearTimeout(S),S=null)}},beforeUnmount(){this.clearTimer()}},[["render",function(t,n,a,l,d,r){const y=c,p=m,w=f(h("uni-countdown"),x);return e(),o(y,{class:"flex column alignCenter bg_div"},{default:s((()=>[u(y,{class:"flex row justifyBetween alignCenter header_div"},{default:s((()=>[u(y,{class:"flex row alignCenter title_content_view",onClick:n[0]||(n[0]=t=>r.goHomePage())},{default:s((()=>[u(y,{class:"title_btn"},{default:s((()=>[i(" 创建 ")])),_:1}),u(y,{class:"title_label"},{default:s((()=>[i(" 在Deploy上创建一个 Ai 应用 ")])),_:1})])),_:1}),u(y,{class:"title_btn2",onClick:n[1]||(n[1]=t=>r.goRecordPage())},{default:s((()=>[i(" 生成记录 ")])),_:1})])),_:1}),u(y,{class:"border_div"},{default:s((()=>[u(y,{class:"flex column alignCenter loding_div"},{default:s((()=>[u(p,{class:"load_image",src:_}),u(y,{class:"loding_text"},{default:s((()=>[i(" 生成中,大约还需 "),u(w,{color:"#FFE70B","font-size":20,showDay:!1,showHour:!1,showMinute:!1,second:d.consuming},null,8,["second"]),i(" 秒 ….. ")])),_:1})])),_:1})])),_:1}),u(y,{class:"notice"},{default:s((()=>[i(" 耗时较长,您可离开当前页面,在生成记录中查看进度和结果 ")])),_:1}),u(y,{class:"notice2"},{default:s((()=>[i(" 一小时内未生成成功,系统自动退款 ")])),_:1}),u(y,{class:"bottom_btn",onClick:n[2]||(n[2]=t=>r.goNextPage())},{default:s((()=>[i(" 跳过等待，去试试其他功能 ")])),_:1})])),_:1})}],["__scopeId","data-v-049c9486"]]);export{b as default};
